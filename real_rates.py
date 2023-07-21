from web3 import Web3
from abis import (QuoterABI, TOKENABI, ABI)



quoter_address = "0xB048Bbc1Ee6b733FFfCFb9e9CeF7375518e25997"
url = "https://bsc-dataseed1.binance.org/"


def get_contract(web3, contract_address, abi):
    return web3.eth.contract(address=contract_address, abi=abi)


def calculate_arbitrage(amount_in, amount_out, surface_obj):
    threshold = 0
    profit_loss_perc = 0
    profit_loss = amount_out - amount_in
    if profit_loss > threshold:
        profit_loss_perc = (profit_loss / amount_in) * 100

        surface_obj['realRateProfitLoss'] = float(profit_loss)
        surface_obj['realRateProfitLossPerc'] = float(profit_loss_perc)

        return surface_obj

    return {}


def get_price(factory, amt_in, trade_direction):
    web3 = Web3(Web3.HTTPProvider(url))
    address = Web3.toChecksumAddress(factory)

    pool_contract = web3.eth.contract(address=address, abi=ABI)
    token0_address = pool_contract.functions.token0().call()
    token1_address = pool_contract.functions.token1().call()
    token_fee = pool_contract.functions.fee().call()

    address_array = [token0_address, token1_address]
    token_info_array = []
    for token_address in address_array:
        contract = web3.eth.contract(address=token_address, abi=TOKENABI)
        token_symbol = contract.functions.symbol().call()
        token_name = contract.functions.name().call()
        token_decimals = contract.functions.decimals().call()
        obj = {
            'id': 'token' + str(address_array.index(token_address)),
            'tokenSymbol': token_symbol,
            'tokenName': token_name,
            'tokenDecimals': token_decimals,
            'tokenAddress': token_address
        }
        token_info_array.append(obj)

    input_token_a = ''
    input_decimals_a = 0
    input_token_b = ''
    input_decimals_b = 0

    if trade_direction == "baseToQuote":
        input_token_a = token_info_array[0]['tokenAddress']
        input_decimals_a = token_info_array[0]['tokenDecimals']
        input_token_b = token_info_array[1]['tokenAddress']
        input_decimals_b = token_info_array[1]['tokenDecimals']

    if trade_direction == "quoteToBase":
        input_token_a = token_info_array[1]['tokenAddress']
        input_decimals_a = token_info_array[1]['tokenDecimals']
        input_token_b = token_info_array[0]['tokenAddress']
        input_decimals_b = token_info_array[0]['tokenDecimals']

    if not isinstance(amt_in, str):
        amt_in = str(amt_in)
    amount_in = web3.toWei(amt_in, 'ether')

    quoter_contract = web3.eth.contract(address=quoter_address, abi=QuoterABI)

    try:
        quoted_result = quoter_contract.functions.quoteExactInputSingle(
            input_token_a,
            input_token_b,
            token_fee,
            amount_in,
            0
        ).call()
    except Exception as e:
        print(f"Error in get_price: {e}")
        return 0

    quoted_amount_out = quoted_result[0]

    output_amount = Web3.fromWei(quoted_amount_out, "ether")
    return output_amount


def get_depth(surface_rate_obj):
    amount_in = surface_rate_obj["startingAmount"]
    pair1_contract_address = surface_rate_obj['poolContract1']
    pair2_contract_address = surface_rate_obj['poolContract2']
    pair3_contract_address = surface_rate_obj['poolContract3']
    trade1_direction = surface_rate_obj['poolDirectionTrade1']
    trade2_direction = surface_rate_obj['poolDirectionTrade2']
    trade3_direction = surface_rate_obj['poolDirectionTrade3']

    print("Checking trade 1 acquired coin...")
    acquired_coin_t1 = get_price(pair1_contract_address, amount_in, trade1_direction)

    print("Checking trade 2 acquired coin...")
    if acquired_coin_t1 == 0:
        return {}
    acquired_coin_t2 = get_price(pair2_contract_address, acquired_coin_t1, trade2_direction)

    print("Checking trade 3 acquired coin...")
    if acquired_coin_t2 == 0:
        return {}
    acquired_coin_t3 = get_price(pair3_contract_address, acquired_coin_t2, trade3_direction)

    real_rate_obj = calculate_arbitrage(amount_in, acquired_coin_t3, surface_rate_obj)

    return real_rate_obj
