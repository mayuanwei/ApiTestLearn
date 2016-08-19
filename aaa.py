import requests
import json
from Exception import TestCaseFailException

def res_ip(para):
    #get请求到url
    urlre = requests.get('http://ip.taobao.com/service/getIpInfo.php',para)
    if urlre.status_code==200: print('状态码：',urlre.status_code,'返回成功')
    else:print('状态码：',urlre.status_code,'返回失败')


    #获取response正文（即json）
    response = urlre.text
    #print(urlre.headers)
    #print(urlre.content)
    print(response)

    #解析json到dict
    res = json.loads(response)
    print(res)

    res_data = res['data']
    if res_data == 'invaild ip.':
        raise TestCaseFailException
    else:
        print(res_data)
        print('国家：', res_data['country'])
        print('省：', res_data['region'])
        print('市：', res_data['city'])
        print('运营商：', res_data['isp'])
        assert res_data['country'] == '中国'
        urlre.close()

if __name__ == '__main__':
    try:
        res_ip('ip=59.172.37.74')
        print('testcase pass')
    except TestCaseFailException:
        print('testcase fail')
