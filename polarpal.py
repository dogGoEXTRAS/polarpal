import pyttsx3
import json
from difflib import get_close_matches
from christmastree import christmasTree
from musicsongs import christmasSongs
import importlib

try: 
    def load_knowledge(file_path:str) -> dict: 
        with open(file_path, 'r') as f: 
            data: dict = json.load(f)
        return data

    def save_knowledge(file_path:str, data:dict): 
        with open(file_path, 'w') as f: 
            json.dump(data, f, indent=2)

    def find_best_match(user_question:str, questions:list[str]) -> str | None:
        matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def get_answer(question:str, knowledge: dict) -> str | None:
        for q in knowledge["questions"]:
            if q["question"] == question: 
                return q["answer"]
            
    def speak(text): 
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def drawChristmasTree():
        christmasTree() 
            
    def chat_bot(): 
        knowledge:dict = load_knowledge('knowledge.json')

        print("Polar Pal: Merry Christmas!\n")
        speak("Merry Christmas!")

        print("Polar Pal: Here are several activities you can also do, and you can socialise with me as well.")
        speak("Here are several activities you can do, and you can also socialise with me as well.")

        activities = ["Christmas Tree Art", "Christmas Songs", "Cookie Game", "Gift List", "Quit"]

        for legend, activity in enumerate(activities): 
            print(f"{legend+1}: {activity}\n")
            speak(f"{legend+1}: {activity}")

        print("Polar Pal: To learn more about PolarPal A.I., visit https://doggodab.github.io")
        speak('To learn more about PolarPal A.I., visit https://doggodab.github.io')

        while True: 
            user_input = str(input("You: ")).lower()

            print("\n")

            if user_input.strip().lower() == '5': 
                break

            elif user_input.strip().lower() == "1": 
                print("Polar Pal: Sure! Here is a drawing of an exquisite Christmas tree! \n")
                speak("Sure! Here is a drawing of an exquisite Christmas tree!")
                drawChristmasTree()

            elif user_input.strip().lower() == "2": 
                print("Polar Pal: Sure! Here are the three Christmas songs you can listen to! \n")
                speak("Sure! Here are the three Christmas songs you can listen to!")
                christmasSongs()

            elif user_input.strip().lower() == "3": 
                print("Polar Pal: Sure! Here is a game for you! \n")
                speak("Sure! Here is a game for you!")
                gift_module = importlib.import_module("cookie")
                gift_module.run_game()

            elif user_input.strip().lower() == "4": 
                print("Polar Pal: Sure! Here is a gift list you can acquire from Santa!")
                speak("Sure! Here is a gift list you can acquire from Santa!")
                gift_module = importlib.import_module("giftlists")
                gift_module.run_game()

            best_match:str | None = find_best_match(user_input, [q["question"] for q in knowledge["questions"]])

            if best_match: 
                answer = get_answer(best_match, knowledge)
                print(f"Polar Pal: {answer}\n")
                speak(answer)

            else:
                print("Polar Pal: I do not know the answer!\n")
                new_answer = str(input("Type the answer or skip to skip: "))
                print("\n")

                if new_answer.strip().lower() != 'skip': 
                    knowledge["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge('knowledge.json', knowledge)
                    print("Polar Pal: Thank you for learning me a new response! I really appreciate it! \n")
except: 
    pass