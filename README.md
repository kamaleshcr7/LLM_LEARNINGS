# Generative AI Learning 🚀

This repository contains my hands-on practice while learning Generative AI concepts as part of the **Data Science course at Besant Technologies**.

## 📚 Topics Covered

- Large Language Model (LLM) API usage
- Prompt-based text generation
- Temperature parameter in LLMs

## 🛠 Technologies Used

- Python
- Groq API
- Llama 3.1 Model

## 📂 Files in this Repository

### 1️⃣ 01_llm_api_basic.py
A basic example of connecting to the Groq API and generating a response from the LLM.

### 2️⃣ 02_temperature_parameter.py
Experiment to understand how the **temperature parameter** affects the creativity and randomness of the AI response.

Temperature values tested:
- 0 → Deterministic responses
- 0.5 → Balanced responses
- 1 → More creative responses

## 🤖 Model Used

- Llama 3.1 8B Instant

## 🌐 Platform

- Groq AI API

## ▶ How to Run the Code

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

    ```bash
    pip install -r requirements.txt

4.Add your API key in a .env file

    GROQ_API_KEY=your_api_key_here

5.Run the program

    python 01_llm_api_basic.py

    or

    python 02_temperature_parameter.py

📈 Learning Outcome

Through these experiments, I learned:

How to interact with LLM APIs

How prompts influence AI responses

How parameters like temperature control response creativity