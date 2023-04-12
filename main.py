import requests
import datetime

num_paragraphs = int(input("enter number paragraps:"))
response = requests.get(f"https://baconipsum.com/api?type=meat-and-filler&paras={num_paragraphs}")
paragraphs = response.json()
paragraphs.reverse()
num_pancetta_paragraphs = 0
for paragraph in paragraphs:
    if "Pancetta" in paragraph:
        num_pancetta_paragraphs +=1
with open("results.txt","w") as file:
    now = datetime.datetime.now()
    file.write(f"Vlad, {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Number 'Pancetta': {num_pancetta_paragraphs}\n")
    file.write("\n".join(paragraphs))