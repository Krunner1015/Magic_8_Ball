import random
Response = ["It is certain", "Answer hazy, try again", "Don’t count on it", "It is decidedly so", "Ask again later", "No", "Without a doubt", "Better not tell you now", "My sources say no", "Yes definitely", "Cannot predict now", "Outlook not so good", "You may rely on it", "Concentrate and ask again",	"Very doubtful", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]

while True:
    question = input("Enter your question here (or type exit to quit): ")
    a=random.randint(0, len(Response) - 1)
    if question.lower() == "exit":
        quit()
    else:
        print(Response[a])