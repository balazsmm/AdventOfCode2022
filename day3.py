def halves(rucksack):
	return rucksack[:(half := int(len(rucksack)/2))], rucksack[half:]

def common(rucksack):
	left, right = halves(rucksack)
	return set(left).intersection(set(right)).pop()

def priority(letter):
	raw = ord(letter)
	return raw-96 if raw > 96 else raw-38

def priority_of_common(rucksack):
	return priority(common(rucksack))

def sum_of_priorities(rucksacks):
	return sum(map(priority_of_common, rucksacks))

def group_rucksacks(rucksaks):
	return tuple(zip(*[iter(rucksaks)]*3))

def group_common(group_rucksacks):
	return set(group_rucksacks[0]).intersection(set(group_rucksacks[1])).intersection(set(group_rucksacks[2])).pop()

def group_common_priority(group_rucksacks):
	return priority(group_common(group_rucksacks))

def sum_of_group_badges(rucksacks):
	return sum(map(group_common_priority, group_rucksacks(rucksacks)))


with open("2022_day3_input", "r") as ifile:
	rucksacks = [f.strip() for f in ifile.readlines()]
	
print("Sum of priorities: {}".format(sum_of_priorities(rucksacks)))
print("Sum of group badge priorities: {}".format(sum_of_group_badges(rucksacks)))