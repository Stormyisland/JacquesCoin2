import hashlib 
import datetime as date
from flask import Flask # type: ignore
from flask import request # type: ignore
node = Flask(__name__)


class Block:
    def __init__(self, index, timestamp, data ,previous_hash):
        self.index = index 
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hashlib.sha256()
        hash_string = str(self.index)         
        str(self.timestamp) 
        str(self.data) 
        str(self.previous_hash) 
        sha.update(hash_string.encode("utf-8"))
        return sha.hexdigest()

# Manually construct a block with
# index zero and arbitrary previous hash
  
def create_genesis_block():
    return Block(0, date.datetime.now(), "the Genesis block", "0")

        
def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! i'm the Block # " + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

    #Create the blockchain and add the genesis block

blockchain  = [create_genesis_block()]
previous_block = blockchain [0]

num_of_blocks_to_add = 200

for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
    
print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
print ("Hash: {}\n".format(block_to_add.hash)) 
