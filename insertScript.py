#f = open('insertData','r')
#s = open('insertStatement','r')
f = open('InsertSample','r')
s = open('InsertStatementSample','r')
flag = False
query = s.readline()
print('Insert sample: ')
print(query)
print('---------Result---------')
text = ""
for x in f:
    x = '\'' + x.replace(',','\',\'').replace('\n','') + '\''
    text = text+query.replace('{values}',x.strip())+';\n'
print(text)

f.close()
s.close()
result = open('Insert.sql','w')
result.write(text)

result.close()