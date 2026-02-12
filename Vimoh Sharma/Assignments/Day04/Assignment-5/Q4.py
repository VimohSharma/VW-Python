#Random Pass Generator
import string
import random

len=int(input("Enter password length (8-12 length): "))

uppercase= string.ascii_uppercase
lowercase=string.ascii_lowercase
digits=string.digits
special_char="!@#$%^&*<>"

all_c=uppercase+lowercase+digits+special_char

password= [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(special_char)
]

for i in range(len-4):
    password.append(random.choice(all_c))

random.shuffle(password)

final_password="".join(password)
print("Generated Password: ", final_password)
