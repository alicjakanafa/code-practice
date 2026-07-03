from decimal import Decimal, ROUND_HALF_UP

def total_with_vat(prices):
    penny = Decimal("0.01")
    vat_rate = Decimal("1.20")

    line_totals = [
        (Decimal(str(price)) * vat_rate).quantize(penny, rounding=ROUND_HALF_UP)
        for price in prices
    ]

    return sum(line_totals).quantize(penny, rounding=ROUND_HALF_UP)
prices = [1.13, 1.13, 1.13, 4.27, 8.88]
print(total_with_vat(prices))
print(0.1 + 0.2)