import random
import string
import colorama

digits = random.sample(string.digits, 2)
lowercase = random.sample(string.ascii_lowercase, 4)
uppercase = random.sample(string.ascii_uppercase, 1)
special = random.sample(["&", "@"], 1)
password = digits + lowercase + uppercase + special
random.shuffle(password)
print("Generate Password: \n", colorama.Fore.RED, "".join(password))
