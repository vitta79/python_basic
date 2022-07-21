from questions import Questions
test=[
    "What is the capital of USA?\n(a) New York\n(b) Washington\n(c) Los Angeles\n",
    "What is the capital of Turkey?\n(a) Ankara\n(b) Istanbul\n(c) Antalya\n",
    "What is the capital of Turkmenistan?\n(a) Avaza\n(b) Ashgabat\n(c) Turkmenbashy\n",
]
questionAnswer=[
    Questions(test[0], "b"),
    Questions(test[1], "a"),
    Questions(test[2], "b")
]
def runTest(questions):
    score=0
    for question in questions:
        answer=input(str(question.question)+"Your Answer: ")
        if answer==question.answer:
            score+=1
    print("Your Score is "+str(score)+"/"+str(len(questions)))
runTest(questionAnswer)