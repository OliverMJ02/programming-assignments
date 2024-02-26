# solution cell
### BEGIN SOLUTION
import requests


def download_csv() -> None:
    response = requests.get("http://onu1.s2.chalmers.se/datasets/assignment_06.csv")
    with open("person_data.csv", "wt", encoding="UTF-8") as pd:
        pd.write(response.text)


### END SOLUTION
