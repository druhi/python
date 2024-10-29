sandwhich_order = ["veg sandwhich" , "bread jam mix"]
finished_order = []
while sandwhich_order:
    s = sandwhich_order.pop()
    print(f"i have made {s}")
    finished_order.append(s)
for sandwhich in finished_order:
    print(f"{sandwhich} have been made all day")