"""MCP Health Check — test if MCP servers are running and responding.

Usage: python tools/mcp-health-check.py
"""

import json
import subprocess
import sys
from dataclasses import dataclass, field


@dataclass
class ServerStatus:
    name: str
    command: str
    status: str
    error: str | None = None


def check_server(name: str, command: list[str]) -> ServerStatus:
    try:
        result = subprocess.run(
            command + ["--version"] if "--version" not in str(command) else command,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return ServerStatus(name=name, command=" ".join(command), status="OK")
        else:
            return ServerStatus(
                name=name,
                command=" ".join(command),
                status="ERROR",
                error=result.stderr[:200],
            )
    except FileNotFoundError:
        return ServerStatus(
            name=name,
            command=" ".join(command),
            status="NOT_FOUND",
            error="Command not found",
        )
    except subprocess.TimeoutExpired:
        return ServerStatus(
            name=name,
            command=" ".join(command),
            status="TIMEOUT",
            error="Server did not respond in 10s",
        )


def check_npx_package(package: str) -> ServerStatus:
    return check_server(
        package,
        ["npx", "-y", package, "--help"],
    )


def main():
    servers = [
        "@modelcontextprotocol/server-filesystem",
        "@modelcontextprotocol/server-github",
        "@modelcontextprotocol/server-brave-search",
        "@modelcontextprotocol/server-fetch",
        "@modelcontextprotocol/server-playwright",
        "@modelcontextprotocol/server-slack",
        "@modelcontextprotocol/server-memory",
        "@modelcontextprotocol/server-sqlite",
        "@modelcontextprotocol/server-postgres",
        "@modelcontextprotocol/server-docker",
        "@modelcontextprotocol/server-sentry",
    ]

    print("MCP Health Check\n")
    print(f"{'Server':<45} {'Status':<12} {'Error'}")
    print("-" * 80)

    results = []
    for pkg in servers:
        status = check_npx_package(pkg)
        results.append(status)
        err = status.error or ""
        print(f"{status.name:<45} {status.status:<12} {err[:40]}")

    ok = sum(1 for r in results if r.status == "OK")
    total = len(results)
    print(f"\n{ok}/{total} servers available")

    return 0 if ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
