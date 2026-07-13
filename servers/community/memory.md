# Memory MCP Server

Community MCP server for persistent memory — store, recall, and search agent memories across sessions.

**Source:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-memory
```

## Configuration

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "/path/to/memory.json"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `store_memory` | Store a key-value memory |
| `recall_memory` | Recall memory by key |
| `search_memories` | Semantic search across memories |
| `list_memories` | List all stored memories |
| `delete_memory` | Delete a memory |

## Storage

- Default: JSON file (simple, portable)
- Custom: Set `MEMORY_FILE_PATH` env var

## Use Case

Persist agent learnings across sessions for long-running assistants.
