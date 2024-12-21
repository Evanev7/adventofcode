from pathlib import Path


with open(f"{Path(__file__).parent.resolve()}/019.txt") as file:
    data = file.read().strip()
    #data = \
    """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

    inputs, outputs = data.split("\n\n")
    outputs = outputs.split("\n")
    inputs = inputs.split(", ")
    print(len(inputs), len(outputs))

    made = set()
    for output in outputs:
        builders = set([""])
        while builders != set():
            new_builders = set()
            for builder in builders:
                for inp in inputs:
                    part = builder + inp
                    if part == output:
                        made.add(output)
                        builders = set()
                    if part == output[:len(part)]:
                        new_builders.add(part)
            builders = new_builders
    print(len(made))