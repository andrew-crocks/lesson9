def add_one():
   
    digits = input("Введіть цифри, розділені комами: ")
    digits = digits.split(",")  
    digits = [int(digit) for digit in digits]  

    num = int("".join(map(str, digits))) 
    sum_num = num + 1

    return [int(digit) for digit in str(sum_num)]

result = add_one()
print(result)
