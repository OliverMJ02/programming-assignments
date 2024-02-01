# solution cell
### BEGIN SOLUTION
def mobile_number_validate(number: str) -> bool:
    isvalid: bool = False
    if number[0] == "0" and number[1] != "0":
        isvalid = bool(len(number) == 10)
    if number[0] == "4" and number[1] == "6" and number[2] != "0":
        isvalid = bool(len(number) == 11)
    if number[0] == "+" and number[1] == "4" and number[2] == "6" and number[3] != "0":
        isvalid = bool(len(number) == 12)
    return isvalid


### END SOLUTION
