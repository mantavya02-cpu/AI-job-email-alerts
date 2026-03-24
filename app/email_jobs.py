from __future__ import annotations

import os
import smtplib
from dataclasses import dataclass
from datetime import datetime
from email.message import EmailMessage


@dataclass
class EmailSettings:
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    to_address: str
    from_address: str
    use_tls: bool = True


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def build_email_settings(recipient_override: str = "") -> EmailSettings | None:
    to_address = recipient_override or get_env("RECRUITING_BOT_EMAIL_TO")
    smtp_host = get_env("RECRUITING_BOT_SMTP_HOST")
    smtp_port = get_env("RECRUITING_BOT_SMTP_PORT", "587")
    smtp_username = get_env("RECRUITING_BOT_SMTP_USERNAME")
    smtp_password = get_env("RECRUITING_BOT_SMTP_PASSWORD")
    from_address = get_env("RECRUITING_BOT_EMAIL_FROM", smtp_username)
    use_tls = get_env("RECRUITING_BOT_SMTP_USE_TLS", "true").lower() not in {"0", "false", "no"}

    if not all([to_address, smtp_host, smtp_port, smtp_username, smtp_password, from_address]):
        return None

    return EmailSettings(
        smtp_host=smtp_host,
        smtp_port=int(smtp_port),
        smtp_username=smtp_username,
        smtp_password=smtp_password,
        to_address=to_address,
        from_address=from_address,
        use_tls=use_tls,
    )


def build_jobs_email_message(job_list: list[dict[str, str]], source_label: str) -> EmailMessage:
    message = EmailMessage()
    today_label = datetime.now().strftime("%m/%d/%Y")
    message["Subject"] = f"{source_label} jobs for {today_label} ({len(job_list)})"

    lines = [
        f"{source_label} job summary for {today_label}",
        "",
    ]

    if not job_list:
        lines.append("No jobs matched this run.")
    else:
        for index, job in enumerate(job_list, start=1):
            posted_at = job.get("posted_at") or "unknown recency"
            lines.append(
                f"{index}. {job['title']} | {job['company']} | {job['location']} | {posted_at}"
            )
            lines.append(job["link"])
            lines.append("")

    message.set_content("\n".join(lines).rstrip() + "\n")
    return message


def build_digest_email_message(
    job_list: list[dict[str, str]],
    digest_label: str,
    source_label: str = "Jobs Digest",
) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = f"{source_label} for {digest_label} ({len(job_list)})"

    lines = [
        f"{source_label} for {digest_label}",
        "",
    ]

    if not job_list:
        lines.append("No jobs were collected for this digest window.")
    else:
        for index, job in enumerate(job_list, start=1):
            lines.append(f"{index}. {job['title']} | {job['company']} | {job['location']}")
            lines.append(job["link"])
            lines.append("")

    message.set_content("\n".join(lines).rstrip() + "\n")
    return message


def send_job_summary_email(
    job_list: list[dict[str, str]],
    source_label: str,
    recipient_override: str = "",
) -> bool:
    settings = build_email_settings(recipient_override=recipient_override)
    if settings is None:
        return False

    message = build_jobs_email_message(job_list=job_list, source_label=source_label)
    message["From"] = settings.from_address
    message["To"] = settings.to_address

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
        if settings.use_tls:
            smtp.starttls()
        smtp.login(settings.smtp_username, settings.smtp_password)
        smtp.send_message(message)

    return True


def send_digest_email(
    job_list: list[dict[str, str]],
    digest_label: str,
    source_label: str = "Jobs Digest",
    recipient_override: str = "",
) -> bool:
    settings = build_email_settings(recipient_override=recipient_override)
    if settings is None:
        return False

    message = build_digest_email_message(
        job_list=job_list,
        digest_label=digest_label,
        source_label=source_label,
    )
    message["From"] = settings.from_address
    message["To"] = settings.to_address

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
        if settings.use_tls:
            smtp.starttls()
        smtp.login(settings.smtp_username, settings.smtp_password)
        smtp.send_message(message)

    return True


def send_test_email(
    recipient_override: str,
    subject: str = "AI Job Email Alerts Test Email",
    body: str = "This is a test email from AI Job Email Alerts.",
) -> bool:
    settings = build_email_settings(recipient_override=recipient_override)
    if settings is None:
        return False

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = settings.from_address
    message["To"] = settings.to_address
    message.set_content(body.rstrip() + "\n")

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
        if settings.use_tls:
            smtp.starttls()
        smtp.login(settings.smtp_username, settings.smtp_password)
        smtp.send_message(message)

    return True
