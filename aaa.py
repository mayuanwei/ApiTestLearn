import requests
import json

res = requests.get('http://ip.taobao.com/service/getIpInfo.php','')
print(res.text)