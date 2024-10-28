# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
steps = {}
def player(prev_play, opponent_history=[]):
	if prev_play != "":
		opponent_history.append(prev_play)
	
	n = 3

	guess = "R"
	if len(opponent_history) > n:
		pattern = "".join(opponent_history[-n:])
		move = "".join(opponent_history[-(n + 1):])
		if move in steps.keys():
			steps[move] += 1
		else:
			steps[move] = 1
		
		next_patterns = [f"{pattern}R", f"{pattern}P", f"{pattern}S"]

		for pat in next_patterns:
			if pat not in steps.keys():
				steps[pat] = 0
		
		next_move = max(next_patterns, key=lambda key: steps[key])[-1]
		
		if next_move == "R":
			guess = "P"
		
		if next_move == "P":
			guess = "S"

		if next_move == "S":
			guess = "R"

	return guess