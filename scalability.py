import multiprocessing as mp

from web3 import Web3

from time_utils import timer


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

input_data = list()

def transfer_eth_tx(input_data):
    private_key, receiver, nonce = input_data
    tx = {
        'chainId': 9999,
        'nonce': nonce,
        'to': receiver,
        'value': w3.toWei(1, 'gwei'),
        'gas': 21000,
        'gasPrice': w3.toWei(4, 'gwei')
    }

    #sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)

    #send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

def get_test_transfer():
    global input_data
    admin_pk = '0xc2ad502333c4abe844ba18be9918a5ee463b214b847a4ab90f00ae35be06b2b8'
    admin_addr = '0x8AD032E701410A62c2E2b66393680648A0352A56'
    nonce = w3.eth.get_transaction_count(admin_addr)

    print('nonce', nonce)

    for i in range(1500):
        input_data.append([admin_pk, admin_addr, nonce+i])
    pool = mp.Pool(mp.cpu_count())
    return pool, input_data

@timer
def transfer_scalability(pool):
    global input_data
    pool.map(transfer_eth_tx, input_data)
    

if __name__ == '__main__':
    pool, input_data = get_test_transfer()
    transfer_scalability(pool)
