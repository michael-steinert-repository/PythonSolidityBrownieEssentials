import pytest
from brownie import Wei, accounts, GuessNumber


# Decorator
# pytest runs fixtures and captures what they returned (if anything), and passes those Objects into the Test Function as Arguments
@pytest.fixture
def guess_number():
    return GuessNumber.deploy(42, {"from": accounts[0], "value": "10 ether"})


def test_guess_wrong_number(guess_number):
    pre_contract_balance = guess_number.getBalance()
    pre_guesser_balance = accounts[1].balance()
    guess_number.guessNumber(accounts[1].address, 41, {"from": accounts[1], "value": "1 ether"})

    assert guess_number.getBalance() == (pre_contract_balance + Wei("1 ether"))
    assert accounts[1].balance() == (pre_guesser_balance - Wei("1 ether"))
    # Current State ACTIVE correspond to 0
    assert guess_number.currentState() == 0


def test_guess_right_number(guess_number):
    pre_contract_balance = guess_number.getBalance()
    pre_guesser_balance = accounts[1].balance()
    guess_number.guessNumber(accounts[1].address, 42, {"from": accounts[1], "value": "1 ether"})

    assert guess_number.getBalance() == Wei("0 ether")
    assert accounts[1].balance() == (pre_guesser_balance + pre_contract_balance)
    # Current State COMPLETE correspond to 1
    assert guess_number.currentState() == 1
