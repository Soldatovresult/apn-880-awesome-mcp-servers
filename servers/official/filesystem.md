# Filesystem MCP Server

Official MCP server for file system access — read, write, move, search files with configurable permissions.

**Source:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/dir
```

## Configuration

### Claude Desktop

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/me/projects",
        "/Users/me/data"
      ]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `read_file` | Read file contents |
| `write_file` | Write content to file |
| `edit_file` | Edit specific lines |
| `search_files` | Regex search across files |
| `list_directory` | List directory entries |
| `move_file` | Move/rename files |

## Allowed Directories

The server restricts access to explicitly allowed directories. Specify multiple directories as arguments.

## Example

```
User: "Find all TODO comments in my project"
Agent: [calls search_files in /Users/me/projects with pattern "TODO"]
```
