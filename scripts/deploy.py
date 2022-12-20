from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from .helpful_scripts import deploy_mocks


gas_strategy = "10 wei"


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract (add address 0x...)

    # if we are on a persistent network like goerli, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": get_account(), "gas_price": gas_strategy},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()


# FORKING AND MOCKING
