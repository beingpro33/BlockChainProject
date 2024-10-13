from Block import Block
from Transaction import Transaction, TransactionEncoder
import time

class BlockChain:
    def __init__(self):
        # Initialize the chain and add the genesis block
        self.chain = [self._create_genesis_block()]
        # Set initial difficulty
        self.difficulty = 5
        # Pending transactions
        self.pending_transactions = []
        # Set mining reward
        self.mining_reward = 100

    @staticmethod
    def _create_genesis_block():
        '''
        Creates the genesis block.
        :return: Genesis block
        '''
        timestamp = time.mktime(time.strptime('2018-06-11 00:00:00', '%Y-%m-%d %H:%M:%S'))
        return Block(timestamp, [], '')

    def get_latest_block(self):
        '''
        Gets the latest block in the chain.
        :return: Latest block
        '''
        return self.chain[-1]

    def add_transaction(self, transaction):
        '''
        Adds a transaction.
        :param transaction: New transaction
        :return:
        '''
        # Perform a series of validations on the transaction based on the business logic
        '''...'''
        # Add to pending transactions
        self.pending_transactions.append(transaction)

    def mine_pending_transaction(self, mining_reward_address):
        '''
        Mines pending transactions
        :param mining_reward_address: Address for mining reward
        :return:
        '''
        block = Block(time.time(), self.pending_transactions, self.chain[-1].hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        # After successful mining, reset pending transactions and add a transaction, which is the reward for this mining
        self.pending_transactions = [
            Transaction(None, mining_reward_address, self.mining_reward)
        ]

    def get_balance_of_address(self, address):
        '''
        Gets wallet balance
        :param address: Wallet address
        :return: Balance
        '''
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.from_address == address:
                    # Expenditure for transactions initiated by oneself
                    balance -= trans.amount
                if trans.to_address == address:
                    # Income
                    balance += trans.amount
        return balance

if __name__ == '__main__':
    # Test
    blockChain = BlockChain()
    # Add two transactions
    blockChain.add_transaction(Transaction('address1', 'address2', 100))
    blockChain.add_transaction(Transaction('address2', 'address1', 50))
    # Mine pending transactions with address3
    blockChain.mine_pending_transaction('address3')
    # Check account balances
    print('address1 balance ', blockChain.get_balance_of_address('address1'))
    print('address2 balance ', blockChain.get_balance_of_address('address2'))
    print('address3 balance ', blockChain.get_balance_of_address('address3'))
    # Mine pending transactions with address2
    blockChain.mine_pending_transaction('address2')
    print('address1 balance ', blockChain.get_balance_of_address('address1'))
    print('address2 balance ', blockChain.get_balance_of_address('address2'))
    print('address3 balance ', blockChain.get_balance_of_address('address3'))
