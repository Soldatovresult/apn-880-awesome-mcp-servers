# Docker MCP Server

Community MCP server for Docker — manage containers, images, volumes, and compose stacks.

**Source:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Installation

```bash
npx -y @modelcontextprotocol/server-docker
```

Requires Docker daemon running on the host.

## Configuration

```json
{
  "mcpServers": {
    "docker": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-docker"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `list_containers` | List running containers |
| `start_container` | Start a container |
| `stop_container` | Stop a container |
| `list_images` | List Docker images |
| `pull_image` | Pull an image from registry |
| `run_container` | Run a new container |
| `container_logs` | Get container logs |

## Use Case

Deploy and manage microservices, run batch jobs, manage dev environments.
