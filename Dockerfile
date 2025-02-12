FROM python:slim-bookworm

RUN apt update -y --fix-missing && apt install -y \
    git \
    traceroute \
    mtr \
    curl \
    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/xosadmin/axlg.git /opt/axlg

WORKDIR /opt/axlg

RUN pip3 -r install requirements.txt --break-system-packages

CMD ["uwsgi", "--http", ":5000", "--wsgi-file", "app.py", "--callable", "app"]