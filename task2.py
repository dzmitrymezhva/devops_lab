list1 = list(map(int, input('Please enter first list separated by spaces: ').split()))
list2 = list(map(int, input('Please enter second list separated by spaces: ').split()))
result = []
s = " "

for element in list1:
    if element in list2 and element not in result:
        result.append(element)
result.sort()
resultStr = [str(x) for x in result]
resultStr = s.join(resultStr)
print(resultStr)
