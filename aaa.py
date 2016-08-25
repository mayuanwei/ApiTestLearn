import jsonpath_rw_ext,jsonpath_rw
import requests
import json

#a = {'ip':'61.183.144.26'}
#ip = json.loads(a)
result = requests.get('http://ip.taobao.com/service/getIpInfo.php?',{'ip':'61.183.144.26'})


print(type(result.json()))
print(result.json())
print(json.dumps(json.loads(result.text)))
print(json.loads(result.text))
print(type(result.text))
print(result.text)

