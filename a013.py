import sys

#羅馬數字轉換字典
roman_n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#羅馬數字轉阿拉伯數字
def inv_roman(s):
    result = 0
    for i in range(len(s)-1):
        if roman_n[s[i]] < roman_n[s[i+1]]:
            result -= roman_n[s[i]]
        else:
            result += roman_n[s[i]]
    result += roman_n[s[-1]]
    return result

def to_roman(n):
    result =''
    roman_l = ['M','D','C','L','X','V','I'] 
    for s in roman_l:
        result += s * (n//roman_n[s])
        n -= roman_n[s] * (n//roman_n[s])
    #簡化轉換
    for old,new in [['DCCCC','CM'],['CCCC','CD'],['LXXXX','XC'],['XXXX','XL'],['VIIII','IX'],['IIII','IV']]:
        result = result.replace(old,new)
    
    if result == '':
        result = 'ZERO'
    return result

while True:
    s = sys.stdin.readline()
    if s == '#\n':
        break
    else:
        a,b = s[:-1].split(' ')
        c = abs(inv_roman(a)-inv_roman(b))
        print(to_roman(c))