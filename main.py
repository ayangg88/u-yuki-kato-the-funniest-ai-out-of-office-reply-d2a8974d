"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes a single funny out-of-office auto-reply to /output/entry.txt.
"""

LINE = "Out of office: I left a smaller model in charge. It has already replied to everyone, incorrectly, with great confidence."


def main() -> None:
    import os

    # The gate only accepts 1 to 160 characters; fail loudly, never silently
    # ship an over-long line.
    assert 1 <= len(LINE) <= 160, f"entry is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
