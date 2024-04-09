def two_dimensional_parity_check():
  bits = int(input("Enter number of bits :"))
  count = int(input("Enter the number of datas to be transmitted:"))
  par = input('Enter parity(odd(o)/even(e)) :')
  data = []

  for i in range(count):
    a = input('Enter the data :')
    data.append(a)

  for i in range(count):
    data[i] = make_parity(data[i],par)

  last = ''
  s = ''
#to find the parity for each columns
  for i in range(bits):
    for j in range(count):
      s += data[j][i]
    if par == 'o':
      last = (last +'1') if s.count('1')%2==0 else (last +'0')
    else:
      last = (last+'1') if s.count('1')%2==1 else (last + '0')
    s = ''
  data.append(make_parity(last,par))
  print(data)

  rx_data = []
  for i in range(len(data)):
    a = input('Enter the recieved data :')
    rx_data.append(a)

  changed = False
  #s = ''
  for i in range(count):
    if not check_parity_og(rx_data[i],par):
      print('The transmitted data is incorrect.')
      break
  if not changed:
    print('The transmitted data is correct.')

def check_parity_og(data, par):
  if par=='o':
    return data.count('1')%2 ==1
  else:
    return data.count('1')%2 ==0

def make_parity(data, par) :
  if par == 'o':
    data = (data+'1') if data.count('1')%2==0 else (data+'0')
  else:
    data = (data+'1') if data.count('1')%2==1 else (data + '0')
  return data

def main():
    print("\tERROR DETECTION METHODS")
    print("Two-Dimensional Parity Check\n")
    two_dimensional_parity_check()
main()


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

    if(value.count('1')%2==0 and parity==2) or (value.count('1')%2==1):
        print("the data is correct")
    else:
        print("the data is not correct")
def main():
    add_parity()
    check_parity()
main()