import unittest
from day4 import total_contained, boundaries, is_containing, partial_overlap

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

with open("2022_day4_input", "r") as ifile:
	task_input = ifile.readlines()

def all_ascending(inp):
	return all(pair[0]<=pair[1] for line in inp for pair in boundaries(line))

class MyTestCase(unittest.TestCase):
	def test_input_slicing(self):
		self.assertEqual(len(input), 6)
		
	def test_boundaries(self):
		self.assertEqual(boundaries(input[0]), ((2,4), (6,8)))
		self.assertEqual(boundaries(input[2]), ((5, 7), (7, 9)))
		
	def test_all_sample_ascending(self):
		self.assertTrue(all_ascending(input))
		self.assertTrue(all_ascending(task_input))
		
	def test_containment_check(self):
		self.assertTrue(is_containing(boundaries(input[4])))
		self.assertTrue(is_containing(boundaries(input[3])))
		self.assertFalse(is_containing(boundaries(input[0])))
		self.assertFalse(is_containing(boundaries(input[5])))
		
	def test_part1(self):
		self.assertEqual(total_contained(is_containing, input), 2)
		
	def test_partial_overlap(self):
		self.assertTrue(partial_overlap(boundaries(input[5])))
		self.assertTrue(partial_overlap(boundaries(input[2])))
		self.assertTrue(partial_overlap(boundaries(input[3])))
		self.assertTrue(partial_overlap(boundaries(input[4])))
		self.assertFalse(partial_overlap(boundaries(input[0])))
		self.assertFalse(partial_overlap(boundaries(input[1])))
	
	def test_part_2(self):
		self.assertEqual(total_contained(partial_overlap, input), 4)


if __name__ == '__main__':
	unittest.main()
