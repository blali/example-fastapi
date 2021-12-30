#!/usr/bin/python3

def hello_decorator(func):
    
    def inner1():
        print('Inner 1 before')
        func()
        print('Inner 1 after')
    
    return inner1

@hello_decorator # this is used my use case 2
def function_to_be_used():
    print('This is inside the function!')

# use case 1 - must remove @hello_decorator
#function_to_be_used = hello_decorator(function_to_be_used)
#function_to_be_used()

# use case 2
#function_to_be_used()