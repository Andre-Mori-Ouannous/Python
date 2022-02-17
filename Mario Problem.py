#Mario Problem

def mario():
    spa = " "
    has = "*"
    a = input("Input the number of blocks: \n")
    if a.isnumeric():
        for i in range(1,int(a)+1):
           print(spa * (int(a)-i) + has*i)   
    else:
        print("enter a correct number type. \n")
        mario()

mario()