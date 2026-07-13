# Slack MCP Server

Official MCP server for Slack — read messages, post messages, search channels, manage threads.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-slack
```

## Configuration

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-...",
        "SLACK_TEAM_ID": "T..."
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `post_message` | Send a message to a channel |
| `search_messages` | Search messages by query |
| `get_channel_history` | Get recent messages |
| `list_channels` | List accessible channels |
| `reply_to_thread` | Reply in a thread |

## Requirements

- Slack app with `chat:write`, `channels:history`, `search:read` scopes
- Bot token with `chat:write.public` for public channels

## Example

```
User: "Post a summary of today's standup to #general"
Agent: [calls post_message with channel and formatted summary]
```
