import unittest
from day3 import common, priority, sum_of_priorities, group_rucksacks, group_common, sum_of_group_badges

rucksacks = (("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
 ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
 ("PmmdzqPrVvPwwTWBwg", "P"),
 ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
 ("ttgJtRGJQctTZtZT", "t"),
 ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"))

raw_rucksacks = [f[0] for f in rucksacks]

groups = (("vJrwpWtwJgWrhcsFMMfFFhFp"),
 ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
 ("PmmdzqPrVvPwwTWBwg")),(
 ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
 ("ttgJtRGJQctTZtZT"),
 ("CrZsJsPPZsGzwwsLwLmpwMDw"))


class MyTestCase(unittest.TestCase):
	def test_commons(self):
		for rck in rucksacks:
			self.assertEqual(common(rck[0]), rck[1])
			
	def test_priorities(self):
		self.assertEqual(priority("a"),  1)
		self.assertEqual(priority("z"), 26)
		self.assertEqual(priority("A"), 27)
		self.assertEqual(priority("Z"), 52)
		
	def test_priority_totals(self):
		self.assertEqual(sum_of_priorities(raw_rucksacks), 157)
		
	def test_grouping(self):
		sliced_groups = group_rucksacks(raw_rucksacks)
		self.assertEqual(sliced_groups[0], groups[0])
		self.assertEqual(sliced_groups[1], groups[1])
	
	def test_group_common(self):
		sliced_groups = group_rucksacks(raw_rucksacks)
		self.assertEqual(group_common(sliced_groups[0]), "r")
		self.assertEqual(group_common(sliced_groups[1]), "Z")
		
	def test_sum_group_badge_values(self):
		self.assertEqual(sum_of_group_badges(raw_rucksacks), 70)




if __name__ == '__main__':
	unittest.main()
