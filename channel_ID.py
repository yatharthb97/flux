"""
This program is done to create random Alpha-Numeric Channel_IDs and assign it to the
different channels from where the datum is coming

"""

import random, string

def getChannel_ID(length):
   
    """Generate a random string"""
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    
print("Random Alphanumeric String for Channel_ID = ", getChannel_ID(5))