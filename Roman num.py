def count_digit(num):
    global n
    n=0
    while num!=0:
        num = num//10
        n += 1
    return n

rom1 = ['I','II','III','IV','V','VI','VII','VIII','IX','X','']
rom2 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C']
rom3 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']

def first():
    global num,rom1,rom2,rom3
    f = num%10
    sec = rom1[f-1]
    return(sec)
    
def second():
    global n,rom1,rom2,rom3,s
    if n==2:
        a1 = s%10
        hun = rom2[a1]
        return(hun)

def third():
    global n,num,rom1,rom2,rom3,s
    if n==3:
        a1 = num//100
        ths = rom3[a1]
        s =  num//10
        return(ths)
     
num = int(input("Enter the number: "))
print("No. of digit is: ",count_digit(num))

if num < 100:
    s =  num//10
    if second()!= None:
        print(second(),end= "")
    if first()!= None and num%10!=0:
        print(first())
if num >= 100:
    if third()!= None:
        print(third(),end= "")
        n=2
    if second()!= None:
        print(second(),end= "")
    if first()!= None and num%10!=0:
        print(first())