### BEGIN SOLUTION
def list_generator(inp: list[str]) -> str:
    outp: str = "<ul>"
    for i in inp:
        outp += "\n<li>" + i + "</li>"
    outp += "\n</ul>"
    return outp


### END SOLUTION
