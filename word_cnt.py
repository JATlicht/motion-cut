import tkinter as tk

def count_words():
    text = text_entry.get("1.0", tk.END)  # Get the input text from the text entry widget
    word_count = len(text.split())  # Split the text into words and count them
    result_label.config(text=f"Word count: {word_count}")

# Create the tkinter window
root = tk.Tk()
root.title("Word Counter")

# Create and pack widgets
instruction_label = tk.Label(root, text="Enter your sentence or paragraph:")
instruction_label.pack()

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the tkinter event loop
root.mainloop()
