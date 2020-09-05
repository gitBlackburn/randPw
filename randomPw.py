import random
import string

def randomPw(pwLength):
    randList = ""
    for i in range(pwLength):
        choice = random.choice([random.randint(0,9),random.choice(string.punctuation),random.choice(string.ascii_letters)])
        randList += str(choice)
    return(randList)


print(randomPw(16))
