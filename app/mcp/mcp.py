from datetime import datetime
from typing import Dict, List

from mcp.server.fastmcp import FastMCP
from app.datasources.candidates import candidates
from app.datasources.job_postings import job_postings
from app.datasources.interviews import interviews

# ------------------------------------------------------------------------------
# Initialize FastMCP instance with a namespace label for the service
# ------------------------------------------------------------------------------
mcp = FastMCP("Recruitement Services")

# ------------------------------------------------------------------------------
# RESOURCES: MCP resources are read-only and can be accessed via URI-based keys.
# ------------------------------------------------------------------------------


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    MCP Resource: greeting://{name}
    Returns a simple personalized greeting.
    Example: greeting://Alice → "Hello, Alice!"
    """
    return f"Hello, {name}!"


@mcp.resource("candidate://{candidate_id}")
def get_candidate(candidate_id: str) -> Dict:
    """
    MCP Resource: candidate://{candidate_id}
    Fetches candidate details using their candidate_id.
    Example: candidate://C123 → { ... candidate info ... }
    """
    candidate = next((c for c in candidates if c["candidate_id"] == candidate_id), None)
    if not candidate:
        return {"error": "Candidate not found"}
    return candidate


@mcp.resource("job://{job_id}")
def get_job(job_id: str) -> Dict:
    """
    MCP Resource: job://{job_id}
    Retrieves job posting information by job_id.
    Example: job://J101 → { ... job posting info ... }
    """
    job = next((j for j in job_postings if j["job_id"] == job_id), None)
    if not job:
        return {"error": "Job not found"}
    return job


@mcp.resource("interview://{interview_id}")
def get_interview(interview_id: str) -> Dict:
    """
    MCP Resource: interview://{interview_id}
    Retrieves interview details using interview_id.
    Example: interview://I203 → { ... interview info ... }
    """
    interview = next((i for i in interviews if i["interview_id"] == interview_id), None)
    if not interview:
        return {"error": "Interview not found"}
    return interview


@mcp.resource("interviewlist://date/{date}")
def get_interviews_by_date(date: str) -> List[Dict]:
    """
    MCP Resource: interviewlist://date/{date}
    Returns a list of interviews scheduled on the specified date (YYYY-MM-DD).
    Example: interviewlist://date/2025-05-28
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return [{"error": "Invalid date format. Use YYYY-MM-DD."}]
    
    return [
        interview for interview in interviews
        if datetime.strptime(interview["scheduled_time"], "%Y-%m-%dT%H:%M:%S").date() == target_date
    ]

# ------------------------------------------------------------------------------
# TOOLS: MCP tools expose functions that can perform operations (CRUD, search).
# ------------------------------------------------------------------------------


@mcp.tool()
def create_candidate(candidate: Dict) -> str:
    """
    MCP Tool: create_candidate
    Adds a new candidate to the list.
    Input: { "candidate_id": "C456", "name": "Bob", "skills": [...] }
    """
    candidates.append(candidate)
    return "Candidate added"


@mcp.tool()
def update_candidate(candidate_id: str, updates: Dict) -> str:
    """
    MCP Tool: update_candidate
    Updates an existing candidate's fields by ID.
    Input: candidate_id = "C123", updates = { "skills": ["Python"] }
    """
    candidate = next((c for c in candidates if c["candidate_id"] == candidate_id), None)
    if not candidate:
        return "Candidate not found"
    candidate.update(updates)
    return "Candidate updated"


@mcp.tool()
def delete_candidate(candidate_id: str) -> str:
    """
    MCP Tool: delete_candidate
    Deletes a candidate using their candidate_id.
    Input: candidate_id = "C123"
    """
    global candidates
    candidates = [c for c in candidates if c["candidate_id"] != candidate_id]
    return "Candidate deleted"


@mcp.tool()
def list_candidates() -> List[Dict]:
    """
    MCP Tool: list_candidates
    Returns the full list of all candidates.
    Useful for directory/bulk views.
    """
    return candidates


@mcp.tool()
def search_candidates_by_skill(skill: str) -> List[Dict]:
    """
    MCP Tool: search_candidates_by_skill
    Searches for candidates who possess a specific skill.
    Input: skill = "Python"
    Returns: List of matching candidates
    """
    return [c for c in candidates if skill in c["skills"]]


@mcp.tool()
def list_interviews_by_date(date: str) -> List[Dict]:
    """
    MCP Tool: list_interviews_by_date
    Returns interviews scheduled on the specified date (YYYY-MM-DD).
    Can be used in dashboards, scheduling bots, etc.
    """
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    filtered_interviews = [
        interview for interview in interviews
        if datetime.strptime(interview["scheduled_time"], "%Y-%m-%dT%H:%M:%S").date() == target_date
    ]
    return filtered_interviews
