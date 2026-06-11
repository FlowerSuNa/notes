#!/usr/bin/env python3
"""
처리 완료된 inbox 파일을 archive/ 로 이동.

Usage: python scripts/archive_file.py <filename>
"""
import sys
import shutil
from pathlib import Path

NOTES_DIR = Path(__file__).parent.parent
INBOX_DIR = NOTES_DIR / "inbox"
ARCHIVE_DIR = INBOX_DIR / "archive"


def main():
    if len(sys.argv) < 2:
        print("Usage: python archive_file.py <filename>")
        sys.exit(1)

    src = INBOX_DIR / sys.argv[1]
    if not src.exists():
        print(f"Not found: {src}")
        sys.exit(1)

    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    dst = ARCHIVE_DIR / src.name

    # 동명 파일이 있으면 타임스탬프 suffix 추가
    if dst.exists():
        from datetime import datetime
        stamp = datetime.now().strftime("%H%M%S")
        dst = ARCHIVE_DIR / f"{src.stem}_{stamp}{src.suffix}"

    shutil.move(str(src), str(dst))
    print(f"Archived: {src.name} → archive/{dst.name}")


if __name__ == "__main__":
    main()
