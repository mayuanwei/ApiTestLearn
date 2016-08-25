import xlrd
import requests
import os,sys
import json

def testrunner(testcasefile):
    testcasefile = os.path.join(os.getcwd(),testcasefile)
    if not os.path.exists(testcasefile):
        print('测试用例文件不存在！')
        sys.exit()

    testcase = xlrd.open_workbook(testcasefile)
    sht = testcase.sheet_by_index(0)

    testcaselist = []
    corcase = []
    errcase = []
    for i in range(1,sht.nrows):
        if sht.cell_value(i,10).replace('\n','').replace('\r','') != 'Yes':
            continue
        api_num = sht.cell_value(i,0).replace('\n','').replace('\r','')
        api_purpose = sht.cell_value(i,1).replace('\n','').replace('\r','')
        api_host = sht.cell_value(i,2).replace('\n','').replace('\r','')
        api_url = sht.cell_value(i,3).replace('\n','').replace('\r','')
        request_method = sht.cell_value(i,4).replace('\n','').replace('\r','')
        request_data_type = sht.cell_value(i,5).replace('\n','').replace('\r','')
        request_data = sht.cell_value(i,6).replace('\n','').replace('\r','')
        encryption = sht.cell_value(i,7).replace('\n','').replace('\r','')
        check_point = sht.cell_value(i,8).replace('\n','').replace('\r','')
        correlation = sht.cell_value(i,9).replace('\n','').replace('\r','')

        if request_data_type == 'Form':
            datafile = os.path.join(os.getcwd(),'TestData\\'+api_purpose+'.txt')
            if os.path.exists(datafile):
                fopen = open(datafile)
                request_data = fopen.readlines()
                fopen.close()
            for i in range(len(request_data)):
                request_data[i] = request_data[i].replace('\n','').replace('\r','')
                status,result = api_test(api_num,api_purpose,api_host,api_url,request_method,request_data_type,request_data[i],check_point)
                if status != 200:
                    errcase.append((api_num + ' ' + api_purpose + api_host+api_url,'第%d条数据执行失败！'%(i+1) + str(result)))
                else:
                    corcase.append((api_num + ' ' + api_purpose + api_host+api_url,'第%d条数据执行成功！'%(i+1) + str(result)))

    return corcase,errcase

def api_test(api_num,api_purpose,api_host,api_url,request_method,request_data_type,request_data,check_point):
    request_data = json.loads(request_data)
    if request_method == 'POST':
        res = requests.post(api_url+api_host,request_data)
    else:
        res = requests.get(api_host+api_url,request_data)

    if res.status_code == 200:
        if res.text.find(check_point) > 0:
            return res.status_code,json.loads(res.text)
        else:
            return 2001,res.text
    else:
        return res.status_code,res.text

def main():
    cortest,errtest = testrunner('TestCase\TestCase.xlsx')
    print('成功：',cortest)
    print('失败：',errtest)

if __name__ == '__main__':
    main()

