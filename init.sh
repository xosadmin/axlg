#!/bin/bash
cd /opt/axlg
if [ ! -d testfile ]; then
  mkdir -p testfile
  cd testfile
  dd if=/dev/zero of=10mb.test bs=1M count=10
  dd if=/dev/zero of=100mb.test bs=1M count=100
  dd if=/dev/zero of=1000mb.test bs=1M count=1000
else
  if [[ ! -f testfile/10mb.test ] || [ ! -f testfile/100mb.test ] || [ ! -f testfile/1000mb.test ]]; then
    cd testfile
    dd if=/dev/zero of=10mb.test bs=1M count=10
    dd if=/dev/zero of=100mb.test bs=1M count=100
    dd if=/dev/zero of=1000mb.test bs=1M count=1000
  fi
fi
cd /opt/axlg
uwsgi --http :5000 --wsgi-file app.py --callable app