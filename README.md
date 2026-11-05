# 🎯 AI Placement Preparation Assistant

An AI-powered interview preparation application that helps candidates prepare for technical interviews by generating role-specific questions, detailed model answers, practical examples, and follow-up questions.

Built using **Python, Streamlit, LangChain, Groq API, and Pydantic**, powered by the **`openai/gpt-oss-20b`** model.

## 🚀 Features

- **Role-Based Preparation:** Choose from different technical job roles.
- **Experience-Level Selection:** Generate questions for freshers and experienced candidates.
- **Custom Difficulty:** Select Easy, Medium, or Hard difficulty.
- **AI-Generated Questions:** Generate interview-oriented technical questions.
- **Detailed Model Answers:** Get technically accurate, interview-ready answers.
- **Beginner-Friendly Explanations:** Understand concepts through simple explanations.
- **Practical Examples:** Explore real-world and coding examples.
- **Important Keywords:** Identify technical terms to remember.
- **Follow-up Questions:** Prepare for deeper interviewer questions.
- **Structured Output:** Validate generated responses using Pydantic.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| LangChain | LLM integration and prompt management |
| Groq API | LLM inference |
| GPT-OSS-20B | AI model |
| Pydantic | Structured output validation |
| python-dotenv | Environment variable management |

## 🏗️ Project Structure

```text
AI-Placement-Preparation-Assistant/
│
├── app.py
├── generator.py
├── prompts.py
├── schemas.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rutuja1918/AI-Placement-Preparation-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd AI-Placement-Preparation-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from [Groq Console](https://console.groq.com/keys).

**Important:** Never share or upload your actual API key to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## 🤖 Model Information

This project uses:

**Model:** `openai/gpt-oss-20b`

**Provider:** Groq API

The model generates structured technical interview preparation content based on the selected job role, experience level, difficulty, and number of questions.

## 💡 How It Works

1. Select a technical job role.
2. Choose your experience level.
3. Select the interview difficulty.
4. Choose the number of questions.
5. Generate interview questions using the AI model.
6. Explore model answers, explanations, practical examples, keywords, and follow-up questions.

## 🎯 Project Objective

The objective of this project is to make technical interview preparation more accessible and structured by providing personalized, AI-generated interview practice for candidates.

## 👩‍💻 Author
Rutuja

BE Information Technology Student

GitHub Profile:https://github.com/Rutuja1918

⭐ If you find this project useful, consider giving it a star!
