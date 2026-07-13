# Playwright MCP Server

Official MCP server for browser automation — navigate, click, fill forms, extract data, take screenshots.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-playwright
```

## Configuration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `navigate` | Go to a URL |
| `click` | Click an element |
| `fill` | Fill an input field |
| `evaluate` | Run JavaScript in page |
| `screenshot` | Take page screenshot |
| `get_text` | Extract page text |
| `pdf` | Generate PDF of page |

## Headless Mode

Runs Chromium in headless mode by default. Requires Playwright browsers:

```bash
npx playwright install chromium
```

## Example

```
User: "Log into the admin dashboard and get the metrics"
Agent: [calls navigate to URL, fill credentials, click login, get_text]
```
