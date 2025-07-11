import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



def count_numbers(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)
    zero_count = sum(1 for num in numbers if num == 0)
    return positive_count, negative_count, zero_count

def process_input():
    input_text = entry.get()
    try:
        number_list = [int(num.strip()) for num in input_text.split(",")]
        update_results_and_chart(number_list)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter only integers separated by commas.")

def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        return
    try:
        with open(file_path, 'r') as file:
            content = file.read().replace("\n", ",")
            number_list = [int(num.strip()) for num in content.split(",") if num.strip()]
            entry.delete(0, tk.END)
            entry.insert(0, ", ".join(map(str, number_list)))
            update_results_and_chart(number_list)
    except Exception as e:
        messagebox.showerror("File Error", f"Error reading file:\n{e}")

def update_results_and_chart(number_list):
    positives, negatives, zeros = count_numbers(number_list)
    result_label.config(
        text=f"✅ Positive: {positives}\n🔻 Negative: {negatives}\n⭕ Zero: {zeros}"
    )
    draw_chart(positives, negatives, zeros)

def draw_chart(positive, negative, zero):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    labels = ['Positive', 'Negative', 'Zero']
    values = [positive, negative, zero]
    colors = ['green', 'red', 'gray']

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# GUI setup
root = tk.Tk()
root.title("📂 Count Numbers with File Upload")

tk.Label(root, text="Enter numbers separated by commas:", font=('Arial', 12)).pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Count Input", command=process_input, font=('Arial', 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="📁 Upload File", command=upload_file, font=('Arial', 12), bg="#FF9800", fg="white").pack(pady=5)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

chart_frame = tk.Frame(root)
chart_frame.pack(pady=10)

root.mainloop()


