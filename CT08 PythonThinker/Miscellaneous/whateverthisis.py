import numpy as np
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import random

# Download required NLTK resources
nltk.download('punkt')

# Sample training data (questions and answers)
data = {
    'question': [
        "Hi", "Hello", "How are you?", "What's your name?", "What do you do?", "How can I help?", "Bye", "Goodbye"
    ],
    'response': [
        "Hello!", "Hi there!", "I'm good, how about you?", "I am Chatbot.", "I am here to assist you.", "You can ask me anything.", "Goodbye!", "See you!"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df['question']
y = df['response']

# Split dataset (although in this simple case, we use the whole dataset for training)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple model using a pipeline (Combining CountVectorizer and LogisticRegression)
model = make_pipeline(CountVectorizer(), LogisticRegression())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')

# Function to interact with the chatbot
def chat():
    print("Chatbot: Hi! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = model.predict([user_input])
        print(f"Chatbot: {response[0]}")

# Start chatting
chat()
