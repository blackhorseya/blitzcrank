import requests


def upload_to_github(repo: str, path: str, token: str, content: str, commit_message: str = "Updated via API"):
    """
    Upload a file to GitHub repository using GitHub API.

    Args:
    repo (str): Repository name including username, e.g., 'username/repo'.
    path (str): Path where the file will be located in the repository, e.g., 'folder/file.md'.
    token (str): GitHub personal access token.
    content (str): Content to be uploaded.
    commit_message (str): Commit message for the operation.

    Returns:
    str: Response from GitHub API or error message.
    """
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the sha of the file if it exists
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json()['sha']
    else:
        sha = None

    # Prepare the data for updating or creating the file
    data = {
        "message": commit_message,
        "content": content.encode("utf-8").decode("utf-8"),
    }
    if sha:
        data["sha"] = sha

    # Make the request to create or update the file
    response = requests.put(url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        return "File uploaded/updated successfully."
    else:
        return f"Failed to upload/update file: {response.json()}"

# Uncomment the following line to test the function
# upload_to_github('username/repo', 'path/to/file.md', 'your_github_token', 'Hello, world! Content of the file.')
