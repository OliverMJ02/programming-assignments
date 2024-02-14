# solution cell
### BEGIN SOLUTION
from datetime import datetime


def datetime_validator(inp: str) -> datetime | None:
    try:
        dl: list[str] = inp.split(", ")
        md: list[str] = dl[0].split(" ")
        m = md[0]
        d = md[1]
        y = dl[1]
        tl: list[str] = dl[2].split(":")
        hour = tl[0]
        minute = tl[1]
        second = tl[2]
        dt = datetime(
            int(y),
            datetime.strptime(m, "%B").month,
            int(d),
            int(hour),
            int(minute),
            int(second),
        )
        return dt
    except Exception:
        return None


### END SOLUTION
