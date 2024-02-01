# solution cell
### BEGIN SOLUTION
def age_counter(inp: str) -> dict[int, int]:
    outp: dict[int, int] = {}
    outpint = 0
    list1: list[str] = inp.split(", ")
    item1: str
    for item1 in list1:
        list2: list[str] = item1.split(" = ")
        item2: int = int(list2[1])
        if item2 in outp:
            outp[item2] += 1
            if 20 <= int(item2) <= 30:
                outpint += 1
        else:
            outp[item2] = 1
            if 20 <= int(item2) <= 30:
                outpint += 1

    # for item3 in outp.items
    print(outpint)
    return outp


### END SOLUTION
