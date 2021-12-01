import fileinput

depths = list(map(lambda x: int(x.rstrip()), fileinput.input()))

# Part 1
num_of_increases = len(list(filter(lambda x: x[0] < x[1], zip(depths, depths[1:]))))
print(num_of_increases)

# Part 2
windows = [depths[i-2] + depths[i-1] + depths[i] for i in range(2, len(depths))]
num_of_increases_window = len(
	list(filter(lambda x: x[0] < x[1], zip(windows, windows[1:])))
)
print(num_of_increases_window)
