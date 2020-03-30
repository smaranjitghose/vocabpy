import random

filename = "gre_words.txt"
file = open(filename, 'r')
all_lines = file.readlines()

print("Select range of words.")
start = int(input("Start (1 to %d): "%(len(all_lines))))
end = int(input("End (%d to %d): "%(start, len(all_lines))))
all_lines = all_lines[start-1:end]

while True:

	print("\nStarting Practice with %d words."%(len(all_lines)))

	while True:
		choice = input("Normal[N] / Reverse[R] / Shuffle[S] : ").strip()

		if choice in ('N', 'n'):
			break

		elif choice in ('R','r'):
			all_lines.reverse()
			break

		elif choice in ('S','s'):
			random.shuffle(all_lines)
			break

		else:
			print("Invalid Input. Please try again.")

	print()

	correct = 0
	total = 0
	repeat = []

	for idx in range(len(all_lines)):
		line = all_lines[idx]

		line_ = line.split(':')
		word, mean = [s.strip() for s in line_]
		input("[%03d/%03d] %s"%(idx+1,len(all_lines),word))
		print(mean)

		while True:
			corr = input("Correct? [0/1] : ").strip()
			if corr in ('0', '1'):
				break

		correct += int(corr)
		total += 1

		if int(corr) != 1:
			repeat.append(line)

		while True:
			choice = input("Continue? [0/1] : ").strip()
			if choice in ('0', '1'):
				break

		print()
		if int(choice) != 1:
			break

	print("Practice Done. Score %d/%d"%(correct, total))
	
	if len(repeat) == 0:
		break

	while True:
		choice = input("Continue? [0/1] : ").strip()
		if choice in ('0', '1'):
			break

	all_lines = repeat