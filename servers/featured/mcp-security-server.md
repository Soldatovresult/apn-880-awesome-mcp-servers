# Security MCP Server (from agent-security-kit)

An MCP security server that validates inputs, checks outputs, and scans for threats — built from `agent-security-kit`.

**Source:** [github.com/FreeAutomation-Tech/agent-security-kit](https://github.com/FreeAutomation-Tech/agent-security-kit)

## Installation

```bash
git clone https://github.com/FreeAutomation-Tech/agent-security-kit.git
cd agent-security-kit
pip install mcp
python examples/secure_agent.py
```

## Configuration

```json
{
  "mcpServers": {
    "agent-security": {
      "command": "python",
      "args": ["path/to/examples/secure_agent.py"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `validate_input` | Check for injection patterns |
| `check_output` | Scan for PII/secrets |
| `scan_config` | Scan config files for security issues |
