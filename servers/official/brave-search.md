# Brave Search MCP Server

Official MCP server for web search via Brave Search API — web results, news, and local search.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-brave-search
```

## Configuration

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "<your-api-key>"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `brave_web_search` | General web search |
| `brave_local_search` | Local business/places search |

## Pricing

- Free tier: 2,000 queries/month
- Pro: 15,000 queries/month ($7.99)

## Example

```
User: "What are the latest AI news?"
Agent: [calls brave_web_search with query "AI news 2026"]
```
