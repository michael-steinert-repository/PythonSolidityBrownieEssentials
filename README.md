## Creating a virtual Environment that has Python3 as default Interpreter

* A virtual Environment allows each Project to have its own Dependencies
* ```python3 -m venv venv```

### Activate (initialize) the virtual Environment

* ```.\venv\Scripts\activate```

### Deactivate the virtual Environment

* ```deactivate```

### Dependencies

* ```pip install web3```
* ```pip install eth-brownie```

### Listing Dependencies

* ```pip list```

### Importing and calling everything from Module "web3_connection"

* ```python```
* ```from web3_connection import *```
* ```is_connected()```

### Brownie

* The Main Reason behind the Development of Brownie is using Python Testing Libraries for Testing Smart Contracts

### Brownie Commands

|Command|Description|
|---|---|
|Initialize Brownie Project|brownie init guess_number|
|Listing all Networks for Brownie|brownie networks list|
|Adding new Ganache Network to Brownie|brownie networks add development local host=http://127.0.0.1:7545 cmd=ganache|
|Open Brownie Console for local Network|brownie console --network local|
|Compiling Smart Contract GuessNumber|brownie compile GuessNumber.sol|
|Testing Smart Contract GuessNumber (before Testing the Smart Contract should be compiled)|brownie test|
|Deploying Smart Contract GuessNumber with a Script|brownie run deploy_guess_number.py|
|__Brownie Console__||
|network.accounts|Showing all Accounts in Network|
|accounts[1].transfer(accounts[0], "42 ether")|Sending Ether between Accounts|
|GuessNumber.deploy(42,{"from":accounts[0], "value": "10 ether"})|Deploying Smart Contract GuessNumber|
|GuessNumber[0].getBalance())|Interacting with Smart Contract GuessNumber|
|dir(GuessNumber)|Getting all Methods of a Python Object|
|GuessNumber.at("0x59423c400a7461B23e0A8086E5A85DFB4D4A91BD").getBalance()|Interacting with Smart Contract in Blockchain|
|GuessNumber.at("0x59423c400a7461B23e0A8086E5A85DFB4D4A91BD").guessNumber(accounts[2].address, 42, {"from": accounts[2], "value": "1 ether"})|Interacting with Smart Contract in Blockchain|
|GuessNumber.at("0x59423c400a7461B23e0A8086E5A85DFB4D4A91BD").currentState()|Interacting with Smart Contract in Blockchain|
