import time
import json
import aiohttp
import asyncio
import arbitrage
from telegram_signal import send_signal_message


url = "https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v3-bsc"


async def retrieve_pancakeswap_information(url):
    query = """
        {
            pools(first: 500, orderBy: totalValueLockedETH, orderDirection: desc) {
                feeTier
                id
                token0Price
                token1Price
                token0 {
                    decimals
                    id
                    name
                    symbol
                }
                token1 {
                    decimals
                    id
                    name
                    symbol
                }
            }
        }
    """

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post(url, json={"query": query}) as response:
            json_dict = await response.json()
            return json_dict


async def process_pairs():
    while True:
        data = await retrieve_pancakeswap_information(url)
        pairs = data["data"]["pools"]
        structured_pairs = arbitrage.structure_trading_pairs(pairs)

        # Get surface rates
        for t_pair in structured_pairs:
            surface_rate = arbitrage.calc_triangular_arb_surface_rate(t_pair, min_rate=1.5)
            if len(surface_rate) > 0:
                print(surface_rate)
                print(2 * "\n" + 100 * "-")
                print("*************** NEW TRADE SIGNAL (Surface Rate) ✅ *******************")
                print(f' 🟢 {surface_rate["exchange"]} EXCHANGE ARBITRAGE SIGNAL')
                print(f' 🤖 {surface_rate["tradeDesc1"]}')
                print(f' 🤖 {surface_rate["tradeDesc2"]}')
                print(f' 🤖 {surface_rate["tradeDesc3"]}')
                print(f' ✅ Profit & Loss  -> {surface_rate["profitLoss"]}')
                print(f' ✅ Profit & Loss Percentage -> {surface_rate["profitLossPerc"]}%')
                print(100 * "-" + "\n")
                
                message = f"*************** NEW TRADE SIGNAL (Surface Rate) ✅ *******************\n"\
                f' 🟢 {surface_rate["exchange"]} EXCHANGE ARBITRAGE SIGNAL\n'\
                    f' ✅ Profit and Loss -> {surface_rate["profitLoss"]}\n'\
                        f' ✅ Profit and Loss Percentage -> {surface_rate["profitLossPerc"]}%\n'\
                        f' 🤖 {surface_rate["tradeDesc1"]}\n'\
                            f' 🤖 {surface_rate["tradeDesc2"]}\n'\
                            f' 🤖 {surface_rate["tradeDesc3"]}\n'\
                                    
                                            
                
                send_signal_message(message)

        await asyncio.sleep(60)


async def main():
    tasks = [process_pairs() for _ in range(5)]  # You can adjust the number of concurrent tasks here
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
