import os,subprocess
import requests
import ipaddress

def runCommand(command):
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        return "\n".join(result.stdout.splitlines())
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    except FileNotFoundError:
        return "Error: Command not found"

def readIP64():
    endpoint = "https://showip.7m7.net"
    ipv4 = runCommand(['curl', '-4', endpoint, '--insecure']).strip()
    ipv6 = runCommand(['curl', '-6', endpoint, '--insecure']).strip()
    if "Couldn't connect to server" in ipv6:
        ipv6 = "Not available"
    return ipv4, ipv6

def validIP(ipaddr):
    try:
        ret = ipaddress.ip_address(ipaddr)
        return True
    except:
        return False

def validIPRange(ipaddr):
    if "/" in ipaddr:
        try:
            ipaddrSplit = ipaddr.split("/")
            if int(ipaddrSplit[1]) <= 48:
                return True
            else:
                return False
        except:
            return False
    else:
        return False

def ip2asn(ipaddr):
    url = f"https://ipinfo.io/{ipaddr}/json"
    if ipaddr != "127.0.0.1":
        response = requests.get(url)
        if response.status_code == 200:
            contents = response.json()
            isp = contents.get("org","Unknown")
            return str(isp)
        else:
            isp = "Cannot retrieve information."
    else:
        isp = "AS65530 Local Address"
    return str(isp)

def ping(dst,time):
    if 0 < int(time) <= 30:
        if ":" not in dst:
            command = ['ping', dst, '-c', time]
        else:
            command = ['ping6', dst, '-c', time]
        result = runCommand(command)
    else:
        result = ""
    return result

def tracert(dst):
    if ":" in dst:
        command = ['traceroute', '-6', dst]
    else:
        command = ['traceroute', dst]
    result = runCommand(command)
    return result

def mtr(dst):
    if ":" in dst:
        command = ['mtr', '--report', '--report-cycles=1', '-6' , dst]
    else:
        command = ['mtr', '--report', '--report-cycles=1', dst]
    result = runCommand(command)
    return result

def bgproute():
    pass
