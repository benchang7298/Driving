country = input('What is your nationnality: ')
age = input('How old are you? ')
age =int(age)
if country == 'taiwan':
    if age >= 18:
        print('over 18 you can get the license')
    else:
        print('Wait for 18')    
elif country == 'American':
    if age >= 16:
        print('over 16 you can get the license')
    else:
        print('Wait for 16')       
else:
    print('Only for Taiwan and USA')   