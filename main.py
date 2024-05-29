import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data ,previous_hash):
        self.index = index 
        self.timestamp = timestamp
        self.data = data
        self.previous_hash
        self.hash = self.hash_block()
        
def hash_block(self):
    sha = hasher.sha256
    sha.update(str(self.index) +
                str.(self.index) +
                str.(self.index) +
                str.(self.data) +
                str(self.previous_hash))
    return sha.hexdigest()

def genesis_block():
    return Block(0, date.datetime.now,"Genesis block", "0")
    