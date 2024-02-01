# solution cell
### BEGIN SOLUTION
def reverse_lower_and_upper_case(inp: list[str]) -> list[str]:
    inp.reverse()
    outp: list[str] = []
    item: str
    for item in inp:
        a: int = inp.index(item)
        print(item)
        if a % 2 == 0:
            item = item.lower()
            outp.append(item)
        else:
            item = item.upper()
            outp.append(item)
    return outp


### END SOLUTION
