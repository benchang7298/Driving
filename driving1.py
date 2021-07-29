country = input('What is your nationnality: ')
age = input('How old are you? ')
age =int(age)
if country == 'taiwan':
    if age >= 18:
        print('over 18 you can get the license')
    else:
        print('Wait for 18')    
