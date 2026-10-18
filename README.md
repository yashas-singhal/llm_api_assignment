# LLM API Response Generator

## Overview
This Python project reads questions from a text file, sends each question to an LLM using the Groq API, and stores the generated answers in a JSON file.

## Technologies Used
- Python
- Groq API
- Llama 3.1 8B Instant
- JSON

## Setup
1. Install dependencies using `pip install groq python-dotenv`.
2. Create a `.env` file containing `GROQ_API_KEY=your_api_key`.
3. Place your questions in `questions.txt`, one question per line.
4. Run `python llm_response_generator.py`.

## Output
The script generates `responses.json`, containing the question number, original question, and generated answer for each successful request. Any failed request is recorded with an error message.