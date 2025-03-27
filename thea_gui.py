import tkinter as tk
from tkinter import scrolledtext
import Zen  # Assuming Zen's chatbot logic is in the 'Zen' module

def send_message():
    user_message = entry.get()
    if not user_message.strip():
        return
    
    chat_box.insert(tk.END, "You: " + user_message + "\n", "user")
    entry.delete(0, tk.END)
    
    # Get AI response from Zen
    ai_response = Zen.chat(user_message)  # Replace with actual function call
    chat_box.insert(tk.END, "Zen: " + ai_response + "\n", "ai")

# GUI Setup
root = tk.Tk()
root.title("Zen - AI Therapist")
root.geometry("500x600")

chat_box = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat_box.pack(pady=10)
chat_box.tag_configure("user", foreground="blue")
chat_box.tag_configure("ai", foreground="green")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
