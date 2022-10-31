
userChoice = input('Enter the name of the file: ')
fileChoice = open(userChoice)

for text in fileChoice:
    if text.startswith('g'):
        continue
    print('The words were: ',text)
    exit()


