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

COPY init.sh /

RUN chmod a+x /init.sh

WORKDIR /opt/axlg

RUN rm -rf .git

RUN pip3 -r install requirements.txt --break-system-packages

EXPOSE 5000

CMD ["/etc/start.sh"]