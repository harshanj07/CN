#single parity
def add_parity():
    value=(input("enter the data:"))
    print("1)odd parity")    
    print("1)even parity")    
    parity=int(input("enter the parity"))

    count=0

    if parity==1:
        if value.count('1')%2==1:
            value+='0'
        else:
            value+='1'
    else:
        if value.count('1')%2==0:
            value+='0'
        else:
            value+='1'
    print(f"the transmitted data is:{value}")

def check_parity():
    value=input("enter the received data:")
    print("1) odd parity")
    print("2) even parity")
    parity=int(input("enter the parity:"))

    if(value.count('1')%2==0 and parity==2) or (value.count('1')%2==1 and parity==1):
        print("the data is correct")
    else:
        print("the data is not correct")
def main():
    add_parity()
    check_parity()
main()
