#storing questions
quiz = quiz = {
    "What is 2 + 2?": "4",
    "What is the capital of South Africa?": "Pretoria",
    "What language is used for data analysis?": "Python"
}

#Basic quiz engine
score = 0 

for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct")
        score += 1
    else:
        print("Wrong! Answer is:", answer)

print("\nFinal Score:", score, "/", len(quiz))

#Add feedback system
percentage = (score / len(quiz)) * 100

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Keep practicing!")