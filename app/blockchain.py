import hashlib
import datetime as date
from http.client import HTTPException

# Cria um block
class Block:
    #Inicializa o bloco
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    #Calcula o hash do bloco
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    #Minera o bloco
    def mine_block(self, difficulty):
        while not ('307' * difficulty in self.hash):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Cria a blockchain (cadeia de blocos)
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
    
    #Cria o bloco genesis (o primeiro bloco da blockchain)
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    #Pega o último bloco da blockchain
    def add_block(self, new_block):
        new_block.previous_hash =  self.chain[-1].hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    #Verifica se a blockchain é válida
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        for block in self.chain:
            print("Block #", block.index)
            print("Timestamp: ", block.timestamp)
            print("Data: ", block.data)
            print("Previous Hash: ", block.previous_hash)
            print("Hash: ", block.hash)
            print(20*'----')
