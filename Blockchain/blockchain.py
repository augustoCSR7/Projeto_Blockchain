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

    def get_index(self):
        return self.index

    def get_timestamp(self):
        return self.timestamp

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.data) + str(
            self.nonce)).encode())
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
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        b = Block(0, time.time(), None, "Genesis Block")
        b.proof_of_work(self.difficulty)
        return b

    def new_block(self, data):
        latest_block = self.get_latest_block()
        return Block(latest_block.get_index() + 1, time.time(), latest_block.get_hash(), data)

    def add_block(self, block):
        if block is not None:
            block.proof_of_work(self.difficulty)
            self.chain.append(block)

    def get_latest_block(self):
        return self.chain[-1]

    def is_first_block_valid(self):
        first_block = self.chain[0]

        if first_block.get_index() != 0:
            return False

        if first_block.get_previous_hash() is not None:
            return False

        if first_block.get_hash() is None or first_block.get_hash() != first_block.calculate_hash():
            return False

        return True

    def is_valid_new_block(self, new_block, previous_block):
        if new_block is not None and previous_block is not None:
            if previous_block.get_index() + 1 != new_block.get_index():
                return False

            if new_block.get_previous_hash() is None or new_block.get_previous_hash() != previous_block.get_hash():
                return False

            if new_block.get_hash() is None or new_block.get_hash() != new_block.calculate_hash():
                return False

            return True

        return False

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
