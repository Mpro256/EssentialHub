import tkinter as tk


def add_words():
    word1 = word1_entry.get()
    word2 = word2_entry.get()
    wordspace = ('{: <1}'.format(word1))
    wordspace2 = ('{: >1}'.format(word2))
    result_label.config(
        text=f"Your combined word is ... {add(wordspace, wordspace2)}")


def add(wordspace, wordspace2):
    return (wordspace + wordspace2)


root = tk.Tk()
root.title("Word Combinations")
root.geometry("400x400")

tk.Label(root, text="Enter the first word:").pack()
word1_entry = tk.Entry(root)
word1_entry.pack()

tk.Label(root, text="Enter the second word:").pack()
word2_entry = tk.Entry(root)
word2_entry.pack()

combine_button = tk.Button(root, text="Combine Words", command=add_words)
combine_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
