from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3
from brownie.network import gas_price

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache-local-nw"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


gas_strategy = "10 gwei"


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account(), "gas_price": gas_strategy},
        )
    print("Mocks deployed!")
