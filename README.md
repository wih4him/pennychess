# Pennychess

A browser-playable chess-variant puzzle engine. Pieces never capture: they move, swap, or stack, and every move can set off physics-like **reactions** (pushes and pulls) that cascade step by step until the board settles. Each level is a puzzle with a minimum move count.

The current version is **Fork 1.3** (`index.html`). Earlier versions are kept unchanged in `versions/`.

## How to run

- **In a browser:** open `index.html`. It is a single self-contained file with nothing to install.
- **As a desktop window:** `pip install pywebview`, then `python app.py`.

## Rules summary

- **Goal:** get the two pennies (the kings) onto the same square. Your score is the number of moves you take, measured against the level's minimum ("Perfect Solve!" if you match it, "NEW RECORD!" if you beat it).
- **No captures.** Pieces use standard chess movement, and a pawn may advance two squares on its first move.
- **Forces:** Rooks, Bishops and Queens push or pull opposite-color pieces along their lines, and pawns push diagonally. A ray stops at the first piece it meets.
- **Pawn shields:** pawns can shield a penny.
- **Knights:**
  - **Knortal:** a force that enters one knight comes out of another knight, with its direction conserved.
  - **Kuantum-tunneling:** a piece that moves or is pushed onto a knight's square swaps places with it.
  - **Kneleportation:** a knight that moves onto an occupied square swaps places with that piece.
- **Reactions:** before each step is applied, every movement in it is shown with an arrow, and you click **Apply Step**. When several forces compete, you choose which one wins (a *Decision*). Forces that loop and cancel out resolve as "Net Force Zero."
- The full rule set and an FAQ are built into the app.

## Fork 1.3 features

- **Free Play:** standard chess for two players sharing one mouse. It has captures, castling, en passant, promotion, and checkmate/stalemate detection.
- **Cheat Mode:** arrange pieces freely.
- **Positions and games:** copy/load a position as FEN (Pennychess shields are added as a suffix), and save/load a whole game as a `.md` file.
- **History:** click any logged step to rewind the board to that point.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 William Isaiah Hardwick.
