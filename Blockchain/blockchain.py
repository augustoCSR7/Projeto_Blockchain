import hashlib
import time

class Block:
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.data) + str(self.nonce)).encode())
        return sha.hexdigest()

    def proof_of_work(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
    def __str__(self):
        block_str = (
            f"Block {self.index}:\n"
            f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Data: {self.data}\n"
            f"Nonce: {self.nonce}\n"
            f"Hash: {self.hash}\n"
        )
        return block_str

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, time.time(), "0", "Genesis Block")

    def add_block(self, block):
        block.previous_hash = self.get_latest_block().hash
        block.proof_of_work(self.difficulty)
        self.chain.append(block)

    def get_latest_block(self):
        return self.chain[-1]

    def is_blockchain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

