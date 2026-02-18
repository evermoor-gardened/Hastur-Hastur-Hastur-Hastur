# Security Model

## Sovereignty Guarantees

RuinWare operates under a zero-trust-outbound model. The system makes no network calls except the optional, user-initiated Cogitator bridge to a local Ollama instance.

### What RuinWare Does NOT Do

- **No telemetry.** Zero usage data, crash reports, or analytics leave your machine.
- **No cloud dependencies.** Core functionality (Kernel, Cenobite, GUI) requires zero network access.
- **No authentication tokens.** No API keys stored, transmitted, or required for operation.
- **No persistent storage.** Session state lives in memory only. Nothing written to disk beyond what the user explicitly creates.
- **No auto-update.** The software never phones home. You update manually, on your terms.

### Ollama Bridge (Cogitator)

The only network call the system makes is a POST to `localhost:11434` when the user sends free-text input. This connection:

- Goes to `localhost` only (configurable but defaults local)
- Sends the user's prompt and a fixed system prompt
- Receives model output
- Uses no authentication (Ollama's default)
- Fails gracefully if unavailable — all other subsystems remain operational

If you never send free-text (only use Cenobite commands and `/status`), the system makes zero network calls.

### Threat Model

| Threat | Mitigation |
|--------|-----------|
| Data exfiltration | No outbound connections except user-initiated local Ollama |
| Dependency supply chain | Minimal deps: `requests` (optional), `tkinter` (stdlib) |
| State persistence attacks | All state in-memory, no disk writes |
| Prompt injection via Cogitator | System prompt is hardcoded, not user-modifiable at runtime |
| GUI input injection | tkinter Entry widget sanitizes by default |

### Hardening Recommendations

For maximum sovereignty:

1. Run with network disabled (`--net=none` in Docker, or firewall rules)
2. Use a local Ollama instance on an air-gapped machine
3. Audit the single-file source before execution
4. Run under a non-privileged user account

## Vulnerability Reporting

If you find a security issue, disclose responsibly. Open an issue or contact the maintainer. Do not weaponize vulnerabilities against users of this software — that violates the license.
