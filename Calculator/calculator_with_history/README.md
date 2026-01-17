# 🧮 History-Based Calculator (Python)

This project is a **command-line calculator** built using Python that performs arithmetic operations **without using `eval()`**.  
It supports **addition, subtraction, multiplication, and division**, and stores every calculation in a **history file** that can be viewed or cleared by the user.

---
## 📁 Project Structure
```
history_based_calculator/
├── calculator.py
├── history.txt   # Auto-created when first calculation is saved
└── README.md
```

## 🛠️ Tech Stack
- **Language:** Python  
- **Concepts Used:**  
  - Loops and conditionals  
  - String manipulation  
  - File handling  
  - Operator-based calculation logic  
  - User input handling  

---

## 🎯 Features
- Supports basic arithmetic operations: `+`, `-`, `*`, `/`
- Handles multiple numbers (e.g. `10+20+30`)
- Prevents division by zero
- Stores calculation history in a text file
- View history using `history`
- Clear history using `clear`
- Continuous execution until user exits
- Beginner-friendly CLI interface

---

## ▶️ How It Works
1. User enters a calculation (e.g. `20+10+5`)
2. Program detects the operator used
3. Expression is split and calculated step-by-step
4. Result is displayed and saved to a history file
5. User can use special commands:
   - `history` → Show previous calculations  
   - `clear` → Clear calculation history  
   - `exit` → Exit the program  

---

## 📌 Sample Usage
```text
_________Simple Calculator_______________
Enter Calculation(+,-,*,/)( use command like history, clear, exit): 20+10+5
result: 35

Enter Calculation(+,-,*,/)( use command like history, clear, exit): history
20+10+5 = 35

Enter Calculation(+,-,*,/)( use command like history, clear, exit): clear
History cleared.!

Enter Calculation(+,-,*,/)( use command like history, clear, exit): exit
Good byy
```
## 🧠 Key Python Concepts Used
- `while True` loop for continuous execution  
- Conditional branching using `if-elif-else`  
- String splitting using operators  
- File handling with `read`, `write`, and `append` modes  
- Input validation and basic error handling  
- Type conversion (`float` → `int` when applicable)  

---

## 🎓 Learning Outcomes
- Understood how calculators work internally **without using `eval()`**  
- Practiced file-based data persistence  
- Improved string processing and logical thinking  
- Built a real-world interactive CLI application  

## 👨‍💻 Author

Nitish Kumar
Aspiring Data Analyst / Data Scientist

🔗 GitHub: https://github.com/Nitishkumar50814

