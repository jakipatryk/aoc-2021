import fileinput


# Part 1

commands = list(map(lambda x: ((x.rstrip().split(' ')[0], int(x.rstrip().split(' ')[1]))), fileinput.input()))

x_position = sum(command[1] for command in commands if command[0] == 'forward')

y_position = sum(-command[1] if command[0] == 'up' else command[1] for command in commands if command[0] != 'forward')

print(x_position * y_position)

# Part 2

aim = 0
x_position = 0
y_position = 0

for command, value in commands:
    if command == 'forward':
        x_position += value
        y_position += value * aim
    elif command == 'up':
        aim -= value
    else:
        aim += value

print(x_position * y_position)