# SQLite MCP Server

Community MCP server for SQLite databases — query, create tables, insert data, run migrations.

**Source:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-sqlite
```

## Configuration

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "/path/to/database.db"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `query` | Execute a SELECT query |
| `execute` | Execute INSERT/UPDATE/DELETE |
| `list_tables` | List all tables |
| `describe_table` | Show table schema |

## Safety

- Read-only queries by default for non-SELECT
- Transactions auto-rollback on error
- File path restricted to allowed directory

## Example

```
User: "Show me all users who signed up last week"
Agent: [calls query with SQL]
```
