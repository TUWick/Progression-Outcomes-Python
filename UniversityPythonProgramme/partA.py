# Date: 07/12/2022

progress	= 0
trailer		= 0
retriever	= 0
exclude		= 0
multiple_inputs = True
credit_list     = []
main_list       = []


#Outcomes and Validation
while multiple_inputs == True:
    while True:
        while True:
            pass_credits = input("Please enter your credits at pass: ")
            if pass_credits.isdigit():  #returns True if all the characters are digits
                pass_credits = int(pass_credits)
                if pass_credits in range (0,121,20):
                    break
                else:
                    print("Out of range.")
                    print('')
            else:
                print("Integer required")
                print('')

        while True:
            defer_credits = input("Please enter your credit at defer: ")
            if defer_credits.isdigit():
                defer_credits = int(defer_credits)
                if defer_credits in range (0,121,20):
                    break
                else:
                    print("Out of range.")
                    print('')
            else:
                print("Integer required")
                print('')
                
        while True:
            fail_credits = input("Please enter your credit at fail: ")
            if fail_credits.isdigit():
                fail_credits = int(fail_credits)
                if fail_credits in range (0,121,20):
                    break
                else:
                    print("Out of range.")
                    print('')
            else:
                print("Integer required")
                print('')
                
        if pass_credits+defer_credits+fail_credits == 120:
            if pass_credits == 120:
                print("Progress")
                progress += 1
                credit_list = ["Progress - ",pass_credits,",",defer_credits,",",fail_credits]
            elif pass_credits == 100:
                print("Progress(module trailer)")
                trailer += 1
                credit_list = ["Progress(module trailer) - ",pass_credits,",",defer_credits,",",fail_credits]
            elif fail_credits >= 80:
                print("Exclude")
                exclude += 1
                credit_list = ["Exclude - ",pass_credits,",",defer_credits,",",fail_credits]
            else:
                print("Do not progress-module retriever")
                retriever += 1
                credit_list = ["Do not progress-module retriever - ",pass_credits,",",defer_credits,",",fail_credits]
            credit_list = list(credit_list)
            main_list.append(credit_list)
            break
        else:
            print("Total incorrect.")
            print('')
            
        
#Multiple Outcomes
    while True:
        multiple_inputs = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        print('')
        if multiple_inputs.lower() == 'y':  
            multiple_inputs = True
            break
        elif multiple_inputs.lower() == 'q':
            multiple_inputs = False
            print("-" * 60)

            
#Histogram
            print("Histogram")
            print("Progress ", progress , ' : ', progress  * "*" )
            print("Trailor  ", trailer  , ' : ', trailer   * "*" )
            print("Retriever", retriever, ' : ', retriever * "*" )
            print("Exclude  ", exclude  , ' : ', exclude   * "*" )
            print("")
            total = progress+trailer+retriever+exclude
            print(total,"outcomes in total.")
            print("-" * 60)
             
                 
#List(extension)
            print("Part 2:")
            for i in range(len(main_list)):
                print(*main_list[i]) #removes double quotation and brackets
            break
        else:
             print("Please Enter 'y' or 'q'.")
    

#Text File(extension)
def progression_file():
    print('')
    print("Part 3:")
    text_file = open("Volume_of_Credit.txt", 'w')
    for x in range (len(main_list)):
        for y in range(len(main_list[x])):
            str_list = str(main_list[x][y])
            text_file.write(str_list)
        text_file.write('\n')
    text_file.close()
    text_file=open("Volume_of_Credit.txt")
    file_content = text_file.read()
    print(file_content)
    text_file.close()
progression_file()

#https://www.w3schools.com/python/ref_string_isdigit.asp
