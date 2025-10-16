def fibonacci(list):
    Fibo = list[1]
    for val in list:
        Fibo = Fibo + val
    return Fibo

my_list = [1, 2, 3, 4, 5]
print(fibonacci(my_list)) 
