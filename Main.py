import tkinter as tk
from tkinter import Text, Scrollbar
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Load the GPT-2 "medium" model and tokenizer
model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Create a text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Function to generate poetic text based on user input
def generate_poetry_from_input():
    user_prompt = user_input.get("1.0", tk.END)
    generated_text = generator(user_prompt, max_length=150,
                               num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)
    generated_poetry.config(state=tk.NORMAL)
    generated_poetry.delete("1.0", tk.END)
    generated_poetry.insert(tk.END, generated_text[0]['generated_text'])
    generated_poetry.config(state=tk.DISABLED)

# Create the main GUI window
root = tk.Tk()
root.title("Poetic Text Generator")

# Create a text input field
user_input = Text(root, height=5, width=40)
user_input.pack()

# Create a button to generate text
generate_button = tk.Button(root, text="Generate Poetry", command=generate_poetry_from_input)
generate_button.pack()

# Create a text display area
generated_poetry = Text(root, height=10, width=40, state=tk.DISABLED)
generated_poetry.pack()

# Start the GUI event loop
root.mainloop()
