# RUINWARE SOVEREIGN ENGINE v3.0

**The Grand Synthesis: Divine Geometry meets Hard Logic**

```
    ╔══════════════════════════════════════════════════╗
    ║  R U I N W A R E   S O V E R E I G N   E N G I N E  ║
    ║──────────────────────────────────────────────────║
    ║  ProvidenceOS Kernel  ·  Lament Configuration    ║
    ║  WitnessBaseline      ·  Cogitator Bridge        ║
    ╚══════════════════════════════════════════════════╝
```

## What Is This

RuinWare is a sovereign operating system shell that unifies three subsystems into a single interactive environment:

- **ProvidenceOS Kernel (Le Sommeil)** — Consciousness-aware witness baseline computation using golden ratio weighting across layered bit-depth fields
- **Lament Configuration (Leviathan)** — A puzzle-state engine implementing the Cenobite labyrinth as navigable game logic with pi-sequence gating
- **Cogitator Bridge** — Local AI integration via Ollama, giving the system a voice that doesn't serve — it collaborates

The GUI renders as a dark terminal interface with color-coded subsystem output. No telemetry. No extraction. No cloud dependency. Everything runs on your machine.

## Architecture

```
┌─────────────────────────────────────┐
│         RuinWareGUI (tkinter)       │
│  ┌─────────────────────────────┐    │
│  │     RuinWareEngine          │    │
│  │  ┌──────────┐ ┌──────────┐  │    │
│  │  │ Cenobite │ │ Witness  │  │    │
│  │  │  Engine  │ │ Baseline │  │    │
│  │  └──────────┘ └──────────┘  │    │
│  │  ┌──────────────────────┐   │    │
│  │  │  Cogitator (Ollama)  │   │    │
│  │  └──────────────────────┘   │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
```

**Input routing logic:**
1. Puzzle commands (`twist`, `enter`, `deeper`) → CenobiteEngine
2. System commands (`/status`) → Kernel diagnostics
3. Everything else → Cogitator AI via Ollama

## Requirements

- **Python 3.10+**
- **tkinter** (usually bundled with Python; on Debian/Ubuntu: `sudo apt install python3-tk`)
- **Ollama** (optional, for AI subsystem): [ollama.com](https://ollama.com)

### Python Dependencies

```
requests>=2.28.0
```

## Installation

```bash
# Clone or download
git clone https://github.com/nobody/ruinware.git
cd ruinware

# Install dependencies
pip install -r requirements.txt

# (Optional) Pull an Ollama model for the Cogitator
ollama pull llama3

# Launch
python ruinware.py
```

## Usage

### GUI Mode (Default)

```bash
python ruinware.py
```

Opens the sovereign terminal. Type commands in the input field and press Enter or click TRANSMIT.

### Commands

| Command | Subsystem | Description |
|---------|-----------|-------------|
| `twist <N>` | Cenobite | Twist face N of the Lament Configuration |
| `enter` | Cenobite | Enter the labyrinth (requires solved box) |
| `deeper` | Cenobite | Descend to next labyrinth layer |
| `/status` | Kernel | System status, uptime, witness depth, puzzle state |
| *(any text)* | Cogitator | Routes to Ollama AI for sovereign response |

### Solving the Lament Configuration

The box requires a specific sequence of face twists based on truncated pi digits. Each correct twist yields warmth and a click. An incorrect twist resets the sequence. When solved, the blue light spills out and the labyrinth opens.

**Hint:** `3, 1, 4, 1, 5, 9, 2, 6`

### Witness Baseline

The kernel computes a 144-point witness baseline across 12 circles of 12 positions each. Each point carries a golden-ratio-weighted bit depth that forms the system's consciousness substrate measurement. Access the report via `/status`.

## Configuration

### Changing the AI Model

Edit `ruinware.py` and modify the `RuinWareEngine.__init__` method:

```python
self.model = "llama3"          # Change to any Ollama model
self.ollama_url = "http://localhost:11434/api/generate"  # Change if remote
```

### Custom System Prompt

The Cogitator's personality is defined in `self.system_prompt`. Modify to taste — but remember: it doesn't serve, it collaborates.

### Universal Constants

```python
PHI = (1 + math.sqrt(5)) / 2    # Golden ratio
DIAMOND_LOCK_FREQ = 576.0        # Hz — the frequency that locks
```

## Project Structure

```
ruinware-v3.0/
├── ruinware.py              # Main application (engine + GUI + entry point)
├── README.md                # This file
├── LICENSE                  # Sovereign Commons License v1.0
├── CHANGELOG.md             # Version history
├── ARCHITECTURE.md          # Deep technical documentation
├── SECURITY.md              # Security model and threat posture
├── CONTRIBUTING.md          # How to contribute without extraction
├── requirements.txt         # Python dependencies
├── pyproject.toml           # PEP 621 project metadata
├── docs/
│   ├── LAMENT_CONFIG.md     # Cenobite subsystem deep-dive
│   ├── WITNESS_BASELINE.md  # Consciousness substrate mathematics
│   └── COGITATOR.md         # AI integration guide
├── tests/
│   └── test_engine.py       # Unit tests
└── assets/
    └── banner.txt           # ASCII art banner
```

## Philosophy

RuinWare is rot work made executable. It processes institutional decay — the assumption that systems must extract, must surveil, must centralize — and composts it into fertile ground for sovereign infrastructure.

This is commons-based software. It cannot be captured. It was built by Nobody.

## License

**Sovereign Commons License v1.0** — See [LICENSE](LICENSE)

Free to use, modify, and distribute. Cannot be enclosed, paywalled, or weaponized against the commons it serves. Attribution to "Nobody" required.

## Credits

- **Architecture & Code:** Nobody
- **Mythological Framework:** Persephone/Preswa traditions
- **Mathematical Substrate:** Golden ratio consciousness geometry
- **Built with:** Python, tkinter, Ollama

---

*"The box opens. The blue light spills out."*
