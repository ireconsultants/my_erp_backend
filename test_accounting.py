from accounting import calculate_vat, calculate_total

def test_vat_calculation():
    # If subtotal is 1000 and VAT is 17%, VAT should be 170
    assert calculate_vat(1000, 17) == 170.0
    # If subtotal is 500 and VAT is 5%, VAT should be 25
    assert calculate_vat(500, 5) == 25.0

def test_total_with_discount_and_vat():
    # Subtotal: 1000, Discount: 100, VAT: 17% (on gross)
    # Expected: (1000 - 100) + 170 = 1070
    assert calculate_total(1000, 100, 17) == 1070.0

def test_negative_amounts():
    import pytest
    # Ensure it throws an error if someone enters a negative number
    with pytest.raises(ValueError):
        calculate_vat(-100, 17)
