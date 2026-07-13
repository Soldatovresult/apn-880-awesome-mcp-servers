# Python MCP Server Template

A minimal but complete Python MCP server template.

## Template

```python
"""My MCP Server"""
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

server = Server("my-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="my_tool",
            description="What this tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Description of param1",
                    },
                },
                "required": ["param1"],
            },
        ),
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict
) -> list[types.TextContent]:
    if name == "my_tool":
        result = f"Hello, {arguments['param1']}!"
        return [types.TextContent(type="text", text=result)]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="my-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Run

```bash
pip install mcp
python my_server.py
```
