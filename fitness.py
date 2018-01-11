import math
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','+','*','-','?','_','=','$']
charset=characters+numbers+symbols
def readLines(name):
    with open(name+'.txt') as f:
        content=f.readlines()
    content = [x.strip() for x in content]
    return content
def ratePassword(password):
    rating=0
    rating=math.pow(len(password),4)
    for i in range(0,10):
        if str(numbers[i]) in password:
            rating=rating*2
    for m in range(0,len(symbols)):
        if str(symbols[m]) in password:
            rating=rating*100
    return rating
def rateOutputFile(name):
    content=readLines(name)
    rating=0
    for i in range(0,len(content)):
        rating=+ratePassword(content[i])
    print(str(rating))
rateOutputFile('output')
        
        
    
    
