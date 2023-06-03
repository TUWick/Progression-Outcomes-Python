# Date: 10/12/2022

progress	= 0
trailer		= 0
retriever	= 0
exclude		= 0
multiple_inputs = True
credit_list     = []
main_list       = []
dictN           = {}
main_dict       = []
credit_dict     = []


#Outcomes and Validation
while multiple_inputs == True:
    while True:
        Student_ID = input("Enter your student ID: ")
        while True:
            pass_credits = input("Please enter your credits at pass: ")
            if pass_credits.isdigit():     #returns True if all the characters are digits
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
                credit_list = ["Progress - ",pass_credits,defer_credits,fail_credits]
            elif pass_credits == 100:
                print("Progress(module trailer)")
                trailer += 1
                credit_list = ["Progress(module trailer) - ",pass_credits,defer_credits,fail_credits]
            elif fail_credits >= 80:
                print("Exclude")
                exclude += 1
                credit_list = ["Exclude - ",pass_credits,defer_credits,fail_credits]
            else:
                print("Do not progress-module retriever")
                retriever += 1
                credit_list = ["Do not progress-module retriever - ",pass_credits,defer_credits,fail_credits]
            credit_list=list(credit_list)
            main_list.append(credit_list)
            main_dict.append(Student_ID)
            credit_dict = list(credit_list)
            dictN[Student_ID] = credit_dict
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
            break
        else:
             print("Please Enter 'y' or 'q'.")
    

#Dictionary(separate program)
print("Part 4:")
x=0
for x in range(len(main_dict)):
    a = str(main_dict[x])
    b = dictN.get(a) 
    print(a,":",*b)


#https://www.w3schools.com/python/ref_string_isdigit.asp
#https://www.w3schools.com/python/ref_dictionary_get.asp

