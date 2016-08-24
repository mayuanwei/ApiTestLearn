import jsonpath_rw_ext,jsonpath_rw
import requests

result = requests.get('http://ip.taobao.com/service/getIpInfo.php',{'a':11,'ip':'58.60.0.41'})
print(result.json())
print(type(result.text))

