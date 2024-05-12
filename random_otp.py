# You can simply improvice random library to generate OTP code in Python
from random import randint

otp = randint(1000,9999)

print(f"Your random value is: {otp}")