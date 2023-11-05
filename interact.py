from web3 import Web3,Account
import json
import random


# Connect to a local Hardhat node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
contract_address = '0x5FbDB2315678afecb367f032d93F642f64180aa3'  # Replace with the actual contract address
contract_abi = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "cardname",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "cardimage",
          "type": "string"
        }
      ],
      "name": "CreateCard",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "symbol",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "cardCount",
          "type": "uint256"
        }
      ],
      "name": "createCollection",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "collectionId",
          "type": "uint256"
        }
      ],
      "name": "getCardMetadata",
      "outputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "image",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "collectionId",
          "type": "uint256"
        }
      ],
      "name": "getCollectionAddress",
      "outputs": [
        {
          "internalType": "address[]",
          "name": "",
          "type": "address[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "collectionId",
          "type": "uint256"
        }
      ],
      "name": "getCollectionMetadata",
      "outputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "symbol",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "collectionId",
          "type": "uint256"
        }
      ],
      "name": "getMaxcards",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "maxcard",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "user",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "collectionId",
          "type": "uint256"
        }
      ],
      "name": "getUserAllCards",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getowner",
      "outputs": [
        {
          "internalType": "address",
          "name": "owneradd",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "initialOwner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    ]  # Replace with the contract's ABI as a list

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
result = contract.functions.getowner().call()

print('Result from the contract:', result)
privatekey='0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
account = Account.from_key(privatekey)

# Contract instance
contract_instance = w3.eth.contract(abi=contract_abi, address=contract_address)
account_address=account.address

### CREATE COLLECTION ###
print("\n### CREATE COLLECTION ###\n")
collname=input("Collection's Name : ")
collsymbole=input("Collection's Symbole : ")
maxcardincoll=1
print('\nThis collection contains '+str(maxcardincoll)+' cards\n')
tx = contract_instance.functions.createCollection(collname, collsymbole, maxcardincoll).build_transaction({'nonce': w3.eth.get_transaction_count(account_address)})
#Get tx receipt to get contract address
signed_tx = w3.eth.account.sign_transaction(tx, privatekey)
#tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
############

### CREATE CARD ###
print("\n### CREATE CARD ###\n")
for i in range(maxcardincoll):
    print('\nCard N°'+str(i)+' : ')
    to=input("Give card to : ") #give card to 
    cardname=input("Card Name : ") 
    cardimage=input("Card Image : ")
    tx = contract_instance.functions.CreateCard(to, cardname, cardimage).build_transaction({'nonce': w3.eth.get_transaction_count(account_address)})
    #Get tx receipt to get contract address
    signed_tx = w3.eth.account.sign_transaction(tx, privatekey)
    #tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#########################

### GET CARD METADATA###
print("\n### GET CARD METADATA ###\n")
CollectionID=input("Enter Collection ID: ")
#for i in range(maxcardincoll):
result = contract.functions.getCardMetadata(0,int(CollectionID)).call()
print(result)
#########################

### GET COLLECTION ADDRESS###
print("\n### GET COLLECTION ADDRESS ###\n")
CollectionID=input("Enter Collection ID: ")
result = contract.functions.getCollectionAddress(int(CollectionID)).call()
print(result)
#########################

### GET COLLECTION METADATA###
print("\n### GET COLLECTION METADATA ###\n")
CollectionID=input("Enter Collection ID: ")
result = contract.functions.getCollectionMetadata(int(CollectionID)).call()
print(result)
#########################

### GET USER's CARD###
print("\n### GET USERS CARD ###\n")
UserAdd=input("Enter User's Address: ")
CollectionID=input("Enter Collection ID: ")
result = contract.functions.getUserAllCards(UserAdd,int(CollectionID)).call()
print(result)
#########################

### GET MAX CARDS###
CollectionID=input("Enter Collection ID: ")
result = contract.functions.getMaxcards(int(CollectionID)).call()
print(result)
#########################


