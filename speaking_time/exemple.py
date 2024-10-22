import random
import string

my_word  = [[random.choice(string.ascii_letters) for i in range(10)]for _ in range(10)]
print(my_word)