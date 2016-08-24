import requests

class HTTPRequestlib(object):
    """"""
    
    '''def __init__(self):
        """Constructor for HTTPRequestlib"""
        object.__init__(self)'''

    def get(self,url,para):
        result = requests.get(url,para)

        return result

#a = HTTPRequestlib()
#a.get('http://ip.taobao.com/service/getIpInfo.php','61.183.144.26')