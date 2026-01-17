# 🧮 History-Based Eval Calculator (Python)

This project is a **command-line calculator** built using Python that supports **BODMAS expressions**, **file-based calculation history**, and **interactive user commands**.  
It evaluates complete mathematical expressions and stores results persistently in a text file.

---
## 📁 Project Structure
```
history_based_eval_calculator/
├── calculator.py
├── history.txt   # Auto-generated at runtime
└── README.md
```
## 🛠️ Tech Stack
- **Language:** Python  
- **Concepts Used:**  
  - File handling  
  - Loops and conditionals  
  - String processing  
  - Expression evaluation using `eval()`  
  - Input validation  

---

## 🎯 Features
- Supports arithmetic operations: `+`, `-`, `*`, `/`, `()`
- Evaluates full expressions (e.g. `2+3*4`, `(2+3)*4`)
- Automatically stores calculation history in a file
- View previous calculations using `history`
- Clear history using `clear`
- Continuous execution until user exits
- Beginner-friendly command-line interface

---

## ▶️ How It Works
1. User enters a mathematical expression  
2. Input is validated for allowed characters  
3. Expression is evaluated using Python’s `eval()`  
4. Result is displayed and saved to a history file  
5. User can use special commands:
   - `history` → Show past calculations  
   - `clear` → Clear history  
   - `exit` → Exit the program  

---

## 📌 Sample Usage
```text
_________Simple Calculator_______________
Enter Calculation(+,-,*,/)( use command like history, clear, exit): 10+5
result: 15

Enter Calculation(+,-,*,/)( use command like history, clear, exit): history
10+5 = 15

Enter Calculation(+,-,*,/)( use command like history, clear, exit): clear
History cleared.!

Enter Calculation(+,-,*,/)( use command like history, clear, exit): exit
Good byy

```

## 👨‍💻 Author

Nitish Kumar
Aspiring Data Analyst / Data Scientist

🔗 GitHub: https://github.com/Nitishkumar50814

