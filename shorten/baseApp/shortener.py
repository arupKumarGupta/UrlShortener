import random
master = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def shorten():
    m = ''
    for i in range(6):
        m+=random.choice(master)
    return m
