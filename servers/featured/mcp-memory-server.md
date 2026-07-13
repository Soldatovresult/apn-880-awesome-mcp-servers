# Memory MCP Server (from agent-memory-kit)

An enhanced MCP memory server with episodic and semantic memory, built on the patterns from `agent-memory-kit`.

**Source:** [github.com/FreeAutomation-Tech/agent-memory-kit](https://github.com/FreeAutomation-Tech/agent-memory-kit)

## Installation

```bash
git clone https://github.com/FreeAutomation-Tech/agent-memory-kit.git
cd agent-memory-kit
pip install mcp
python examples/mcp_memory_server.py
```

## Configuration

```json
{
  "mcpServers": {
    "agent-memory": {
      "command": "python",
      "args": ["path/to/examples/mcp_memory_server.py"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `store_episode` | Store an episodic memory |
| `recall_episodes` | Recall recent episodic memories |
| `store_knowledge` | Store semantic knowledge |
| `recall_knowledge` | Recall semantic knowledge |
