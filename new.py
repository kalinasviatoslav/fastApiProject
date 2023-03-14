import os
my_secret = os.environ['MY_SECRET']
print(my_secret)
print(my_secret)
print('ALOHADANCE')
if my_secret == "TEST":
    print('ok')
else:
    raise MemoryError