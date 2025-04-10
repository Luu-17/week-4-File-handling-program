
while True:
    fileName = input("Please enter File Name: ")
    mode = input("Please enter mode \n w(write) \n a(append) \n r(read) \n x(exit)  : ")

    
    
    if mode == 'x':
        print("Exiting the program.")
        break

    elif mode == 'w':
       with open(fileName, mode) as file:
           data1 = file.write(input('Please enter text to be written'))
           print(data1)
           
        
    elif mode == 'a':
    
        with open(fileName, mode) as file:
            data1 = file.write(input('Please enter text to be appended:\n '))
            print(data1)
                    
       
            print("File not found, program exiting")

    
    elif mode == 'r':
        try:
                with open(fileName, mode) as file:
                    data1 = file.read()
                    print(data1)
                    break
        except FileNotFoundError:
            print('File Not found')

    
    else:
        print("Invalid mode. Use 'w', 'r', or 'a'.")
    

