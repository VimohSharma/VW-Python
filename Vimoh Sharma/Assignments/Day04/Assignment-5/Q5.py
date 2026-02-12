#CAPTCHA Checker
import string
import random

captcha_len=6
chars=string.ascii_letters+string.digits
captcha="".join(random.choice(chars) for i in range(captcha_len))

print("CAPTCHA:", captcha)

userin=input("RETYPE CAPTCHA: ")

if userin==captcha:
    print("Verified")
else:
    print("Incorrect Captcha, Try Again.")