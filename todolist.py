print("To do list")
print("Select what to do:")
print("1.Add\n2.Delete\n3.Exit")
task=[]

while True:
    try:
        n=int(input("Enter the choice:"))
        if n==3:
            print("Exit is suceess")
            break

        if 0<n<=3:
            if n==1:
                value=input("Enter the task:")
                task.append(value)
                print(task)
            elif n==2:
                task.pop()
                print(task)
            else:
                print("Enter proper choices")
        else:
            print("Between 1-3")
    except:
        print("Enter properly")
                
                    
