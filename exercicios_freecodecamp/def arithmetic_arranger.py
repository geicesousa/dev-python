def arithmetic_arranger(problems, show_answers=False):
    print(problems)
    if len(problems) > 5:
        print('Error: Too many problems.')
 
    for e in problems:  
        operator = e.find('/')
        operator2 = e.find('*')

        if operator != -1 or operator2 != -1 :
            print('Error Operator must be "+" or "-".')

        print(e[0])
        print(e[2])      
        
        print(e)
        print(e)     

      

    # for p in problems:
    print()
    print((problems[0].replace(' ', ',')))
    print('-----')
    print((problems[2].split()))
    # return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')