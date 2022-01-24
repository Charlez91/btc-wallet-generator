from bitcoinaddress import Wallet

#creates a mainnet btc wallet of various types
def mainnet_wallet_create():
    wallet = Wallet()
    return wallet

#creates a testnet btc wallet of various types
def testnet_wallet_create():
    wallet = Wallet(testnet=True)
    return wallet

#imports a wallet with its private keys
def import_wallet(privatekey):
    wallet =  Wallet(privatekey)
    return wallet

#displays attribute of a wallet keys, address,etc
def wallet_attributes():
    wallet = Wallet()
    print(wallet.key.__dict__)
    print(wallet.key.__dict__['mainnet'].__dict__)
    print(wallet.key.__dict__['testnet'].__dict__)
    print(wallet.address.__dict__)
    print(wallet.address.__dict__['mainnet'].__dict__)
    print(wallet.address.__dict__['testnet'].__dict__)

print(mainnet_wallet_create())

x = str(mainnet_wallet_create())

with open('wallets.txt', 'w+') as f:
    f.write(x)