count_fizz = 0
count_buzz = 0
count_FizzBuzz = 0

for i in range (100, 0, -1):
    if i == 1 :
        break    
    elif i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
        count_FizzBuzz += 1
    elif i % 5 == 0 :
        print("Buzz")
        count_buzz += 1
    elif i % 3 == 0 :
        print("Fizz")
        count_fizz += 1
    else :
        print (i)


print(f"Fizz: {count_fizz}")
print(f"Buzz: {count_buzz}")
print(f"FizzBuzz: {count_FizzBuzz}")