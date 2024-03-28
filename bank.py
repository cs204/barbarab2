answer = (input("Приветствие: ")).lower()

if answer.startswith("здравствуйте"):
        print("$0")
elif answer.startswith("з"):
        print("$20")
elif answer.startswith("привет"):
        print("$100")

