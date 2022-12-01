with open("2022_day1_input", "r") as ifile:
	input = [v.strip() for v in ifile.readlines()]

cal_per_elf, counter, last = [], 0, len(input)

while counter < last:
	single_elf_calories = []
	while counter < last and input[counter] != "":
		single_elf_calories.append(int(input[counter]))
		counter += 1
	counter += 1
	cal_per_elf.append(single_elf_calories)

total_per_elf = [sum(cpf) for cpf in cal_per_elf]

print("Top calories per elf: {}".format(max(total_per_elf)))
print("Top three calories: {}".format(sum(sorted(total_per_elf, reverse=True)[:3])))

