from collections import defaultdict

# (asin, mont) -> ave. price

def parse_month(date_str: str) -> str:
    parse = date_str.split("/")
    
    if len(parse) != 3:
        raise ValueError("Invalid date")
    
    month, _day, year = parse
    
    if len(year) == 2:
        year = "20" + year
        
    return f"{year}-{month.zfill(2)}"

def average_price_per_asin_per_month(upc_records: list[tuple[str, str, float]], upc_to_asin: dict[str, str]) -> dict[tuple[str, str], float]:
    aggregation = defaultdict(lambda: [0.0, 0])
    
    for upc, date_str, price in upc_records:
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        if upc not in upc_to_asin:
            continue
        
        asin = upc_to_asin[upc]
        month = parse_month(date_str)
        
        key = (asin, month)
        
        aggregation[key][0] += price
        aggregation[key][1] += 1
        
    result = {}
    
    for key, (total_price, count) in aggregation.items():
        result[key] = total_price / count
        
    return result
        
        
def run_tests():
    upc_to_asin = {
        "UPC1": "ASIN1",
        "UPC2342": "ASIN2",
    }

    records = [
        ("UPC1", "10/12/10", 1.0),
        ("UPC1", "10/13/10", 2.0),
        ("UPC1", "10/13/10", 1.0),
        ("UPC2342", "10/13/10", 7.0),
    ]

    result = average_price_per_asin_per_month(records, upc_to_asin)

    expected = {
        ("ASIN1", "2010-10"): 4.0 / 3,   # (1+2+1)/3
        ("ASIN2", "2010-10"): 7.0,
    }

    for key, exp in expected.items():
        got = result.get(key)
        status = "PASS" if got is not None and abs(got - exp) < 1e-9 else "FAIL"
        print(f"[{status}] {key} -> got {got}, expected {exp}")

    # 매핑 없는 UPC는 결과에 없어야 함
    extra = [k for k in result if k not in expected]
    print(f"[{'PASS' if not extra else 'FAIL'}] no unexpected keys: {extra}")


run_tests()
