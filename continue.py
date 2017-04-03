# Filename : continue.py

while True:
    s =raw_input('Enter something : ')
    if s== 'quit':
        break
    if len(s)<3 :
        continue
    print 'Repeat it agin '
print '已经跳出了while 循环'
    
