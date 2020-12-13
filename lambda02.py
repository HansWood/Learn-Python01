list_input_a = [1, 2, 3, 4, 5]

ouput_3 = map(lambda x: x * x, list_input_a)

print(list(ouput_3))


ouput_4 = filter(lambda x: x < 3, list_input_a)

print(list(ouput_4))