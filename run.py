import time

print('Hi, friend! What is your name?')
userName = input()
time.sleep(1)
print('Oh, ' + str(userName) + ', huh? I like the sound of that. Do you want to hear a joke? Y/N?')
answer = input()
time.sleep(1)
if answer == 'y':
    print('What do you call a can opener that doesn\'t work? A can\'t opener! Haha!')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('What? That was hilarious.')
    time.sleep(2)
    print('Okay, then. Do you want another joke? Y/N?')
    secondAnswer = input()
    time.sleep(2)
    if secondAnswer == 'y':
        print('Nah, I changed my mind. See ya!')
    if secondAnswer == 'n':
        print('Fine. I didn\'t want to tell another one anyway!')
if answer=='n':
    print('I can\'t believe this... ' + str(userName) + ', what am I supposed to do with my life now?')
