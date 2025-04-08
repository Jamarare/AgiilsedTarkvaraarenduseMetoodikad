def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print("vale sisestatud numbrid")

print(mySum(1,3))

def mySub(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a - b
    else:
        print("vale sisestatud numbrid")

print(mySub(1,3))

def myKorr(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a * b
    else:
        print("vale sisestatud numbrid")

print(myKorr(1,3))

def myJagamine(a,b):
    try:
        if isinstance(a,int) and isinstance(b,int):
            return a / b
        else:
            print("vale sisestatud numbrid")
    except ZeroDivisionError:
        print("Ei saa jagada nulliga")


def main():
    while True:
    valik = input("mida sa tahad?")
    if valik == "1":
        a = int (input("Sisesta number 1: "))
        b = int (input("Sisesta number 2: "))
        result = mySum(a,b)
        print("tulemus on: ",result)
    elif valik == "2":
        a = int (input("Sisesta number 1: "))
        b = int (input("Sisesta number 2: "))
        result = mySub(a,b)
        print("tulemus on: ",result)
    elif valik == "3":
        a = int (input("Sisesta number 1: "))
        b = int (input("Sisesta number 2: "))
        result = myKorr(a,b)
        myArr[2] += 1
        print("tulemus on: ",result)
    elif valik == "4":
        a = int (input("Sisesta number 1: "))
        b = int (input("Sisesta number 2: "))
        result = myJagamine(a,b)
        myArr[3] += 1
        print("tulemus on: ",result)
    else:
        print("seda valiku pole")
main()
    
    
def displayInfo():
    print("kokku oli ", sum(myArr))
    print("summeerimine töötas: ", myArr[0], "korda")
    print("lahutamine töötas: ", myArr[1], "korda")
    print("korrutamine töötas: ", myArr[2], "korda")
    print("jagamine töötas: ", myArr[3], "korda")
    
myArr = [0,0,0,0]


