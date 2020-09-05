'''
n = int(input())
fishs1 = list(map(int, input().split()))
count = 0
length = len(fishs1)
while True:
    index2 = 0
    for i  in range(1, length) :
        if fishs1[i] < fishs1[i-1]:
            fishs1[index2] += fishs1[i]
        else:
            index2 +=1
            fishs1[index2] = fishs1[i]
    print(fishs1)
    if index2+1 == length:
        break
    count += 1
    length = index2 +1
print(count)
'''
#1 最大连续和
#nums = list(map(int, input().split(',')))
import random
nums = []
for i in range(1000):
    nums.append(random.randrange(-10000, 10000))
print(nums)
result = []
for i in nums:
    result.append(0)
result[0] = nums[0]
index = 0
for i in range(1, len(nums)):
    if result[i-1] >= 0:
        result[i] = nums[i]+result[i-1]
    else:
        result[i] = nums[i]
print(max(result))