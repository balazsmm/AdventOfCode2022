with open("day2_input", "r") as i_file:
	input = [l.strip().split(" ") for l in i_file.readlines()]

print(type(input))
values = {"X":1, "Y":2, "Z":3}
winners = {"A":"Y", "B":"Z", "C":"X"}
equals = {"A":"X", "B":"Y", "C":"Z"}

adjusted_round_score = {"X":0, "Y":3, "Z":6}
adjusted_values = {"A":1, "B":2, "C":3}
adjusted_winners = {"A":"B", "B":"C", "C":"A"}

score = 0
for round in input:
	score += values[round[1]]
	if winners[round[0]] == round[1]:
		score += 6
	elif equals[round[0]] == round[1]:
		score += 3

print("Score: {}".format(score))

score = 0
for round in input:
	if round[1] == "X":
		score += adjusted_values["ABC".replace(round[0], "").replace(adjusted_winners[round[0]], "")]
	elif round[1] == "Y":
		score += adjusted_values[round[0]]
	elif round[1] == "Z":
		score += adjusted_values[adjusted_winners[round[0]]]
	score += adjusted_round_score[round[1]]
	
print("Real score: {}".format(score))