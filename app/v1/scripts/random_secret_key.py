import random
import string



def random_secret_key():
    """
    Generates a random secret key for you to use in your .env file.
    """
    secret_key = ''.join([random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(64)])
    print('SECRET_KEY = "{}"'.format(secret_key))


random_secret_key()