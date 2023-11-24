import csv
a=[]
with open ('example_100kb.csv') as f:
    s=f.readlines()
    for i in range (1, len(s), 2):
        a.append(s[i].strip()+s[i+1])

b={}
for i in range (len(a)):
    s=a[i].split(',')
    s=s[2]
    j=s.find('@')
    if s[j+1:] not in b:
        b[s[j+1:]]=1
    else:
        b[s[j+1:]]+=1
print(b)
with open ('file.csv','w',newline='')  as f:
    writer=csv.writer(f)
    for key in b:
        writer.writerow[key,b[key]]

