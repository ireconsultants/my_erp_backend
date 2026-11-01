def calculate_vat(subtotal: float, vat_rate: float) -> float:
    """Calculates VAT based on the subtotal and rate."""
    if subtotal < 0 or vat_rate < 0:
        raise ValueError("Subtotal and rate cannot be negative")
    return round((subtotal * vat_rate) / 100, 2)

def calculate_total(subtotal: float, discount: float, vat_rate: float) -> float:
    """Calculates final total: (Subtotal - Discount) + VAT on Gross."""
    # VAT is always calculated on the subtotal (gross), not the discounted amount
    vat = calculate_vat(subtotal, vat_rate)
    return round((subtotal - discount) + vat, 2)
