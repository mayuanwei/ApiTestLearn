

class ResultCount(object):
    def __init__(self,failcase,passcase):
        self.failcases = failcase
        self.passcases = passcase
        self.text = '总共运行%d用例' % (len(self.passcases) + len(self.failcases)) + '\n' + \
                    '失败:%d条'%len(self.failcases) + ' ' + '通过:%d条'%len(self.passcases) + '\n'

    def passcount(self):
        return len(self.passcases)

    def failcount(self):
        for failcase in self.failcases:
            self.text += '第%s条用例失败' % failcase[0]['No.'] + ' ' + '结果是:' + str(failcase[1]) + '\n'
        return len(self.failcases),self.text

    def count(self):
        return len(self.passcases)+len(self.failcases)

'''fail =[({'URL': 'http://ip.taobao.com/service/getIpInfo.php', 'Check Point': '"code":0', 'No.': '2', 'Request Data': '{"ip":"61.183.144.2611"}'}, '{"code":1,"data":"invaild ip."}', 'fail'),({'URL': 'http://ip.taobao.com/service/getIpInfo.php', 'Check Point': '"code":0', 'No.': '2', 'Request Data': '{"ip":"61.183.144.2611"}'}, '{"code":1,"data":"invaild ip."}', 'fail')]
pa = [({'URL': 'http://ip.taobao.com/service/getIpInfo.php', 'Check Point': '"code":0', 'No.': '1', 'Request Data': '{"ip":"61.183.144.26"}'}, {'data': {'area': '华中', 'isp_id': '100017', 'area_id': '400000', 'county': '', 'isp': '电信', 'region': '湖北省', 'country_id': 'CN', 'country': '中国', 'county_id': '-1', 'city': '武汉市', 'ip': '61.183.144.26', 'city_id': '420100', 'region_id': '420000'}, 'code': 0}, 'pass')]
r = ResultCount(fail,pa)
c,text = r.failcount()
print(text)'''


