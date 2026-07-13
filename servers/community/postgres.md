# PostgreSQL MCP Server

Community MCP server for PostgreSQL — query databases, explore schemas, manage tables.

**Source:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-postgres
```

## Configuration

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/mydb"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `query` | Execute read-only query |
| `execute` | Execute write query |
| `list_tables` | List all tables in schema |
| `describe_table` | Show table schema and indexes |

## Safety

- Connection string via env var only (not in config)
- Read-only mode for `query` tool
- Query timeout: 30s default

## Example

```
User: "What's the total revenue by month for Q2?"
Agent: [calls query with SQL aggregation]
```
