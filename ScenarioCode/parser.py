def read_file(file_name):
    instructions = []
    with open(file_name) as file:
        line = file.readline()
        while line != '':
            instr = line.split('|')
            instructions.append(instr)
    return instructions


def parse_file(instructions):
    for inst in instructions:
        for i in range(len(inst)):
            print(1)
            # when i = 0
            # switch statement for integer representing what functions to take
            # should know how many arguments it takes

            # for i in range(num of arguments that function takes)

            # call function with these arguments
