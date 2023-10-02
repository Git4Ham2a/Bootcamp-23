num1 = int(input("Enter a number: "))

num2 = int(input("Enter another number: "))

print("Menu: ")
print("1. Add +,2. Subtract -, 3. Multiply *, 4. Divide /, 5. Square s")

choice = input("Enter the operation (1/2/3/4): ")

if choice == '1':
    result = num1 + num2 
    print({result})

elif choice == '2':
   result = num1 - num2 
   print({result}) 

elif choice == '3':
   result = num1 * num2 
   print({result}) 

elif choice == '4':
   result = num1 / num2 
   print({result}) 

else:
    print("Invalid choice.")

