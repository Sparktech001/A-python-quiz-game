# A python quiz game
questions = (("How many numbers are in binary system?"), 
             ("How many elements are on the perodic table?"), 
             ("What is the biggest mammal?"), 
             ("How many bones has the human body?"), 
             ("Which planet in the solar system is the hottest?"))
options = (("A. 2", "B. 1", "C. 9", "D. 10"), 
           ("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Dog", "B. Ostrich", "C. Elephant", "D. Whale"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),)
answers = (("A"), ("C"), ("D"), ("A"), ("B"))
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT")
        print(f"The correct answer is, {answers[question_num]}")
    question_num += 1

print ("---------YOUR SCORE IS---------")
print(score)