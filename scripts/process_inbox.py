#!/usr/bin/env python3
"""
Inbox scanner — Claude가 /정리 명령 실행 시 호출.
inbox/ 의 미처리 파일을 읽어 JSON으로 출력한다.

Usage: python scripts/process_inbox.py [--all]
  기본: inbox/ 의 .md/.txt 파일만 (archive/ 제외)
  --all: archive/ 포함
"""
import json
import sys
from pathlib import Path
from datetime import datetime

NOTES_DIR = Path(__file__).parent.parent
INBOX_DIR = NOTES_DIR / "inbox"
ARCHIVE_DIR = INBOX_DIR / "archive"
PROCESSED_DIR = NOTES_DIR / "processed"


def scan_files(include_archive: bool = False) -> list[Path]:
    targets = []
    for f in INBOX_DIR.iterdir():
        if f.is_file() and f.suffix in (".md", ".txt") and f.name != "README.md":
            targets.append(f)
    if include_archive:
        for f in ARCHIVE_DIR.iterdir():
            if f.is_file() and f.suffix in (".md", ".txt"):
                targets.append(f)
    return sorted(targets, key=lambda p: p.stat().st_mtime)


def read_text(path: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp949", "euc-kr"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def file_info(path: Path) -> dict:
    mtime = datetime.fromtimestamp(path.stat().st_mtime)
    content = read_text(path)
    return {
        "filename": path.name,
        "path": str(path),
        "modified": mtime.strftime("%Y-%m-%d %H:%M"),
        "date": mtime.strftime("%Y-%m-%d"),
        "size_chars": len(content),
        "content": content,
    }


def main():
    include_archive = "--all" in sys.argv
    files = scan_files(include_archive)

    if not files:
        print(json.dumps({"status": "empty", "count": 0, "files": []}, ensure_ascii=False))
        return

    result = {
        "status": "ready",
        "count": len(files),
        "processed_dir": str(PROCESSED_DIR),
        "archive_dir": str(ARCHIVE_DIR),
        "files": [file_info(f) for f in files],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
