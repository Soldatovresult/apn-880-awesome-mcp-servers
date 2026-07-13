# Custom MCP Client Configuration

Connect MCP servers from any custom client or application.

## Python Client

```python
import asyncio
from mcp import ClientSession, StdioServerParameters

async def main():
    server = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
    )
    async with ClientSession(server) as session:
        tools = await session.list_tools()
        for tool in tools:
            print(f"{tool.name}: {tool.description}")

asyncio.run(main())
```

## TypeScript Client

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js"
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js"

const transport = new StdioClientTransport({
  command: "npx",
  args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
})

const client = new Client({ name: "my-client", version: "1.0.0" })
await client.connect(transport)
const tools = await client.listTools()
```

## HTTP/SSE Transport

```json
{
  "mcpServers": {
    "remote-server": {
      "url": "https://mcp.mycompany.com/sse",
      "headers": {
        "Authorization": "Bearer <token>"
      }
    }
  }
}
```
