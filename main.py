import re
import requests
import json
from datetime import datetime
from typing import Dict, Optional, List


class RepoCommitQuery:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)

    @staticmethod
    def load_config(config_file: str) -> Dict:
        """Load configuration from JSON file."""
        with open(config_file, "r") as file:
            return json.load(file)

    @staticmethod
    def validate_iso8601_date(date_str: str) -> bool:
        """Validate date format conforms to ISO 8601 standard (e.g., YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)."""
        iso8601_date_regex = r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?$"
        return bool(re.match(iso8601_date_regex, date_str))

    @staticmethod
    def validate_date_range(since: str, until: str) -> bool:
        """Ensure since date is earlier than or equal to until date."""
        # Convert date strings to datetime objects, defaulting to 00:00:00 if time is not specified
        since_date = datetime.fromisoformat(since.replace("Z", ""))
        until_date = datetime.fromisoformat(until.replace("Z", ""))
        return since_date <= until_date

    def query_commits(self, api_mode: str, org: str, repo: str, branch: str, since: str, until: str) -> Optional[List[Dict]]:
        """
        Query commits from a specified repository and branch within a specified time range.
        """
        # ISO 8601 date format and range validation
        if not (self.validate_iso8601_date(since) and self.validate_iso8601_date(until)):
            print("Invalid date format. Please use ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ).")
            return None
        if not self.validate_date_range(since, until):
            print("Invalid date range. 'Since' date must be earlier than or equal to 'Until' date.")
            return None

        # Load platform configuration
        platform_config = self.config.get(api_mode)
        if not platform_config:
            print(f"Unsupported API mode '{api_mode}'. Check config file.")
            return None

        # Prepare request details
        url = platform_config["url"].format(org=org, repo=repo)
        token = platform_config["token"]
        headers = {"Authorization": f"token {token}"}
        params = {
            "sha": branch,
            "since": since if "T" in since else f"{since}T00:00:00Z",
            "until": until if "T" in until else f"{until}T23:59:59Z"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching commits from {api_mode}: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Load configuration
    config_file = "config.json"
    commit_query = RepoCommitQuery(config_file=config_file)

    # Query parameters
    api_mode = "github"  # or "gitee" or "gitlab"
    org = "user_or_org"
    repo = "repository_name"
    branch = "main"
    since = "2024-01-01"         # ISO 8601 without time
    until = "2024-01-31T23:59:59Z"  # ISO 8601 with time

    # Fetch commits
    commits = commit_query.query_commits(api_mode, org, repo, branch, since, until)
    if commits:
        print(commits)
