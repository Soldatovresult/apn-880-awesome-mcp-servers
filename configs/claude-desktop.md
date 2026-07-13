# Claude Desktop Configuration

Configure MCP servers in Claude Desktop for local AI assistant with tool access.

## Configuration File

**Path:** `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)  
**Path:** `%APPDATA%\Claude\claude_desktop_config.json` (Windows)

## Full Example

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_..."
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "..."
      }
    },
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "/Users/me/data/app.db"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "/Users/me/.claude-memory.json"
      }
    }
  }
}
```

## Tips

- Restart Claude Desktop after changing config
- Check logs at `~/Library/Logs/Claude/mcp*.log` (macOS)
- Test a server: `npx -y @modelcontextprotocol/server-filesystem /tmp/test`
