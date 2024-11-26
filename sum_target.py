'''
    @Author: Sudhanshu Kumar
    @Date: 24--11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-11-2024
    @Title : Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target

'''

def sum_target(arr,target):
    li = [0,0]
    for index in range(len(arr)-1):
        li[0]=index
        req = target-arr[index]
        for sec_index in range(len(arr)):
            if req == arr[sec_index]:
                li[1]=sec_index
                return li

def main():
    arr = [2,3,4,5,7]
    target = 8
    print(sum_target(arr,target))

if __name__=="__main__":
    main()
