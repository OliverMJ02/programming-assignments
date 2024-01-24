# solution cell
### BEGIN SOLUTION


def greetings(sal: str, fn: str, ln: str, age: int, loc: str) -> str:
    sal = sal.capitalize()
    fn = fn.capitalize()
    ln = ln.capitalize()
    loc = loc.capitalize()
    return f"Hello, World! I'm {sal} {fn} {ln}, age {age}.\nI'm currently in {loc}."


### END SOLUTION
