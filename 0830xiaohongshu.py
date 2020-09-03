from itertools import combinations, permutations
a = list(permutations([1,2,3], 2))
b = list(combinations([1,2,3], 2))
print(a)
print(b)




'''
n, m = map(int, input().split())

foodList = {}
foods = []
for i in range(n):
    food, number = input().split()
    foods.append(food)
    foodList[food] = int(number) if int(number) > 0 else 0

#print(foodList)
_ = input()

orderList = {}
for i in range(m):
    name, op, food = input().split()
    nameList = [_name for (_name, _) in orderList.items()]
    if name not in nameList:
        orderList[name] = None
#    print(nameList)
    if op == 'order':
        if food in foods and foodList[food] > 0 and orderList[name]==None:
            orderList[name] = food
            foodList[food] -= 1
            print('yes')
        else:
            print('no')
    elif op == 'release':
        if food in foods and orderList[name] == food:
            orderList[name] = None
            foodList[food] += 1
            print('yes')
        else:
            print('no')
    else:
        print('no')
'''