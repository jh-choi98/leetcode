from collections import defaultdict


def get_month_key(date_str: str) -> str:
    """
        I'll assume the date format is consistent, so I can extract the
        month and year directly instead of overcomplicating date parsing
    """
    parts = date_str.split("/")
    
    if len(parts) != 3:
        raise ValueError("Date must be in MM/DD/YY or MM/DD/YYYY format")
    
    month,_day, year = parts

    if len(year) == 2:
        year = "20" + year
    
    return f"{year}-{month.zfill(2)}"

def average_price_per_asin_per_month(
    upc_records: list[tuple[str, str, float]],
    upc_to_asin: dict[str, str]
) -> dict[tuple[str, str], float]:
    """
        I'll aggreate by ASIN and month, because multiple UPCs can map
        to the same ASIN and each UPC can have multiple price records
    """
    
    aggregation = defaultdict(lambda: [0.0, 0])
    
    for upc, date_str, price in upc_records:
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        """
            If the UPC is not in the mapping, I cannot know which ASIN
            it belongs to, so I'll skip it. If the interviewer wants
            strict validation I could raise an error instead
        """
        if upc not in upc_to_asin:
            continue
        
        asin = upc_to_asin[upc]
        month = get_month_key(date_str)
        
        key = (asin, month)
        
        """
            For each ASIN-month group, I'll keep the running total price
            and the number of price observations together
        """
        aggregation[key][0] += price
        aggregation[key][1] += 1
        
    """
        Once I have totals and counts, the average is totoal divided by
        count for each ASIN-month group
    """
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
