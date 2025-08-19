import os,subprocess
from flask import *
from utils import *
from conf import sysconfig

app = Flask(__name__)

siteTitle = sysconfig["siteTitle"]

def getIP():
    ipaddr = request.headers.get("CF-Connecting-IP")
    if not ipaddr:
        ipaddrReturn = request.remote_addr
    if "," in ipaddrReturn:
        ipaddrReturn = ipaddrReturn.split(",")[0]
    return ipaddrReturn

@app.route("/")
def homepage():
    srvip4, srvip6 = readIP64()
    userIP = getIP()
    asnisp = ip2asn(userIP)
    srvipv4ISP = ip2asn(srvip4)
    srvipv6ISP = ip2asn(srvip6)
    hostname = sysconfig["hostname"]
    location = sysconfig["Location"]
    iperf3 = sysconfig["iperf3"]
    return render_template("index.html",
                           siteTitle=siteTitle,
                           hostname=hostname,
                           userIP=userIP,
                           asnisp=asnisp,
                           srvipv4=srvip4,
                           srvipv6=srvip6,
                           iperf3=iperf3,
                           srvipv4ISP=srvipv4ISP,
                           srvipv6ISP=srvipv6ISP,
                           location=location)

@app.route("/process/<type>/<value>",methods=["GET"])
def process(type,value):
    result = ""
    if type == "ping":
        if validIP(value):
            result = ping(value,sysconfig["pingtime"])
        else:
            result = "Invalid IP Address"
    elif type == "traceroute":
        if validIP(value):
            result = tracert(value)
        else:
            result = "Invalid IP Address"
    elif type == "mtr":
        if validIP(value):
            result = mtr(value)
        else:
            result = "Invalid IP Address"
    elif type == "bgproute":
        if validIP(value):
            result = tracert(value)
        else:
            result = "Invalid IP Address"
    else:
        result = "Invalid Action."
    return f"<pre>{result}</pre>"

@app.route("/robots.txt")
def robots():
    searchEngine = sysconfig["DiscourageSearchEngine"]
    if searchEngine:
        content = "User-agent: *\nDisallow: /"
    else:
        content = "User-agent: *"
    return Response(content, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
