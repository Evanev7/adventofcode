from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/005.txt") as file:
    data = file.read()

    # Data formatting
    raw_rules, prints = [i.split("\n") for i in data.split("\n\n")]
    inverse_rules = {}
    rules = {}
    for i in raw_rules:
        pre, post = int(i.split("|")[0]), int(i.split("|")[1])
        if post in inverse_rules.keys():
            inverse_rules[post].add(pre)
        else:
            inverse_rules[post] = set([pre])
        # Is there a default implementation of this?
        # Or like a better data structure?
        if pre in rules.keys():
            rules[pre].add(post)
        else:
            rules[pre] = set([post])

    prints = [[int(j) for j in i.split(",")] for i in prints]

    tot = 0
    for line in prints:
        broke = False
        # Hot pages considered harmful considered harmful
        while True:
            hot = set()
            for i, page in enumerate(line):
                # If we find a successor page, make it's predecessors hot. We're also going to mark the index, so we can recover that information for later.
                if page in inverse_rules.keys():
                    hot = hot.union(inverse_rules[page])
                if page in hot:
                    # A disallowed page has been found!
                    broke = True
                    # Let's find the offending page
                    for maybe_offending_page in rules[page]:
                        if maybe_offending_page in line[:i]:
                            # Found it! Let's put page before it then return.
                            line.remove(page)
                            line.insert(line.index(maybe_offending_page), page)
                            break
                    break
            else:
                if broke:
                    tot += line[len(line) // 2]
                broke = False
            if not broke:
                # lmao
                break

    print(tot)
