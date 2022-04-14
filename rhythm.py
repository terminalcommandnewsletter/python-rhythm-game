import time

tune = [{"W":4},{"A":2},{"S":3},{"D":3},{"W":4},{"A":2},{"S":3},{"D":3},{"W":2},{"A":3},{"S":2},{"D":3},{"W":2},{"A":3},{"S":2},{"D":3}]
score = 0

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
        print("Score: " + str(int(score)))
        exit()
    elif instruction.upper() != list(each.keys())[0] or time_taken > 3:
        print("You lost!", instruction.upper(), list(each.keys())[0], time_taken)
        exit()
    else:
        if time_taken < 1:
            print(f"COOL! Time taken: {time_taken} seconds")
            score = score + 100 // time_taken
        elif time_taken > 1 and time_taken < 3:
            print(f"IMPRESSIVE! Time taken: {time_taken} seconds")
            score = score + 60 // time_taken
        else:
            pass
        print("=" * 50)
        print("=" * 50)
    print("Score: " + str(int(score)))
