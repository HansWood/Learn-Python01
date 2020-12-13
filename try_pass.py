
list_input_a = ["1", "t", "3", "f", "5"]

list_number = []

for item in list_input_a:

    try:
        int(item)
        list_number.append(item)
    except:
        
        pass

print(list_input_a)
print(list_number)