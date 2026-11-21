def ticket_total(count, price=12):
    return count*price

def final_price(count, is_school_group=False):
    total=ticket_total(count)
    if is_school_group==True:
        total=ticket_total(count)*0.75
    return total

res1=final_price(3)
print(res1)

res2=final_price(4,is_school_group=True)
print(res2)

res3=ticket_total(2,price=15)
print(res3)