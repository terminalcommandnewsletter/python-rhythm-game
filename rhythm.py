import time
import random

tune = list("")

######## CONFIG ########
inputs = ["W","A","S","D"] # The input keys
min_length = 5 # The minimum length for randomly generated seeds including those in which length is set by users
max_length = 30 # The minimum length for randomly generated seeds including those in which length is set by users
cool_rank_maximum = 1 # Under what level should it say "COOL!"
impressive_rank_minimum = 1 # Above what level (must be below max_response_time) should it say "IMPRESSIVE!".
max_response_time = 3 # The maximum time you can take to respond after the key prompt is shown
seed_part_delimiter = "."
seed_part_properties_delimiter = "/"
########################

current_seed = ""
score = 0
counter = 0

def seedgenerator(length):
	seed = ""
	for number in range(1,length + 1):
		index = random.randint(0,3)
		time = random.randint(1,5)
		seed += f"{index}{seed_part_properties_delimiter}{time}"
		if number != length:
			seed += seed_part_delimiter
	seedparser(seed)

def seedparser(seedinput):
	seed_pieces_layer_one = seedinput.split(seed_part_delimiter)
	seed_pieces_layer_two = list("")
	for element in seed_pieces_layer_one:
		seed_pieces_layer_two.append(element.split(seed_part_properties_delimiter))
	for element in seed_pieces_layer_two:
		tune.append({inputs[int(element[0])]: int(element[1])})
	print(f"Seed: {seedinput}")

def mode_getter():
	mode = input(f"Hey! Type 1 for existing song, 2 for a custom seed, 3 for a random seed of specified length, or 4 for a random seed of random length between {min_length} and {max_length}: ")

	if mode == "1":
		song_one = [{inputs[0]:4},{inputs[1]:2},{inputs[2]:3},{inputs[3]:3},{inputs[0]:4},{inputs[1]:2},{inputs[2]:3},{inputs[3]:3},{inputs[0]:2},{inputs[1]:3},{inputs[2]:2},{inputs[3]:3},{inputs[0]:2},{inputs[1]:3},{inputs[2]:2},{inputs[3]:3}]
		for each in song_one:
			tune.append(each)
	elif mode == "2":
		seed = input("Seed: ")
		seedparser(seed)
	elif mode == "3":
		length = input("Number of instructions: ")
		if int(length) < min_length and int(length) > max_length:
			seedgenerator(int(length))
		else:
			print(f"The minimum length is {min_length} and the maximum length is {max_length}")
	elif mode == "4":
		seedgenerator(random.randint(min_length,max_length))
	else:
		print("Sorry, that was not a valid input")
		mode_getter()

mode_getter()


for each in tune:
	for i in range(1,each[list(each.keys())[0]] + 1):
		time.sleep(each[list(each.keys())[0]] // (each[list(each.keys())[0]]))
		print((' ' * (each[list(each.keys())[0]] + i)) + (list(each.keys())[0]) + ('=' * (each[list(each.keys())[0]] - i)) + "|")
	print("=" * 50)
	t_one = time.time()
	instruction = input("Key:")
	t_two = time.time()
	time_taken = t_two - t_one
	if instruction == "!stop":
		print(f"Score: {str(int(score))}")
		exit()
	elif instruction.upper() != list(each.keys())[0] or time_taken > max_response_time:
		print(f"You lost after note #{counter}! Your answer was {instruction.upper()}. The expected answer (case-insensitive) was {list(each.keys())[0]}. You took {time_taken} seconds")
		exit()
	else:
		if time_taken < cool_rank_maximum:
			print(f"COOL! Time taken: {time_taken} seconds")
			score = score + 100 // time_taken
		elif time_taken > impressive_rank_minimum and time_taken < max_response_time:
			print(f"IMPRESSIVE! Time taken: {time_taken} seconds")
			score = score + 60 // time_taken
		else:
			pass
		counter = counter + 1
		print("=" * 50)
print("Score: " + str(int(score)))
