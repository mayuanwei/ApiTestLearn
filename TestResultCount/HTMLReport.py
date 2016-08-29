import HTMLTestRunner

class HTMLReport(object):
    def __init__(self,filename,suite):
        self.filename = filename
        self.suite = suite

    def htmlreport(self):
        try:
            f = open(self.filename, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(f, title='自动化测试报告', description='自动化测试报告')
            runner.run(self.suite)
        except:
            print('测试报告生成失败！请检查！')
            return False
        else:
            print('测试报告生成成功！')
            return True

    def report_parser(self):
        if self.htmlreport():
            try:
                f = open(self.filename, 'r', encoding='utf8')
                text = f.readlines()
                f.close()
            except:
                print('测试报告打开或读取失败！请检查！')
                return None
            else:
                te = ''
                for t in text:
                    te += t.replace('\n', '') + '\n'
                te = te.replace('charset=UTF-8', 'charset=gb2312')
                return te

#a = HTMLTestRunner()