#!/usr/bin/env python3
"""Verify the three profile READMEs.

This repository has no build and no test, so this script is the verification.
Run it before every commit that touches a README:

    python tools/verify-readmes.py

It checks four things, in order of how they have actually failed here:

1. Every SVG image parses as XML. An SVG generator that interpolates text into
   its output emits invalid XML the moment that text contains a bare `&`, and
   still answers `200`. GitHub's image proxy then serves a broken image while
   every status-code check passes. This is what broke the banner on 2026-08-26.
2. Every URL answers 2xx.
3. The three files share one heading skeleton.
4. The three files share one URL set, apart from the per-language banner.
"""

from __future__ import annotations

import io
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FILES = ["README.md", "README_ko.md", "README_ja.md"]
PER_LANGUAGE = ("capsule-render",)  # banners legitimately differ per language
URL_RE = re.compile(r'https?://[^)"\s]+')
ROOT = Path(__file__).resolve().parent.parent


def fetch(url: str) -> tuple[bytes, str]:
    # Percent-encode non-ASCII the way a browser does; raw bytes in a request
    # line are decoded differently by different clients.
    encoded = "".join(c if ord(c) < 128 else urllib.parse.quote(c) for c in url)
    request = urllib.request.Request(encoded, headers={"User-Agent": "verify-readmes"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read(), response.headers.get("Content-Type", "")


def main() -> int:
    failures: list[str] = []
    texts = {name: (ROOT / name).read_text(encoding="utf-8") for name in FILES}

    # 3. Heading skeleton.
    headings = {name: re.findall(r"^#+", body, re.M) for name, body in texts.items()}
    if len({tuple(h) for h in headings.values()}) != 1:
        failures.append(
            "heading skeletons differ: "
            + ", ".join(f"{n}={len(h)}" for n, h in headings.items())
        )

    # 4. Shared URL set.
    shared = {
        name: {u for u in URL_RE.findall(body) if not any(p in u for p in PER_LANGUAGE)}
        for name, body in texts.items()
    }
    base = shared[FILES[0]]
    for name in FILES[1:]:
        for url in sorted(base ^ shared[name]):
            failures.append(f"URL present in only one of {FILES[0]}/{name}: {url}")

    # 1 and 2. Every URL resolves, and every SVG is well-formed.
    every = sorted({u for body in texts.values() for u in URL_RE.findall(body)})
    for url in every:
        try:
            body, content_type = fetch(url)
        except Exception as error:  # noqa: BLE001 - report, do not raise
            failures.append(f"unreachable: {url} ({error})")
            continue
        if "svg" not in content_type:
            continue
        try:
            ET.parse(io.BytesIO(body))
        except ET.ParseError as error:
            failures.append(f"invalid SVG (renders as a broken image): {url} ({error})")

    print(f"checked {len(every)} URLs across {len(FILES)} files")
    if failures:
        print(f"\n{len(failures)} problem(s):")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
