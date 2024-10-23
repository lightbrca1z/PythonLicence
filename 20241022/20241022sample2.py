def say_something():
    print('hi')

say_something();

print (type(say_something))

def what_is_this(color):
    print(color)

what_is_this('red');

def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result = what_is_this2('red')
print(result)