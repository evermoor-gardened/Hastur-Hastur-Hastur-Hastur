# Contributing to RuinWare

## The Ground Rules

This is commons-based infrastructure. Contributions are welcome under the Sovereign Commons License. If you contribute, your work enters the commons alongside everything else here. It cannot be recaptured.

## How to Contribute

### Bug Reports
Open an issue with: what you did, what happened, what you expected. Include your Python version and OS.

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-thing`)
3. Make your changes in `ruinware.py` or add new modules
4. Write tests in `tests/` if adding functionality
5. Ensure `python -m pytest tests/` passes
6. Submit a pull request

### What We're Looking For

- **New subsystem modules** — Additional engines that plug into the routing chain
- **Puzzle expansions** — New labyrinth layers, alternative puzzle sequences
- **Witness model enhancements** — Alternative weighting functions, higher-dimensional baselines
- **Hardware integration** — Cyberdeck builds, physical Lament Configuration interfaces
- **Documentation** — Clearer explanations, translations, tutorials
- **Accessibility** — Screen reader support, alternative input methods

### What We Won't Accept

- Telemetry, analytics, or tracking of any kind
- External service dependencies for core functionality
- Anything that violates the Sovereign Commons License
- Code that phones home, calls external APIs without explicit user action, or stores data without consent

## Code Style

- Python 3.10+ type hints where practical
- Docstrings on public methods
- No external dependencies for core engine logic
- Graceful degradation when optional deps are missing
- Comments should explain *why*, not *what*

## Architecture Decisions

Major architecture changes should be discussed in an issue first. The three-subsystem design (Kernel, Cenobite, Cogitator) is intentional and should be preserved. New subsystems are additive, not replacements.

## Recognition

Contributors are credited in CHANGELOG.md entries for the releases that include their work. Attribution follows the "Nobody" tradition — you may use your name or a chosen identity.
