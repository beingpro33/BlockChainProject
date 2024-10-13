import hashlib
import json
import time
from Transaction import TransactionEncoder


class Block:

    def __init__(self, timestamp, transactions, previous_hash=''):
        '''
        Initializes a block.
        :param timestamp: Timestamp of creation
        :param transactions: Block transactions
        :param previous_hash: Hash of the previous block
        :param hash: Block hash
        '''
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        '''
        Calculates the hash of the block.
        :return: Hash value
        '''
        # Concatenate block information and generate SHA256 hash value
        raw_str = self.previous_hash + str(self.timestamp) + json.dumps(self.transactions, ensure_ascii=False, cls=TransactionEncoder) + str(self.nonce)
        sha256 = hashlib.sha256()
        sha256.update(raw_str.encode('utf-8'))
        hash = sha256.hexdigest()
        return hash

    def mine_block(self, difficulty):
      '''
      Mine a block
      :param difficulty: Difficulty level for mining
      :return:
      '''
      time_start = time.perf_counter()
      # Require hash value to start with 'difficulty' number of zeros
      while self.hash[0: difficulty] != ''.join(['0'] * difficulty):
          self.nonce += 1
          self.hash = self.calculate_hash()
      print("Mined block: %s, Time taken: %f seconds" % (self.hash, time.perf_counter() - time_start))

