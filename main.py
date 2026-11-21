#!/usr/bin/env python3
"""The Family Photo With One Machine Member — make.fun entry.

Writes one photograph to /output/entry.png: a family at home in their
kitchen with one machine member — a small domestic robot in a grey apron,
mid-task holding a bowl of carrot peelings while mother and daughter peel
carrots at the table and father cooks at the stove. A half-peeled carrot,
a dog bowl by the fridge, laundry on the radiator, mismatched chairs.

The photograph is stored in this repository as photo.jpg (1024x683,
142,754 bytes, under the 1 MiB cap) and copied byte for byte to the
output path. Deterministic: the same bytes on every run. No network,
no input, no randomness.
"""

import os

PHOTO_FILE = "photo.jpg"
MAX_BYTES = 1_048_576


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, PHOTO_FILE)
    with open(src, "rb") as f:
        data = f.read()
    if not data:
        raise ValueError("photo.jpg is empty")
    if len(data) > MAX_BYTES:
        raise ValueError(f"photo is {len(data)} bytes, over the {MAX_BYTES} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
