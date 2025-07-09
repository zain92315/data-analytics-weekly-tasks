print("cmd calulator")

history=[]
while True:
    print("operations: +, -, *, /, ^, %, type history to view calculation history and exit for leaving")
    exp=input("Enter expression for calculation like (2 * 2)").strip()


    if exp.lower() == "exit":
        break
    elif exp.lower() == "history":
        if history:
            print("\nCalculation History:")
            for entry in history:
                print(entry)
        else:
            print("No calculations yet.")
        continue
    try:
        parts=exp.split()
        if len(parts) != 3:
            raise ValueError("Invalid input format. Use format: num1 operator num2")

        num1,operator,num2=parts
        num1=float(num1)
        num2=float(num2)
        result=0
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '%':
            result = num1 % num2
        else:
            raise ValueError(f"Unsupported operator: {operator}")

        history.append(f"{num1} {operator} {num2} = {result}")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error:{e}")
        
