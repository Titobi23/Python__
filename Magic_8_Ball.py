# Magic 8 Ball

import random
question = input("What is your question? ")
answer = random.randint(1, 20)
print("Question: {}".format(question))
if answer == 1:
    print('It is certain')
elif answer == 2:
    print('Yes')
elif answer == 3:
    print('Reply hazy try again')
elif answer == 4:
    print('Ask again later')
elif answer == 5:
    print('Concentrate and ask again')
elif answer == 6:
    print('My reply is no')
elif answer == 7:
    print('Outlook not so good')
elif answer == 8:
    print('Very doubtful')
elif answer == 9:
    print('Signs point to yes')
elif answer == 10:
    print('Without a doubt')
elif answer == 11:
    print('Better not tell you now')
elif answer == 12:
    print('Cannot predict now')
elif answer == 13:
    print('Most likely')
elif answer == 14:
    print('No')
elif answer == 15:
    print('Don\'t count on it')
elif answer == 16:
    print('My sources say no')
elif answer == 17:
    print('Outlook good')
elif answer == 18:
    print('Yes - definitely')
elif answer == 19:
    print('You may rely on it')
elif answer == 20:
    print('As I see it, yes')
else:
    print('Don\'t count on it')