"""Core rent calculation logic, adapted from the original rent_sys.py."""

def calculate_per_person(rent: int, food: int, electricity_units: int,
                         charge_per_unit: int, people: int) -> dict:
    """Return electricity cost, total expenses, and per-person share."""
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    if min(rent, food, electricity_units, charge_per_unit) < 0:
        raise ValueError("Amounts and units cannot be negative.")

    electricity_cost = electricity_units * charge_per_unit
    total_expenses = rent + food + electricity_cost

    # Preserve the original program's integer floor-division behaviour.
    per_person = total_expenses // people

    return {
        "electricity_cost": electricity_cost,
        "total_expenses": total_expenses,
        "per_person": per_person,
        "remainder": total_expenses % people,
    }
