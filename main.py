import random

# Functions
def addition(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

addition(5,6)
addition(56,88,90)

def inventory(**invItems):
    for k,v in invItems.items():
        print("{} is {}".format(k,v))

inventory(firstName="Anna", surname="Smith")
inventory(firstName="Mike", surname="Miller", age=5)

#addition function
def addition(x,y):
    return x+y

# assign the function's return (of type int) to a variable and use it
sum = addition(5,6)
a = sum%2
print(a)

#addition using the lambda function
addition = lambda x,y: x+y
print(addition(11,3))

myList = [23,45,66,77,100]

def odd_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    new_l = filter(odd_numbers, myList)
    print(list(new_l))

    new_l_with_lambda = filter(lambda x:x%2 == 0, myList)
    print(list(new_l_with_lambda))

    new_l_map_with_lambda = map(lambda x:x%2, myList)
    print(list(new_l_map_with_lambda))

    print(random.randint(2,10))
    print(random.uniform(3, 5.5))
    print(random.choice(["anna", "mike","oranges"]))

#### CODE for read/write to a file as an example. We first write to file so you don't need to
#### have a file created already. the process below will create a new one in the same directory
#### as your main.py. Uncomment to run it.

    # with open('roomInfo.txt', 'w') as file:
    #     file.write("Hello World")
    #
    #     lines = ["Alice\n", "George\n"]
    #     file.writelines(lines)
    #
    # with open('roomInfo.txt', 'r') as file:
    #
    #     print(file.read())

if __name__ == '__main__':
    main()
