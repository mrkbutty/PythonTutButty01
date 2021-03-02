def greet(name=None):
    if not name:
        name = 'World'
    text = 'Hello ' + name + '!'
    print(text)

greet()
answer = input('What is your name? ')
greet(answer)
