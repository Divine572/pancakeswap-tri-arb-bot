PancakeV3Factory = "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865"
import os
from dotenv import load_dotenv

load_dotenv()


MAINNET_URL = "https://bsc-dataseed1.binance.org/"
TESTNET_URL = "https://data-seed-prebsc-1-s1.binance.org:8545/"

URL = TESTNET_URL if os.getenv("MODE") == "DEVELOPMENT" else MAINNET_URL

PancakeV3FactoryTestNet = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"
SmartRouterV3 = "0x13f4EA83D0bd40E75C8222255bc855a974568Dd4"
SmartRouterV3TestNet = "0x9a489505a00cE272eAa5e07Dba6491314CaE3796"


BNBAddress = "0x050Ec6a7294AC024897ac73A7E725d165eB7faEb"
PrivateKey = os.getenv("PrivateKey")