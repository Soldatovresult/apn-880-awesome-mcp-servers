# MCP Transport Options

MCP supports two transport mechanisms: stdio (local) and SSE (remote).

## stdio (Local)

Default for local development. Server runs as a subprocess, communicating via stdin/stdout.

**Pros:** Simple, secure, no network exposure  
**Cons:** Local only, one client per server

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

## SSE over HTTP (Remote)

Server runs as an HTTP endpoint, communicating via Server-Sent Events.

**Pros:** Remote access, multiple clients, scales horizontally  
**Cons:** Requires auth, network latency, more complex

```json
{
  "mcpServers": {
    "remote-server": {
      "url": "https://mcp.example.com/sse",
      "headers": {
        "Authorization": "Bearer <token>"
      }
    }
  }
}
```

## WebSocket

Alternative remote transport with bidirectional streaming.

**Pros:** Full-duplex, lower latency than SSE  
**Cons:** Requires WebSocket server, more complex setup

## Choosing

| Criterion | stdio | SSE | WebSocket |
|-----------|-------|-----|-----------|
| Local dev | ✅ | ❌ | ❌ |
| Remote | ❌ | ✅ | ✅ |
| Multi-client | ❌ | ✅ | ✅ |
| Simple setup | ✅ | ❌ | ❌ |
| Low latency | ✅ | ✅ | ✅ |
| Firewall-friendly | ✅ | ✅ | ❌ |
