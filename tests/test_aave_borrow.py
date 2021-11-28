from scripts.aave_borrow import get_asset_price, get_account, get_lending_pool, approve_erc20
from brownie import config, network, config

def test_get_asset_price():
    price_feed_address = config["networks"][network.show_active()]["weth_token"]
    asset_price = get_asset_price(price_feed_address)
    assert asset_price > 0

def test_get_lending_pool():
    lending_pool = get_lending_pool()
    assert lending_pool is not None

def test_approve_erc20():
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 100000000000000000
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    assert tx 