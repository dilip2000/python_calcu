def title():
    print("~~~~~~Start_Calculator~~~~~~")
    print()
def calAdd(no1,no2): 
    addRes = no1+no2
    print(no1,"+",no2,"=",addRes)
    
def calSub(no1,no2): 
    subRes = no1-no2
    print(no1,"-",no2,"=",subRes)
    
def calmultiply(no1,no2): 
    multiplyRes = no1*no2
    print(no1,"*",no2,"=",multiplyRes)

def caldiv(no1,no2): 
    divRes = no1/no2
    print(no1,"/",no2,"=",divRes)

def calmod(no1,no2): 
    modRes = no1%no2
    print(no1,"%",no2,"=",modRes)
    
def caldiv1(no1,no2): 
    div1Res = no1//no2
    print(no1,"//",no2,"=",div1Res)

def caldiv2(no1,no2): 
    div2Res = no1/no2
    print(no1,"/",no2,"=",div2Res)
def title1():
    print()
    print("~~~~~~End_Calculator~~~~~~~~")
title()
calAdd(10,15)
calSub(20,10)
calmultiply(2,5)
caldiv(50,20)
calmod(2,9)
caldiv2(2.2,1.4)
caldiv1(5,20)
title()    
