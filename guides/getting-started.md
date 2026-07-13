# Getting Started with MCP

The Model Context Protocol (MCP) lets AI agents use external tools, data sources, and services through a standardized interface.

## What is MCP?

MCP is an open protocol developed by Anthropic that standardizes how AI applications connect to external tools and data. Think of it as "USB-C for AI" — one interface for all tools.

## How It Works

```
Agent ←→ MCP Client ←→ MCP Server ←→ External Service (API, DB, Filesystem)
```

## Quick Start

### 1. Install Node.js

MCP servers are distributed via npm. Install Node.js 18+:

```bash
node --version
```

### 2. Choose a Server

Pick from this collection — start with `filesystem` and `brave-search`:

```bash
npx -y @modelcontextprotocol/server-filesystem /tmp
npx -y @modelcontextprotocol/server-brave-search
```

### 3. Configure Your Client

- **Claude Desktop**: Edit `claude_desktop_config.json`
- **Custom client**: Use the MCP SDK

### 4. Use It!

Ask your agent questions like:
- "Read the file at /tmp/notes.txt"
- "Search the web for latest AI news"
- "Query my database for users"

## Next Steps

- Browse the server collection in this repo
- Try the health check tool: `python tools/mcp-health-check.py`
- Build your own server using the Python template
