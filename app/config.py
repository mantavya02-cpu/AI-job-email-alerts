from __future__ import annotations

from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent
LOCAL_TIMEZONE = "America/New_York"
PROFILE_NOTES_FILE = PROJECT_ROOT / "docs" / "profile_notes.md"
DEFAULT_SHEETS_CREDENTIALS = PROJECT_ROOT / "keys" / "google-credentials.json"
OLLAMA_BASE_URL = "https://ollama.com"
OLLAMA_MODEL = "gemma3:4b-cloud"
OLLAMA_SHORTLIST_SIZE = 6
OLLAMA_MIN_FIT_SCORE = 6
OLLAMA_APPROVED_MAX_PER_RUN = 15
DEFAULT_SHEETS_URL = "https://docs.google.com/spreadsheets/d/14m287_XzZc-rN6-MNhXOMnN5cIiSAoDs2V9GPgqNmRY"
DEFAULT_SHEETS_TAB = "Jobs"
ARCHIVED_SHEETS_TAB = "Archived Jobs"
JOBSPY_SITES = [
    "linkedin",
    "indeed",
]
JOBSPY_HOURS_OLD = 24
JOBSPY_COUNTRY_INDEED = "USA"
JOBSPY_BIG_COMPANY_EMPLOYEE_MARKERS = [
    "1001 to 5,000",
    "5001 to 10,000",
    "10,000+",
]
JOBSPY_BLOCKED_COMPANY_KEYWORDS = [
    "deloitte",
]
JOBSPY_BLOCKED_RECRUITER_KEYWORDS = [
    "teksystems",
    "optomi",
    "motion recruitment",
    "cybercoders",
    "recruit",
    "staffing",
]
VISA_RESTRICTION_KEYWORDS = [
    "no sponsorship",
    "no visa sponsorship",
    "no work visa",
    "not able to sponsor",
    "unable to sponsor",
    "cannot sponsor",
    "we do not sponsor",
    "does not sponsor",
    "sponsorship is not available",
    "sponsorship not available",
    "not eligible for sponsorship",
    "ineligible for sponsorship",
    "sponsorship cannot be provided",
    "must be a us citizen",
    "must be a u.s. citizen",
    "us citizens only",
    "u.s. citizens only",
    "citizen or permanent resident only",
    "active security clearance required",
    "top secret clearance required",
    "secret clearance required",
    "active secret clearance",
    "requires secret clearance",
    "clearance required",
    "security clearance required",
]
FIT_SCORE_MINIMUM = 4
FIT_DESCRIPTION_POSITIVE_KEYWORDS = [
    "mba",
    "new grad",
    "early career",
    "0-2 years",
    "0-3 years",
    "1-3 years",
    "consumer",
    "b2c",
    "growth",
    "experimentation",
    "analytics",
    "platform",
    "roadmap",
    "product strategy",
]
FIT_DESCRIPTION_NEGATIVE_KEYWORDS = [
    "7+ years",
    "8+ years",
    "10+ years",
    "staff",
    "principal",
    "director",
    "vp",
    "vice president",
    "quota",
    "sales",
]
FIT_PREFERRED_LOCATION_KEYWORDS = []
SEARCH_TERMS = [
    "Associate Product Manager",
    "MBA Product Manager",
    "Healthcare Analyst",
    "Strategy Associate",
]
TARGET_LOCATIONS = [
    "New York, New York, United States",
    "Chicago, Illinois, United States",
    "San Francisco, California, United States",
    "Boston, Massachusetts, United States",
]
MAX_JOBS_PER_DAY = 40
ALLOWED_TITLE_PATTERNS = [
    "associate product manager",
    "product manager",
    "product strategy",
    "product management",
    "growth product manager",
    "product operations",
    "product analyst",
    "healthcare analyst",
    "strategy analyst",
    "strategy associate",
    "business analyst",
    "management consultant",
    "consulting analyst",
    "associate consultant",
]
BLOCKED_TITLE_PATTERNS = [
    "senior",
    "sr.",
    "staff",
    "principal",
    "director",
    "head of",
    "vice president",
    "vp ",
    "lead ",
    "group product manager",
    "chief ",
    "technical product manager",
    "security product manager",
    "internal systems",
    "founding product manager",
    "clinical product manager",
    "manager, product management",
]
FIT_STRONG_TITLE_PATTERNS = [
    "associate product manager",
    "product manager intern",
    "product strategy",
    "product manager",
    "strategy associate",
    "strategy analyst",
    "healthcare analyst",
    "associate consultant",
]
