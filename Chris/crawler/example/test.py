with open("result", "r") as fr:
    data = fr.readlines()
    for line in data:
        line = line.strip()
        line_list = line.split()
        print line_list[0]
