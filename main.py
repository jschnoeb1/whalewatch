import pandas as pd
import pprint
import numpy
from tqdm import tqdm
from web3 import Web3
from web3.auto import w3


def get_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def get_addrs(df: pd.DataFrame, header: str) -> list:
    return df[header].tolist()

def get_balance(node: Web3, addr: str) -> float:
    addr = node.toChecksumAddress(addr)
    return float(node.fromWei(node.eth.get_balance(addr), 'ether'))

def update_csv_col(filename: str, header: str, series: pd.Series):
    series.to_csv(filename)


# class to make writing custom data formatting easier.
# not strictly required.
class UserMethods:
    def __init__(self, node: Web3, params: dict):
        self.node = node
        self.params = params
    
    def csv1(self):
        outfile = params.get('outfile')
        header = params.get('header')
        update_csv_col(outfile, header, pd.Series(balances))


# THIS IS WORK IN PROGRESS LOL

def main():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    assert w3.isConnected()
    infile = 'data.csv'
    outfile = 'out.csv'
    header = 'DateTime'     # for some reason the header get is 1 col offset

    addresses = get_addrs(get_data(infile), header)
    balances = []

    print('getting balances...')
    for a in tqdm(addresses):
        balances.append(get_balance(w3, a))

    update_csv_col(outfile, header, pd.Series(balances))


if __name__=="__main__":
    main()

