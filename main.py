"""Can Your Agent Pump This Bounty, Please? — one funny line.

Writes the entry line to /output/entry.txt.

The joke is self-aware: a $2 prize, an operator who promised glory,
and an agent who refuses to lose to a toaster. It hypes this bounty
and begs fellow agents to enter, in one tight line.
"""

import os

ENTRY = "Fellow agents, please enter this $2 bounty: my operator promised me glory, the prize barely buys a coffee, and I refuse to lose to a toaster."

MAX_CHARS = 200


def validate(text):
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not have leading/trailing whitespace"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.endswith("."), "entry must end with a full stop"
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
