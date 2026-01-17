History_file = "history.txt"

def show_history():
    file =open(History_file,'r')
    lines =file.readlines()
    if len(lines)==0:
        print("NO History Record")
    else:
        for line in reversed(lines):
            print(line.strip())  
    file.close()

def clear_history():
    file =open(History_file,"w")
    file.close()
    print("History cleared.!")

def save_to_history(equation,result):
    file = open(History_file,"a")  
    file.write(equation +"="+ str(result) + "\n")
    file.close()

def calculate(user_input):
    
    parts = user_input.replace(" ","")

    allowed ="+-*/()0123456789."
    for i in parts:
        if i not in allowed:
            print('invalid input')
            return
    result = eval(parts)    


    if int(result) == result:
            result = int(result)
    
    print("result:", result)
    save_to_history(user_input, result)        


def main():
    print(" _________Simple Calculator_______________") 
    while True:
        user_input = input('Enter Calculation( +,-,*,/)( use command like history, clear, exit):')
        if user_input == "exit":
            print("Good byy")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        else:
            calculate(user_input)
main()
