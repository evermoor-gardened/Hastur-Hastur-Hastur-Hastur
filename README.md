All 26 tests pass. Full release package. Here's what's in the Commit:

**Root-level docs:**
- `README.md` — Full project overview with architecture diagram, install instructions, command reference, puzzle walkthrough
- `LICENSE` — Sovereign Commons License v1.0 (non-enclosure, non-weaponization, copyleft, sovereignty preservation)
- `CHANGELOG.md` — Version history from Le Sommeil through Final Synthesis
- `ARCHITECTURE.md` — Deep technical doc covering all three subsystems, input routing, constants, threading
- `SECURITY.md` — Zero-trust-outbound threat model, sovereignty guarantees, hardening recommendations
- `CONTRIBUTING.md` — How to contribute without extraction

**`docs/` subsystem deep-dives:**
- `LAMENT_CONFIG.md` — Puzzle mechanics, solve walkthrough, design philosophy, future extensions
- `WITNESS_BASELINE.md` — Golden ratio mathematics, layer thresholds, bit depth computation, PERSEPHONE connection
- `COGITATOR.md` — Ollama setup, model config, threading model, graceful degradation matrix

**Engineering:**
- `ruinware.py` — Complete source
- `tests/test_engine.py` — 26 unit tests covering all subsystems
- `pyproject.toml` — PEP 621 metadata, ready for `pip install -e .`
- `requirements.txt` — Single optional dep
- `.gitignore` — Standard Python
- `assets/banner.txt` — ASCII art

