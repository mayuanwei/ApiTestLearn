
f = open('C:\\Users\\cpr223\\PycharmProjects\\ApiTestLearn\\TestResult\\Result.html','r',encoding='utf8')
text = f.readlines()
f.close()
te = ''
for t in text:
    te += t.replace('\n','')+'\n'
te = te.replace('charset=UTF-8','charset=gb2312')
print(te)
