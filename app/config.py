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
    "jpmorgan",
    "jp morgan",
    "jpmc",
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
    "security clearance required",
]
FIT_SCORE_MINIMUM = 4
FIT_HEALTHCARE_KEYWORDS = [
    "healthcare",
    "health care",
    "life sciences",
    "pharma",
    "pharmaceutical",
    "biotech",
    "clinical",
    "payer",
    "health tech",
    "healthtech",
    "health system",
    "digital health",
    "hospital",
    "medical device",
    "therapeutics",
    "oncology",
    "patient outcomes",
    "health insurance",
    "population health",
]
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
    "quota",
]
FIT_PREFERRED_LOCATION_KEYWORDS = []
PRIORITY_COMPANY_KEYWORDS = [
    "clearview",
    "humana",
    "biogen",
    "novartis",
    "vertex",
]
SEARCH_TERMS = [
    "Healthcare Product Manager",
    "Health Analyst",
    "Life Sciences Strategy",
    "Pharma Strategy Analyst",
    "Life Sciences Analyst",
    "Digital Health Product Manager",
    "Health System Analyst",
    "Associate Product Manager",
]
TARGET_LOCATIONS = [
    "New York, New York, United States",
    "Chicago, Illinois, United States",
    "San Francisco, California, United States",
    "Boston, Massachusetts, United States",
]
MAX_JOBS_PER_DAY = 40
ALLOWED_TITLE_PATTERNS = [
    # Product roles
    "associate product manager",
    "product manager",
    "product strategy",
    "product management",
    "growth product manager",
    "product operations",
    "product analyst",
    # Healthcare / life sciences — broad enough to catch real job title variants
    "healthcare",
    "health analyst",
    "health system",
    "health policy",
    "health economics",
    "digital health",
    "population health",
    "clinical analyst",
    "clinical strategy",
    "clinical operations",
    "medical affairs",
    "care management",
    "life sciences",
    "pharma",
    "biotech",
    "therapeutics",
    # Strategy / consulting
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
    "manager, product management",
    "intern",
    "internship",
    "co-op",
    "coop",
    "summer",
    "part-time",
    "part time",
    "contract",
    # Clinical / hands-on roles not relevant to PM/analyst search
    "pharmacist",
    "pharmacy technician",
    "registered nurse",
    "nurse practitioner",
    "physician",
    # Sales roles
    "sales representative",
    "account executive",
    "account manager",
]
FIT_STRONG_TITLE_PATTERNS = [
    "healthcare",
    "health analyst",
    "health system",
    "clinical analyst",
    "clinical strategy",
    "digital health",
    "population health",
    "life sciences",
    "pharma",
    "biotech",
    "associate product manager",
    "product strategy",
    "product manager",
    "strategy associate",
    "strategy analyst",
    "associate consultant",
]
