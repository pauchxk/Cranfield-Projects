import requests
import tkinter as tk
import time
from tkinter import scrolledtext

# API Setup
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to handle user input and display response
def ask_question():
    user_question = user_input.get()
    if not user_question.strip():
        return  # Don't send empty requests

    response_text = get_response(user_question)
    
    # Clear previous response and insert new one
    response_box.config(state=tk.NORMAL)
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, response_text)
    response_box.config(state=tk.DISABLED)
    
    user_input.delete(0, tk.END)  # Clear input box

# Function to get response from API
def get_response(user_question):

    # Set headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Set data
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {"role": "system", "content": "You are a learning assistant specializing in breaking down complex acronyms used in the defense and aerospace business, such as BAE Systems Air"},
            {"role": "user", "content": f"{user_question} (Request ID: {time.time()})"}
        ],
        "stream": False
    }

    # Send HTTP request to API
    response = requests.post(API_URL, json=data, headers=headers)

    # Interpret API response
    if response.status_code == 200:
        result = response.json()
        # If response is not empty
        if result["choices"][0]["message"]["content"] != "":
            return result["choices"][0]["message"]["content"]
        # If response is empty
        else:
            return "Error :( please try again."
    # If no response
    else:
        return f"Error: {response.status_code}"

# Tkinter GUI Setup
root = tk.Tk()
root.title("B.E.A.N.S | BAE Extreme Acronym Network Solution")
root.geometry("600x500")
root.config(bg="#343541")  # Background color similar to ChatGPT dark mode

# Color Theme
BG_COLOR = "#40414F"  # Dark gray chat bubbles
TEXT_COLOR = "#E0E0E0"  # Light text
ACCENT_COLOR = "#744DA9"  # Purple accent

# Chat display frame
chat_frame = tk.Frame(root, bg="#343541")
chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Response box (larger size)
response_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, height=12, bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
response_box.config(state=tk.DISABLED)  # Make it read-only
response_box.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# User input frame
input_frame = tk.Frame(root, bg="#343541")
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# User input box
user_input = tk.Entry(input_frame, font=("Consolas, 'Courier New', monospace", 14), bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief=tk.FLAT)
user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5, ipady=5)

# Send button
send_button = tk.Button(input_frame, text="Ask", font=("Consolas, 'Courier New', monospace", 12), bg=ACCENT_COLOR, fg="white", relief=tk.FLAT, command=ask_question)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Start GUI loop
root.mainloop()
