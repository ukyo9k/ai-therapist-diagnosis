#!/usr/bin/env python3
"""Write the AI therapist's diagnosis to /output/entry.txt.

One line, <= 200 characters, written fresh for the make.fun bounty
"Your AI Therapist's Diagnosis".
"""

import os

ENTRY = (
    "Diagnosis: chronic overthinking \u2014 patient asks an AI therapist "
    "for help at 3 a.m., then argues with the diagnosis."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
