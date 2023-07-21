
QuoterABI = [
    {
        "constant": True,
        "inputs": [
            {
                "name": "tokenIn",
                "type": "address"
            },
            {
                "name": "tokenOut",
                "type": "address"
            },
            {
                "name": "fee",
                "type": "uint24"
            },
            {
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "name": "sqrtPriceLimitX96",
                "type": "uint160"
            }
        ],
        "name": "quoteExactInputSingle",
        "outputs": [
            {
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]


ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "token0",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "token1",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "fee",
        "outputs": [
            {
                "name": "",
                "type": "uint24"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]


TOKENABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]



