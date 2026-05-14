import os
from dotenv import load_dotenv

load_dotenv()

# RPC Configuration
RPC_URL = os.getenv("RPC_URL", "https://rpc.pulsechain.com")

# Contract Addresses
CONTRACT_ADDRESS = "0xA54E7486Dc69219B6814798b30dd09e14Ee9cd10"
TOKEN_ADDRESS = "0xFf640cBd35A618Df1348D861B5e47f7eaB05b422"

# Dashboard Settings
MAX_SUPPLY = 21_000_000