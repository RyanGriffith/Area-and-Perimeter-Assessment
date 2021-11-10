# ask if area or perimeter
AreaOrPerimeter = input("Calculating area or perimeter?: ").strip().lower()
if AreaOrPerimeter != "area" or "perimeter":
    print("invalid")
else:
    # ask what shape (get shape from list if I can get it to work for once)
    shape = input("What shape?: ")
# ask the lengths of the sides in a clockwise motion? (asked multiple times according to exit code or side amount
