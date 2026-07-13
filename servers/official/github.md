# GitHub MCP Server

Official MCP server for GitHub API — manage repos, issues, PRs, code search, and more.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
**Stars:** 31K+

## Installation

```bash
npx -y @modelcontextprotocol/server-github
```

## Configuration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "<your-token>"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `create_repository` | Create a new repo |
| `search_repositories` | Search repos by query |
| `create_issue` | Create an issue |
| `search_issues` | Search issues and PRs |
| `get_issue` | Get issue details |
| `add_issue_comment` | Comment on an issue |
| `search_code` | Search code in repos |
| `list_pull_requests` | List PRs for a repo |
| `get_pull_request` | Get PR details |
| `merge_pull_request` | Merge a PR |

## Requirements

- `GITHUB_TOKEN` env var with `repo` and `workflow` scopes
- Or use `gh auth token` for local setups

## Example

```
User: "Show me open issues labeled 'bug' in my repo"
Agent: [calls search_issues with repo and labels]
```
