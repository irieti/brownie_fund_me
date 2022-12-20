from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    accounts,
)
from scripts.deploy import deploy_fund_me
from brownie import network, exceptions
import pytest

gas_strategy = "10 gwei"


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund(
        {"from": account, "value": entrance_fee, "gas_price": gas_strategy}
    )
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account, "gas_price": gas_strategy})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


# to run tests only on development network
# pytest.skip


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # fund_me.withdraw({"from": bad_actor, "gas_price": gas_strategy})
    # how to tell the pytest that we want thise test to fail?
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor, "gas_price": gas_strategy})
