from brownie import FundMe
from scripts.helpful_scripts import get_account

gas_strategy = "10 wei"


def fund():
    fund_me = FundMe[-1]  # the most recent deployed contract
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee, "gas_price": gas_strategy})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account, "gas_price": gas_strategy})


def main():
    fund()
    withdraw()
