FROM python:slim-bookworm

RUN apt update -y --fix-missing && apt install -y \
    git \
    traceroute \
    mtr \
    curl \
    net-tools \
    gcc \
    iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/xosadmin/axlg.git /opt/axlg

COPY init.sh /

RUN chmod a+x /init.sh

WORKDIR /opt/axlg

RUN pip3 install -r requirements.txt --break-system-packages

EXPOSE 5000

CMD ["/init.sh"]