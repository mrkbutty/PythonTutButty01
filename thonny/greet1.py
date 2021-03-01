def greet(name=None):
    if name==None or name=='':
        name = 'World'
    text = 'Hello ' + name + '!'
    print(text)

print(greet)
answer = input('What is your name? ')
greet(answer)