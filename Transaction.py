import json

class Transaction:
    def __init__(self, from_address, to_address, amount):
        '''
        Initializes a transaction.
        :param from_address: Sender's address
        :param to_address: Receiver's address
        :param amount: Transaction amount
        '''
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount


class TransactionEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Transaction):
            return o.__dict__
        return json.JSONEncoder.default(self, o)
