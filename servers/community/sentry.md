# Sentry MCP Server

Community MCP server for Sentry — query errors, view stack traces, manage issues.

**Source:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-sentry
```

## Configuration

```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "<your-auth-token>",
        "SENTRY_ORG": "my-org"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `list_projects` | List Sentry projects |
| `list_issues` | List recent issues |
| `get_issue` | Get issue details with stack trace |
| `search_issues` | Search issues by query |
| `get_event` | Get specific event details |

## Example

```
User: "What errors happened in production in the last hour?"
Agent: [calls list_issues with timeframe filter]
```
