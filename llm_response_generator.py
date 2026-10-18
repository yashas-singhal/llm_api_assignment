
import os
import json
from groq import Groq
from dotenv import load_dotenv

# Loading the API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# Reading questions from the text file
with open("questions.txt", "r", encoding="utf-8") as file:
    questions = [line.strip() for line in file if line.strip()]

# Creating a list to store the results
results = []

# Sending each question to the AI model
for question_number, question in enumerate(questions, start=1):
    print(f"Processing question {question_number}: {question}")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=300
        )

        answer = response.choices[0].message.content

        results.append({
            "question_number": question_number,
            "question": question,
            "answer": answer
        })

    except Exception as error:
        print(f"Error processing question {question_number}: {error}")

        results.append({
            "question_number": question_number,
            "question": question,
            "error": str(error)
        })

# Saving all responses to a JSON file
with open("responses.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

print("All responses saved to responses.json")
