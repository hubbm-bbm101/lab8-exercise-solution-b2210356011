import sys
inputs=sys.argv[1].split(",")
with open("student.txt","r") as f:
    metin=f.readlines()
    for j in range(len(metin)):
        metin[j]=metin[j].strip('\n ')
    cmd2=[]
    for i in metin:
        i=i.split(":")
        cmd2.append(i)
dic=dict()
for k,v in cmd2:
    dic[k]=v
print(dic.keys())
x=True
while x==True:
    for i in inputs:
        try:
            print("name: %s"%i,"University: %s"%dic[i])
        except KeyError:
            print("No record of ",i, " was found!")
    x=False



