import random
import string

class shortner:

    token = 5

    def __init__(self, token=None):
        self.token = token if token is not None else 5
    
    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token) )
