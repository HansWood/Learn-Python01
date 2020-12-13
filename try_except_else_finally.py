
try:
    number_input_a = int(input("please enter integer: "))

    print(number_input_a)
    print(2 * 3.14 * number_input_a)
    print(3.14 * number_input_a * number_input_a)

except:

    print("fail")

else:

    print("success")

finally:

    print("end")
