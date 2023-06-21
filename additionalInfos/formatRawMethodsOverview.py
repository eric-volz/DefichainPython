import os

FILE_PATH = "rawMethodsOverview.txt"

with open(FILE_PATH) as input:
    with open(FILE_PATH + ".tmp", "w") as output:
        while True:
            line = input.readline()
            if line == "":
                break

            line = line + "\n"

            output.writelines(line)

with open(FILE_PATH + ".tmp") as input:
    with open(FILE_PATH, "w") as output:
        output.write(input.read())

os.remove(FILE_PATH + ".tmp")
