import json
import random
import os
import string

dirname = os.path.dirname(__file__)
names_json = os.path.join(dirname, 'names.json')
surnames_json = os.path.join(dirname, 'surnames.json')
domain_list = ['@gmail.com', '@yahoo.com', '@outlook.com']

names = json.loads(open(names_json).read())
surnames = json.loads(open(surnames_json).read())

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


for i in range (10):
    user_i = User(random.choice(names) + '.' + random.choice(surnames) + str(random.randrange(100)) + random.choice(domain_list), ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range (10)))
    print(user_i.email)
    print(user_i.password)