string = input("Please enter sentence: ")
result = []
words = string.split()
for element in words:
    result.append(element[::-1])
print(" ".join(result))
