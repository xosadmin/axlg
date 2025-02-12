#!/bin/bash
DIR="/opt/axlg"
TESTFILE_DIR="$DIR/static/testfile"
if [ ! -d "$TESTFILE_DIR" ]; then
  mkdir -p "$TESTFILE_DIR" || { echo "Error creating directory" >&2; exit 1; }
fi

create_test_file() {
  local size="$1"
  local filename="$2"
  local filepath="$TESTFILE_DIR/$filename"

  if [ ! -f "$filepath" ]; then
    dd if=/dev/zero of="$filepath" bs=1M count="$size" || { echo "Error creating file $filename" >&2; exit 1; }
  fi
}

create_test_file 10 10mb.test
create_test_file 100 100mb.test
create_test_file 1000 1000mb.test


cd "$DIR" || { echo "Error changing directory" >&2; exit 1; }

git pull

uwsgi --http :5000 --wsgi-file app.py --callable app || { echo "Error starting uwsgi" >&2; exit 1; }