f = open('updateStatement', 'r')
update = open('Update.sql','w')
statement = f.readline().strip()

print('Update sample: ')
print(statement)
print('---------Result---------')

#params = open('updateOldData','r')
#newdata = open('updateNewData')
newdata = open('UpdateSampleNew')
params = open('UpdateSample','r')
table  = params.readline().strip()
columns = params.readline().strip().split(',')
param = params.readline().strip()

text = ''
# pointer is set to first param and first line in new data
for line in newdata:
    values = line.split(',')
    result = ''
    for i in range(0,len(values)): 
        result = result + columns[i]+'=\''+values[i].strip()+'\','
    result = result[:-1]
    p = params.readline().strip()
    text = text + statement.replace('{table}',table).replace('{values}',result).replace('{parameter}',param).replace('{p}', p)+';\n'
print(text)


update.write(text)
f.close()
update.close()
params.close()