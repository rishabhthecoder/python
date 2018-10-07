f=open('ban.txt','w+')
f.write('my \nname\n is')
t=open('temp.txt','a+')
a=f.readline()
while True:
    if(a=='name'):
        t.write('ris')
    elif(a==''):
        break
    else:
        t.write(a)
    a=f.readline()
#f.remove()
#f.close()
t.seek(0)
#f=open('ban.txt','a+')
f.write(t.read())
#t.remove()
f.seek(0)
t.seek(0)
print(t.read(),'\n\n',f.read())
f.close()
t.close()
