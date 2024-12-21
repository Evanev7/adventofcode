from pathlib import Path

class Node:
    def __init__(self, val = ""):
        self.val = val
        self.paths_to_this_node = 1
    

with open(f"{Path(__file__).parent.resolve()}/019.txt") as file:
    data = file.read().strip()

    inputs, outputs = data.split("\n\n")
    outputs = outputs.split("\n")
    inputs = inputs.split(", ")

    tot = 0
    for i,output in enumerate(outputs):
        print(f"\rProgress {i:2}/{len(outputs)}", end = "")
        dagger = [[] for i in range(len(output))]
        for inp in inputs:
            for i in range(len(output)):
                if inp == output[i:i+len(inp)]:
                    dagger[i].append(Node(inp))

        for i in range(len(output)-1, -1, -1):
            for dag in dagger[i]:
                if i + len(dag.val) != len(output):
                    dag.paths_to_this_node = sum(child.paths_to_this_node for child in dagger[i + len(dag.val)])
                
        tot += (sum(i.paths_to_this_node for i in dagger[0]))
    print()
    print(tot)
