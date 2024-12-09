from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/005.txt") as file:
    data = file.read()

    # Data formatting
    raw_rules, prints = [i.split("\n") for i in data.split("\n\n")]
    inverse_rules = {}
    for i in raw_rules:
        pre, post = i.split("|")
        if post in inverse_rules.keys():
            inverse_rules[post].add(pre)
        else:
            inverse_rules[post] = set(pre)
    prints = [[j for j in i.split(",")] for i in prints]

    tot = 0
    for line in prints:
        # Hot pages considered harmful considered harmful
        hot = set()
        for page in line:
            # If we find a successor page, make it's predecessors hot.
            if page in inverse_rules.keys():
                hot = hot.union(inverse_rules[page])
            if page in hot:
                # A disallowed page has been found!
                break

        else:
            tot += int(line[len(line) // 2])
    print(tot)
