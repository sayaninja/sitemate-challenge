from fastapi import APIRouter, HTTPException
import json

from models.issue import Issue, IssueIn

router = APIRouter()


# File name where the issues will be stored
FILE_NAME = "issues.json"

# Load existing issues or create an empty list if no file exists
def load_issues():
    try:
        with open(FILE_NAME, 'r') as f:
            return [Issue(**issue) for issue in json.load(f)]
    except FileNotFoundError:
        return []

# Save the issues to the JSON file
def save_issues(issues):
    with open(FILE_NAME, 'w') as f:
        json.dump([issue.dict() for issue in issues], f)

@router.post("/", response_model=Issue)
def create_issue(issue: IssueIn):
    issues = load_issues()
    # Assign an ID to the new issue
    issue_id = len(issues) + 1 if issues else 1
    new_issue = Issue(**issue.dict(), id=issue_id)
    issues.append(new_issue)
    print(issues)
    save_issues(issues)
    return new_issue

@router.get("/")
def read_issue():
    return load_issues()

@router.put("/{issue_id}", response_model=Issue)
def update_issue(issue_id: int, issue_data: IssueIn):
    issues = load_issues()
    for issue in issues:
        if issue.id == issue_id:
            issue.title = issue_data.title
            issue.description = issue_data.description
            save_issues(issues)
            return issue
    raise HTTPException(status_code=404, detail="Issue not found")

@router.delete("/{issue_id}")
def delete_issue(issue_id: int):
    issues = load_issues()
    for issue in issues:
        if issue.id == issue_id:
            issues.remove(issue)
            save_issues(issues)
            return {"status": "Issue deleted"}
    raise HTTPException(status_code=404, detail="Issue not found")
