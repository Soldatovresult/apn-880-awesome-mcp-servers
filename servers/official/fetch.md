# Fetch MCP Server

Official MCP server for fetching web content — HTML to markdown conversion, screenshot capture.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-fetch
```

## Configuration

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `fetch` | Fetch URL and convert to markdown |
| `screenshot` | Capture page screenshot |

## Features

- Automatic HTML-to-markdown conversion
- Handles JavaScript-rendered pages (via Puppeteer for screenshots)
- Respects robots.txt
- Configurable user agent

## Example

```
User: "Summarize the content at https://example.com"
Agent: [calls fetch with URL]
```
