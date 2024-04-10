def singel_par(data,p):
    c=data.count('1')
    if p==1:
        if c%2==1:
            data.append('0')
        else:
            data.append('1')
    else:
        if c%2==0:
            data.append('0')
        else:
            data.append('1')
    return data
def double_par(data,l,p):
    colpar=[]
    for i in range(l):
        c=0
        for j in data:
            if j[i]=='1':
                c=c+1
        if p==1:
            if c%2==1:
                colpar.append('0')
            else:
                colpar.append('1')
        else:
            if c%2==0:
                colpar.append('0')
            else:
                colpar.append('1')
                
    colpar=singel_par(colpar,p)
    data.append(colpar)
    return data

n=int(input("Enter the no of data:"))
l=int(input("Enter the length of each frame:"))
print("\n1.Odd Parity\n2.Even Parity")
p=int(input("Enter the Parity:"))
data=[]
for i in range(n):
    d=list(input("Enter the data:"))
    d=singel_par(d,p)
    data.append(d)
data=double_par(data,l,p)
print(data)
rx=[]
for i in range(n+1):
    r=list(input("Enter the received data:"))
    rx.append(r)
if data==rx:
    print("Success")
else:
    print("Wrong")
