import json
from openai import OpenAI

client = OpenAI(
    api_key = "YOUR_API_KEY_GOES_HERE_IM_NOT_SHARING_MINE"
)

start_message = """
Welcome to the translator 9000. Please select an input language:
1. Spanish
2. English

"""

selection = ""
input_language = ""
while selection != "1" and selection != "2":
    selection = input(start_message)

if selection == "1":
    input_language = "Spanish"
elif selection == "2":
    input_language = "English"

request_output = """
Please select an output language below.
1. Mandarin
2. French
3. Japanese

"""

input_text = input("Please enter your text in " + input_language + ": ")

selection = ""
output_language = ""
while selection != "1" and selection != "2" and selection != "3":
    selection = input(request_output)

if selection == "1":
    output_language = "Mandarin"
elif selection == "2":
    output_language = "French"
elif selection == "3":
    output_language = "Japanese"

print("Converting from", input_language, "to", output_language,"...")

system_prompt = """
You are a language translator. A user will give you an input language, an output
language, and the text they want translated. Output ONLY their translated message.
"""

user_prompt = input_language + "->" + output_language + ", my message is: " + input_text

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print("Done! Here it is: ")
print(response.choices[0].message.content)