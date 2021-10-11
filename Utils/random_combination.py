# This creates a random combination of numbers and letters that can be used for e.g ids.
import string
import random

def create(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
