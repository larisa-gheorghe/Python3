import requests
from random import randint
import pyfiglet
from termcolor import colored

url = "https://icanhazdadjoke.com/search"
header = pyfiglet.figlet_format("Dad Joke 3000", font="standard")
header = colored(header, color="magenta")
print(header)
topic = input("Let me tell you a joke! Give me a topic: ")


response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={
        "term":topic
    }
).json()
search = response["results"]
if len(search) == 0:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
elif len(search) == 1:
    print(f"I've got one joke about {topic}. Here it is:\n{search[0]['joke']}")
else:
    num = randint(0,len(search)-1)
    print(f"I've got {len(search)} jokes about {topic}. Here's one:\n{search[num]['joke']}")