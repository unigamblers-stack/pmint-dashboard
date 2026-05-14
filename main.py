from src.config import CONTRACT_ADDRESS, RPC_URL
from src.data_fetcher import get_current_cycle, get_total_minted, get_pulse_price

print("🔥 pMINT Dashboard")
print("=" * 40)
print(f"Contract: {CONTRACT_ADDRESS}")
print(f"RPC: {RPC_URL[:25]}...")

cycle = get_current_cycle()
print(f"\nCurrent Cycle: {cycle}")

total_minted = get_total_minted()
print(f"Total Minted: {total_minted:,.0f} pMINT")