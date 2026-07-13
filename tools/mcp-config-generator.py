"""MCP Config Generator — generate Claude Desktop config for selected servers.

Usage: python tools/mcp-config-generator.py
"""

import json
import sys


SERVERS_CATALOG = {
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
        "env": {},
        "description": "File system access",
    },
    "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {"GITHUB_TOKEN": "<your-token>"},
        "description": "GitHub API access",
    },
    "brave-search": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {"BRAVE_API_KEY": "<your-key>"},
        "description": "Web search via Brave",
    },
    "fetch": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-fetch"],
        "env": {},
        "description": "Fetch web content",
    },
    "playwright": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-playwright"],
        "env": {},
        "description": "Browser automation",
    },
    "slack": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-slack"],
        "env": {"SLACK_BOT_TOKEN": "xoxb-...", "SLACK_TEAM_ID": "T..."},
        "description": "Slack messaging",
    },
    "memory": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"],
        "env": {"MEMORY_FILE_PATH": "/path/to/memory.json"},
        "description": "Persistent memory",
    },
    "sqlite": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sqlite", "/path/to/db.sqlite"],
        "env": {},
        "description": "SQLite database",
    },
    "postgres": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-postgres"],
        "env": {"DATABASE_URL": "postgresql://user:pass@localhost:5432/db"},
        "description": "PostgreSQL database",
    },
    "docker": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-docker"],
        "env": {},
        "description": "Docker container management",
    },
    "sentry": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sentry"],
        "env": {"SENTRY_AUTH_TOKEN": "<token>", "SENTRY_ORG": "my-org"},
        "description": "Sentry error tracking",
    },
}


def generate_config(selected: list[str]) -> dict:
    config = {"mcpServers": {}}
    for name in selected:
        if name in SERVERS_CATALOG:
            entry = SERVERS_CATALOG[name]
            server_config = {
                "command": entry["command"],
                "args": entry["args"],
            }
            if entry["env"]:
                server_config["env"] = entry["env"]
            config["mcpServers"][name] = server_config
    return config


def main():
    print("MCP Config Generator\n")
    print("Available servers:")
    for name, info in SERVERS_CATALOG.items():
        print(f"  [{name:15}] {info['description']}")

    if len(sys.argv) > 1:
        selected = sys.argv[1:]
    else:
        print("\nUsage: python mcp-config-generator.py server1 server2 ...")
        print("Example: python mcp-config-generator.py filesystem github brave-search")
        sys.exit(1)

    config = generate_config(selected)
    print("\nGenerated Config:\n")
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()
