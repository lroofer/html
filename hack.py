import os
import random
while True:
    name = str(random.randint(1, 1000000))
    os.mkdir(name)
