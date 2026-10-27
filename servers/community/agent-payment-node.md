# Agent Payment Node

Local payment runtime and stdio MCP tools from Nuanu AI, written in TypeScript and licensed under MIT.

**Source:** https://github.com/nuanu-ai/agent-payment-node

**Platform:** Apple Silicon macOS and Node 24 only. Linux, Windows and Intel Macs are unsupported.

## Installation

```bash
brew install nuanu-ai/tap/apn
```

## Configuration

After installation, generate the actual MCP launch descriptor:

```bash
apn mcp config
```

Use that output in your MCP client's configuration. The documented local stdio launch command is `apn mcp serve`. There is no hosted MCP endpoint or npm package to substitute for this Homebrew setup.

## Capabilities

- Inspect supported x402 offers.
- Prepare bounded payment operations under owner-configured policy.
- Query operation status and receipts, and use documented recovery paths.

## Payment authority and limits

Direct transfers and EVM x402 signing require foreground owner approval. Solana exact x402 can run under an owner-admitted policy. APN is spend-capable software; it is not a read-only server or a general sandbox.

Wallet setup and payment policy remain owner responsibilities. The upstream README documents disposable local-software custody and compromised-host limits. Do not place private keys, seed phrases or provider secrets in prompts or public client configurations.

The software is free. Network and provider fees are separate. This entry does not claim an independent security audit, live payment test or current client-specific interoperability retest.
