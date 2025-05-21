questions = [
    {
        "question":"Wie heißt die Code-Admiralin?",
        "options":["A) Ada Lovelace","B) Grace Hopper","C) Ida Rhodes","D) Adelle Goldberg"],
        "answer":"B"
    },
    {
        "question":"Wer ist der Vater der theoretischen Informatik?",
        "options":["A) Morgan Freeman","B) Steve Goldberg","C) Alan Turing","D) Terry Crews"],
        "answer":"C"
    },
    {
        "question":"Was ist Python für eine Sprache?",
        "options":["A) Kompiliert","B) Philosophiert","C) Studiert","D) Interpretiert"],
        "answer":"D"
    }
]

def run_quiz():
    print("Willkommen zu meinem Zauberer-Quiz")
    score = 0
    for questionsentry in questions:
        print(questionsentry["question"])
        for option in questionsentry["options"]:
            print(option)
        user_answer = input("Deine Antwort (A/B/C/D): ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print(" Wähle aus A, B, C, oder D.")
            user_answer = input("Deine Antwort (A/B/C/D): ").strip().upper()

        if user_answer == questionsentry["answer"]:
            print(" Richtig!\n")
            score += 1
        else:
            print(f" Falsch! Die richtige Antwort ist {questionsentry['answer']}.\n")
    
    print(f"🎉 Quiz beendet! Du hast {score} von {len(questions)} richtig.\n")
    print(" Danke fürs spielen! 👋")





run_quiz()