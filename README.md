# AAVE Borrow Scripts

## Running the script
```
brownie run scripts/aave_borrow.py --network [network name]
```

## Running the test
```
brownie test --network [network name]
```

## Features
1. Swap our ETH for WETH.
2. Deposit some ETH(WETH) into AAVE.
3. Borrow some asset with the ETH collateral then Sell that borrowed asset. (Short selling)
4. Repay everything back.
