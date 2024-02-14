# solution cell
### BEGIN SOLUTION


def write_text_with_line_numbers(inp: str) -> None:
    sl: list[str] = inp.split("\n")
    num: int = 1
    with open("text_file.txt", "w", encoding="utf-8") as f:
        for s in sl:
            if num > 1:
                f.write("\n")
            f.write(str(num) + ". " + s)
            num += 1


### END SOLUTION
