# solution cell
### BEGIN SOLUTION
from parse_csv_solution import parse_csv


def visualize_table() -> str:
    dct: dict[str, list[str]] = parse_csv()
    outp: str = "<table>\n    <thead>\n        <tr>"
    for key, value in dct.items():
        outp += "\n            <th>" + str(key) + "</th>"
        unused: str = str(value)
        unused += unused
    outp += "\n        </tr>"
    outp += "\n    </thead>\n    <tbody>"
    for i in range(len(dct["Name"])):
        outp += "\n        <tr>"
        for key in dct.keys():
            outp += "\n            <td>" + dct[key][i] + "</td>"
        outp += "\n        </tr>"
    outp += "\n    </tbody>\n</table>"
    return outp


### END SOLUTION
