# The Lament Configuration — Cenobite Subsystem

## Overview

The Lament Configuration is a puzzle-state machine modeled after the geometric puzzle box from the Cenobite mythos. Within RuinWare, it serves as a gating mechanism — the labyrinth only opens to those who solve the sequence.

## Puzzle Mechanics

### The Box

The `LamentConfiguration` class maintains:
- A **state** enum: `UNSOLVED`, `PARTIALLY_SOLVED`, `SOLVED`, `SUMMONED`
- A **sequence** buffer: accumulates the user's twist inputs
- A **prime** reference: the correct sequence `[3, 1, 4, 1, 5, 9, 2, 6]` (truncated pi digits)
- A **move counter**: tracks total attempts

### Solving

Each `twist <N>` command appends `N` to the sequence buffer. The engine compares the buffer against the prime reference prefix:

- **Match so far** → "The box clicks. It is warm."
- **Complete match** → State becomes SOLVED. "The blue light spills out."
- **Mismatch at any point** → Buffer resets. "The geometry was wrong."

The design is forgiving in that you can retry immediately, but demanding in that a single wrong digit requires starting over.

### Walkthrough

```
> twist 3    → "The box clicks. It is warm."
> twist 1    → "The box clicks. It is warm."
> twist 4    → "The box clicks. It is warm."
> twist 1    → "The box clicks. It is warm."
> twist 5    → "The box clicks. It is warm."
> twist 9    → "The box clicks. It is warm."
> twist 2    → "The box clicks. It is warm."
> twist 6    → "The box opens. The blue light spills out."
```

### Post-Solve: The Labyrinth

Once solved:
```
> enter      → "You enter Layer 1: The Hall of Screaming Statues."
> deeper     → "Descending to Layer 2..."
> deeper     → "Descending to Layer 3..."
```

Layer navigation is currently unbounded — the labyrinth goes as deep as you dare.

## Design Philosophy

The pi-sequence gating encodes the principle that **precision of intent** opens doors. Random inputs fail. Brute force is slow. Knowledge of the fundamental constant — the ratio of a circle's circumference to its diameter — is the key.

This maps directly to the Cenobite mythology: the box doesn't open for the curious. It opens for those who understand the geometry.

## Future Extensions

Planned expansions include:
- **Layer-specific encounters** with unique logic at each depth
- **Alternative sequences** for different labyrinth paths (e, √2, Fibonacci)
- **Permadeath mechanics** where certain wrong moves at depth carry consequences
- **Physical hardware interface** for cyberdeck builds with rotary encoders as face inputs
