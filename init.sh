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

if [[ ! -f "${TESTFILE_DIR}/10mb.test" ]]; then
  echo "Creating test files. This may takes a bit longer..."
  create_test_file 10 10mb.test
  create_test_file 100 100mb.test
  create_test_file 1000 1000mb.test
fi

cd "$DIR" || { echo "Error changing directory" >&2; exit 1; }

echo "Updating settings..."

if [[ -n "$siteTitle" ]]; then
  mv conf.py conf.py.backup 2>/dev/null

  lowerIperf=$(echo "$iperf3" | tr 'A-Z' 'a-z')
  lowerdiscouragesearch=$(echo "$discouragesearch" | tr 'A-Z' 'a-z')

  case "$lowerIperf" in
    true) iperf="Enabled" ;;
    *) iperf="Disabled" ;;
  esac

  case "$lowerdiscouragesearch" in
    true) discouragesearches=True ;;
    *) discouragesearches=False ;;
  esac

  if [[ -z "$location" ]]; then
    location="Unknown"
  fi

  cat > conf.py <<EOF
sysconfig = {
    "siteTitle": "${siteTitle}",
    "hostname": "${hostname}",
    "Location": "${location}",
    "pingtime": "${pingtime}",
    "iperf3": "${iperf}",
    "DiscourageSearchEngine": ${discouragesearches}
}
EOF
fi

git stash push -u -m "conf.py stash" || echo "Nothing to stash"
git pull || { echo "Git pull failed" >&2; exit 1; }
git stash pop || echo "Nothing to pop"

echo "Starting WSGI http server..."
uwsgi --http :5000 --wsgi-file app.py --callable app || { echo "Error starting uwsgi" >&2; exit 1; }