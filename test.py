import re

colors = ['red','blue','violet']

text = 'this is text for blue CommonPasswordValidator'

for color in colors:
    print('we need '+color+' color')

    if re.search(color,text):
        print(color+' color found')

    else:
        print(color+' color not fdfound')
