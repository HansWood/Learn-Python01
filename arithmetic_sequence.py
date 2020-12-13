def sum(fitem = 1, litem = 100, step = 1):
    output = 0

    for i in range(fitem, litem + 1, step):
        output += i
    
    return output


value = sum(1, 100, 1)

print(value)

for i in range(1, 10, 1):
    print(i)