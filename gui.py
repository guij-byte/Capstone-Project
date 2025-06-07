import tkinter as tk
from tkinter import messagebox
from predictor import Predictor
def predict_callback():
    try:
        features = {
            "func_calls": int(entry_calls.get()),
            "lib_used": int(entry_lib.get()),
            "lines_of_code": int(entry_lines.get())
        }
        predictor = Predictor()
        result = predictor.predict_vulnerabilities(features)
        messagebox.showinfo("result", f"Is there a vulnerability?: {result['vulnerable']}")
    except Exception as e:
        messagebox.showerror("False", str(e))

app = tk.Tk()
app.title("AI Code Vulnerability Predictor")
tk.Label(app, text="Number of function calls").pack()
entry_calls = tk.Entry(app)
entry_calls.pack()

tk.Label(app, text="No external libraries used (0/1)").pack()
entry_lib = tk.Entry(app)
entry_lib.pack()

tk.Label(app, text="Lines of code").pack()
entry_lines = tk.Entry(app)
entry_lines.pack()

tk.Button(app, text="Predicting vulnerabilities", command=predict_callback).pack()

app.mainloop()
