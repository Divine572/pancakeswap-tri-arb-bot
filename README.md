# PancakeSwap V3 Triangular Arbitrage Bot

This is a Python-based Triangular Arbitrage Bot designed to operate on the PancakeSwap V3 decentralized exchange on the Binance Smart Chain (BSC). The bot identifies potential arbitrage opportunities between three different tokens and executes trades to profit from price differences.

## Requirements

- Python 3.x
- web3.py library
- abis.py (containing contract ABIs)

## Installation

1. Install Python 3.x if not already installed.
2. Install the required Python packages:

```
pip install web3
```

3. Save the contract ABIs in a file named `abis.py`.

## Usage

1. Make sure to set the `quoter_address` and `url` variables in the code to the appropriate addresses for PancakeSwap V3 and BSC network, respectively.
2. Run the bot using the Python interpreter:

```
python your_script_name.py
```

## Bot Features

- The bot fetches trading pair information from the PancakeSwap V3 exchange using The Graph API.
- Triangular arbitrage opportunities are identified and calculated based on token prices and trading pair information.
- Arbitrage opportunities with a profit percentage above a user-defined threshold (`min_surface_rate`) are logged and displayed.

## Configuration

- The `min_surface_rate` variable in the script determines the minimum profit percentage required for a trade to be considered as an arbitrage opportunity. Modify this value according to your preference.

