'''
    @Author: Sudhanshu Kumar
    @Date: 24--11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-11-2024
    @Title : Python program to reverse an integer
'''

def reverse(num):
    sign = num
    rev = 0
    if num<0:
        num = -1*num
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    if sign<0:
        rev = -1*rev
    return rev

def main():
    num =-234
    print(reverse(num))

if __name__=="__main__":
    main()