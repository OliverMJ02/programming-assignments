# solution cell
### BEGIN SOLUTION
from download_csv_solution import download_csv


def parse_csv() -> dict[str, list[str]]:
    try:
        with open("person_data.csv", "rt", encoding="UTF-8") as pd_file:
            lines = pd_file.readlines()
        header = lines[0].strip().split(",")
        person_data: dict[str, list[str]] = {key: [] for key in header}
        for line in lines[1:]:
            data = line.strip().split(",")
            for i, value in enumerate(data):
                person_data[header[i]].append(value)
        return person_data
    except Exception:
        download_csv()
        return parse_csv()


### END SOLUTION
