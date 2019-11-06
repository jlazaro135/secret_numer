

def get_score_list(filename):
    import json
    with open(filename, "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_score(filename):
    score_list = get_score_list(filename)
    top_score = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return (top_score)

def play_game(level= "easy"):
    import random
    import datetime
    import json
    secret = random.randint(1, 30)
    attempts = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret and level == "easy":
            score_list = get_score_list("score_list.txt")
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess == secret and level == "Hard":
            score_list_hard = get_score_list("score_list_hard.txt")
            score_list_hard.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list_hard.txt", "w") as score_file:
                score_file.write(json.dumps(score_list_hard))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
