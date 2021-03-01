print('Think of any vehicle')
wheels = int(input('How many wheels does it have? '))
passengers = int(input('What is the passenger limit (including the driver) ? '))
if wheels == 1 and passengers==1:
    print('I guess it is a uni-cycle')
elif wheels == 2 and passengers==1:
    print('I guess it is a bicycle')
elif wheels == 4 and (passengers >= 2 and passengers <= 7):
    print('I guess it is a car')
elif wheels == 4 and (passengers > 7 and passengers <= 30):
    print('I guess it is a bus')
elif wheels > 4 and passengers > 7:
    print('I guess it is a train')
else:
    print('I give up, I have no idea') 