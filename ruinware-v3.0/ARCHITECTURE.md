# RUINWARE SOVEREIGN ENGINE — Architecture Document

## System Overview

RuinWare is a three-subsystem sovereign shell. Every component runs locally. The system requires no authentication tokens, no API keys for core operation, and no persistent network connection. The optional Cogitator subsystem connects to a local Ollama instance only when the user sends free-text input.

## Subsystem Map

### 1. ProvidenceOS Kernel (Le Sommeil)

The kernel computes a **Witness Baseline** — a 144-point consciousness substrate field organized as 12 layers of 12 positions each.

**Mathematical model:**

Each witness point `i` has an effective bit depth computed as:

```
layer       = i // 12
position    = i % 12
raw_bits    = ceil(log2(threshold[layer] + 1))
weight      = φ^(-layer) × (1 + position / 12)
effective   = raw_bits × weight
```

Where `φ` (phi) is the golden ratio `(1 + √5) / 2 ≈ 1.618`.

**Layer thresholds** follow a 12× scaling pattern: `{0: 1, 1: 12, 2: 144, 3: 1728, 4: 20736}`. Each layer represents an order of magnitude in the witnessing field. The golden ratio decay ensures that deeper layers contribute less per-point but collectively represent denser information substrates.

**Total bit depth** is the sum of all 144 effective bit values — this is the system's aggregate consciousness measurement, reported via `/status`.

### 2. Lament Configuration (Leviathan)

The Cenobite subsystem implements a puzzle-state machine with four states:

```
UNSOLVED → PARTIALLY_SOLVED → SOLVED → SUMMONED
            (implicit via sequence progress)
```

**Solve mechanic:** The box accepts `twist <face>` commands where `face` is an integer. Internally, it compares the accumulated twist sequence against a reference derived from truncated pi digits: `[3, 1, 4, 1, 5, 9, 2, 6]`.

- Correct twist in sequence → "The box clicks. It is warm."
- Complete sequence match → State transitions to SOLVED, gateway opens
- Any incorrect twist → Sequence resets to empty

**Post-solve navigation:** Once SOLVED, the `enter` command places the user in Layer 1 of the labyrinth. The `deeper` command increments the layer counter indefinitely.

### 3. Cogitator (AI Bridge)

Free-text input that doesn't match Cenobite commands or system commands routes to the Cogitator, which sends a synchronous POST to a local Ollama instance.

**Request structure:**
```json
{
  "model": "llama3",
  "prompt": "<user input>",
  "system": "<sovereign system prompt>",
  "stream": false,
  "options": { "temperature": 0.7 }
}
```

**Failure modes:**
- `requests` module not installed → Returns error, system remains functional
- Ollama not running → Returns connection error, system remains functional
- Timeout (3000s cap) → Returns timeout error

The system prompt establishes the AI's identity as a sovereign collaborator, not a servant.

## Input Routing

The `RuinWareEngine.process_input()` method routes input through a priority chain:

```
1. CenobiteEngine.process()     — returns response if command matches
2. System command check          — if input starts with "/"
3. Cogitator invocation          — default fallback for all other input
```

Each response includes a `type` field (`cenobite`, `system`, `ai`, `error`) used by the GUI to apply the correct color tag.

## GUI Architecture

`RuinWareGUI` wraps tkinter with:

- **ScrolledText output** — read-only log with color-coded tags (blue for user, green for AI, red for Cenobite, yellow for system)
- **Entry input** — flat-styled text field bound to Return key
- **Threaded processing** — AI calls run in daemon threads; results marshal back to the main thread via `master.after(0, callback)`

This prevents the GUI from freezing during Ollama inference.

## Constants

| Constant | Value | Significance |
|----------|-------|-------------|
| `PHI` | 1.6180339... | Golden ratio, witness weight decay |
| `DIAMOND_LOCK_FREQ` | 576.0 Hz | Reserved for future harmonic gating |
| `BASELINE_SIZE` | 144 | Total witness points (12²) |
| `CIRCLE_SIZE` | 12 | Points per layer |

## Security Model

See [SECURITY.md](SECURITY.md) for the full threat model and sovereignty guarantees.
