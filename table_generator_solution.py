# solution cell
### BEGIN SOLUTION


def table_generator(inp: list[str]) -> str:
    outp: str = "<table>"
    outp += "\n    <thead>"
    outp += "\n        <tr>"
    outp += "\n            <th>Index</th>"
    outp += "\n            <th>Value</th>"
    outp += "\n        </tr>"
    outp += "\n    </thead>"
    outp += "\n    <tbody>"
    num: int = 0
    for i in inp:
        num += 1
        outp += "\n        <tr>"
        outp += "\n            <td>" + str(num) + "</td>"
        outp += "\n            <td>" + i + "</td>"
        outp += "\n        </tr>"
    outp += "\n    </tbody>"
    outp += "\n</table>"
    return outp


### END SOLUTION
