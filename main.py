"""make.fun entry: news-image-20261125.

This script is the code part of the make.fun news-image bounty entry
for 25 November 2026. It takes the cover image ``entry.png`` that sits
next to this file and writes an identical copy to the output location
expected by make.fun (``/output/entry.png`` by default, or the path in
the ``MAKEFUN_OUTPUT`` environment variable when set).

The program performs no network access and no image processing: it
copies the PNG bytes exactly, so every run produces the same output.
After copying, it checks that the SHA-256 digest of the copy matches
the digest of the source file and fails with a clear error if the two
differ.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    """Copy entry.png to the make.fun output path and verify it."""
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        print(
            f"error: source image not found: {source}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    output = Path(os.environ.get("MAKEFUN_OUTPUT") or "/output/entry.png")
    if output.parent != Path("."):
        output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output)
    source_hash = sha256_of(source)
    output_hash = sha256_of(output)
    if output_hash != source_hash:
        print(
            f"error: SHA-256 mismatch after copying entry.png: "
            f"source {source_hash} != output {output_hash}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    print(f"wrote {output} (sha256 {output_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
