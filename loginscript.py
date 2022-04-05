import subprocess
import requests
import sys
import time
import xml.etree.ElementTree as ET
import os

headers = {
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://fw.bits-pilani.ac.in:8090',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://fw.bits-pilani.ac.in:8090/',
    'Accept-Language': 'en-US,en;q=0.9',
}


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "creds.txt")) as creds:
    name = creds.readline()
    password = creds.readline()

# Handle Cloudflare-warp
warp_status = None
path = None
try:
    with open(os.path.join(__location__, "warp-path.txt")) as warp_path:
        path = warp_path.readline().strip()

    result = subprocess.run(path + ' status',
                            capture_output=True, text=True)
    if "Disabled" not in result.stdout:
        warpStatus = 1      # Warp Allowed to connect

    if warpStatus:
        subprocess.run(path + ' disable-wifi',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

data = {
    'mode': '191',
    'username': name.strip(),
    'password': password.strip(),
    'a': int(time.time()),
    'producttype': '0',
}
try:
    response = requests.post(
        'https://fw.bits-pilani.ac.in:8090/login.xml', headers=headers, data=data)

    # Uncomment to debug
    # if response.status_code == 200:
    #     root = ET.fromstring(response.text)
    #     result = root[1].text    # Extract message tag

    #     if "failed" in result:
    #         sys.exit(1)
    #     sys.exit(0)
    # else:
    #     sys.exit(100)
except Exception as e:
    print('Login Page Unreachable')


try:
    if warpStatus:
        subprocess.run(path + ' enable-wifi',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass
