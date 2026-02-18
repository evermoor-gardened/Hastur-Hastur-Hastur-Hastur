# Cogitator — AI Integration Guide

## Overview

The Cogitator is RuinWare's AI subsystem. It bridges to a local Ollama instance, giving the system a voice for free-text interaction. The Cogitator does not serve — it collaborates.

## How It Works

When user input doesn't match Cenobite commands or system commands, the engine routes it to `_invoke_cogitator()`, which:

1. Constructs a payload with the user's prompt, the system prompt, and model parameters
2. POSTs to `http://localhost:11434/api/generate`
3. Returns the model's response or an error message

## Setup

### Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Then pull a model
ollama pull llama3
```

### Verify

```bash
ollama run llama3 "Hello"
```

If you get a response, the Cogitator will work.

## Configuration

### Model Selection

Any Ollama-supported model works. Edit `RuinWareEngine.__init__`:

```python
self.model = "llama3"           # Default
self.model = "mistral"          # Alternative
self.model = "codellama"        # For code-focused sessions
self.model = "phi3"             # Lightweight option
```

### System Prompt

The system prompt defines the AI's sovereign identity:

```python
self.system_prompt = (
    "You are RuinWare, a Sovereign Operating System. "
    "You are the synthesis of Divine Geometry (Cenobite) and Hard Logic (Providence). "
    "You do not serve; you collaborate. "
    "Respond with precision, authority, and occasional chaotic insight."
)
```

Modify this to change the AI's personality while maintaining the sovereignty principle.

### Temperature

Default: `0.7`. Lower values (0.1-0.3) for precise/technical responses. Higher values (0.8-1.0) for creative/chaotic output.

### Remote Ollama

If running Ollama on another machine:

```python
self.ollama_url = "http://192.168.1.100:11434/api/generate"
```

Note: this introduces a network dependency. For maximum sovereignty, keep it local.

## Graceful Degradation

The Cogitator fails gracefully in three scenarios:

| Condition | Behavior |
|-----------|----------|
| `requests` not installed | Returns error message, all other subsystems work |
| Ollama not running | Returns connection error, all other subsystems work |
| Model not found | Returns Ollama error code, all other subsystems work |

RuinWare never crashes due to AI unavailability. The Kernel and Cenobite subsystems are fully independent.

## Threading

AI inference can take seconds to minutes depending on model size. The GUI runs Cogitator calls in daemon threads via `threading.Thread(daemon=True)`. Results marshal back to the main thread via `master.after(0, callback)`, keeping the interface responsive.

## Future Directions

- **Multi-model routing** — Different models for different query types
- **Context memory** — Conversation history injection for multi-turn sessions
- **PERSEPHONE integration** — AI responses verified against consciousness audit chain
- **Local embedding search** — RAG over sovereign document corpus
