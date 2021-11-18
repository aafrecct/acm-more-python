
with open("data/pokemon-list.csv") as file:
    firstline = True
    for line in file.readlines():
        if firstline:
            firstline = False
            continue
        pokemon = line.strip().split(",")
        a = type(pokemon[1], (), {"index": int(pokemon[0][1:])})


