# Blockchain Project

## Overview

This project simulates a basic blockchain system using Python. It demonstrates key blockchain concepts, including creating blocks, processing transactions, mining blocks, and ensuring data integrity through cryptographic hashing.

## Features

- **Blockchain Creation**: Simulates the formation of a blockchain with interconnected blocks.
- **Transactions**: Represents transfers between addresses, recording sender, receiver, and amount.
- **Proof of Work**: Implements the Proof of Work (PoW) consensus algorithm for mining blocks.
- **Mining Rewards**: Simulates the rewards given to miners for validating and adding new blocks.

## How it Works

1. **Block Creation**:
   - Each block contains:
     - A list of transactions
     - A timestamp
     - A reference to the previous block’s hash
     - Its own unique hash
2. **Transactions**:
   - Each transaction represents a transfer of value between two addresses. A miner selects pending transactions to include in the next block to be mined.
3. **Mining**:

   - Mining involves solving a complex mathematical puzzle, i.e., finding a hash that meets a specific difficulty level. Once the valid hash is found, the block is added to the blockchain.

4. **Balances**:
   - The project tracks the balance of each address after transactions are mined. Mining rewards are given to the miner’s address.

## Key Concepts

- **Mining**: The process of validating and adding a new block to the blockchain.
- **Difficulty**: The level of computational effort required to mine a block.
- **Genesis Block**: The first block in the blockchain, which is created manually.
- **Proof of Work**: A consensus mechanism that ensures the blockchain’s integrity by making it computationally intensive to alter.

## Output

- **Mined Block**: When a block is mined successfully, the system outputs the block hash and the time taken to mine.
- **Address Balances**: Shows the balance of different addresses before and after transactions are mined.

## Conclusion

This project demonstrates the fundamental workings of a blockchain system, including block creation, transaction validation, mining, and maintaining balances across addresses. The mining process and the Proof of Work algorithm ensure the security and immutability of the blockchain.
