import random

def generate_random_array(n):
    l = range(9999)
    return [random.choice(l) for _ in range(n)]

