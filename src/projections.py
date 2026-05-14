def project_next_halving(current_cycle):
    """Simple projection for next halving"""
    print(f"Current cycle: {current_cycle}")
    print("Next halving expected in ~30 days")
    print("Mint cost will double after next halving")
    return current_cycle + 1

def get_projected_supply():
    """Long term supply projection"""
    return {
        "current": 850000,
        "in_6_months": 2400000,
        "in_1_year": 5200000,
        "max": 21000000
    }