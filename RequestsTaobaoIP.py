import requests
import json
from Exception import TestCaseFailException

def taobao_ip(para):
    #get请求到url
    taobao_ip = requests.get('http://ip.taobao.com/service/getIpInfo.php',para)
    if taobao_ip.status_code==200: print('状态码：',taobao_ip.status_code,'返回成功')
    else:print('状态码：',taobao_ip.status_code,'返回失败')

    #获取response正文（即json）
    response = taobao_ip.text
    #print(taobao_ip.headers)
    #print(taobao_ip.content)

    #解析json到dict
    res_text = json.loads(response)

    res = res_text['data']
    res_data = {}
    try:
        if res_text['code'] == 1:
            #res_data = res
            raise TestCaseFailException
        else:
            res_data['国家'] = res['country']
            res_data['省'] = res['region']
            res_data['市'] = res['city']
            res_data['运营商']  = res['isp']
            assert res_data['国家'] == '中国'
            return res_data
    except TestCaseFailException:
        raise TestCaseFailException
    finally:
        taobao_ip.close()

if __name__ == '__main__':
    ip = ['59.172.37.74','59.172.37.741','','abc','地址']
    for i in ip:
        try:
            text = taobao_ip('ip='+i)
            print('IP:%s'%i,'Data:',text,'Result:Pass')
        except TestCaseFailException:
            print('IP:%s'%i,'Data:invaild ip','Result:Fail')
