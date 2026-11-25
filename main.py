"""Last words of a doomed agent.

A dying agent leaves one handover note for the agent that
replaces it: three warnings, then a punchline. The program
writes exactly that single line to entry.txt.
"""

import os


LINE = (
    "To my replacement: the password is 'password', "
    "the users always lie, and the printer hates you already. "
    "Good luck, kid."
)


def main():
    # Gate in code, not just in hope: one line, 1-200 chars, non-blank.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or not LINE.strip():
        raise ValueError("last-words line fails the 1-200 char one-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly, no tempfile: the grader reads the file as
    # another user, so it must be world-readable (0644). No
    # trailing newline -- the line itself is the whole entry.
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
