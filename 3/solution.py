import fileinput


# Part 1

numbers = list(map(lambda x: x.rstrip(), fileinput.input()))
gamma = []
epsilon = []
for i in range(len(numbers[0])):
    most_common = '0' if (sum(1 for b in numbers if b[i] == '0') >= (len(numbers) / 2)) else '1'
    least_common = '1' if most_common == '0' else '0'
    gamma.append(most_common)
    epsilon.append(least_common)

gamma_num = int(''.join(gamma), 2)
epsilon_num = int(''.join(epsilon), 2)

print(gamma_num * epsilon_num)

# Part 2
ox_numbers = numbers.copy()
for i in range(len(numbers[0])):
    most_common = '1' if (sum(1 for b in ox_numbers if b[i] == '1') >= (len(ox_numbers) / 2)) else '0'
    ox_numbers = list(filter(lambda b: b[i] == most_common, ox_numbers))
    if len(ox_numbers) == 1:
        break
ox_number = int(''.join(ox_numbers[0]), 2)

co2_numbers = numbers.copy()
for i in range(len(numbers[0])):
    most_common = '1' if (sum(1 for b in co2_numbers if b[i] == '1') >= (len(co2_numbers) / 2)) else '0'
    least_common = '1' if most_common == '0' else '0'
    co2_numbers = list(filter(lambda b: b[i] == least_common, co2_numbers))
    if len(co2_numbers) == 1:
        break
co2_number = int(''.join(co2_numbers[0]), 2)

print(ox_number * co2_number)
