import csv
x = 0
particulers = 0
comments = ' '
y = ' '
lines = list()

# CRUD

def ask():
    '''
    asks the user about what function they want to perform
    Returns
    -------
    None.
    '''
    print('Press 1 to add expenses.')
    print('Press 2 to find an expense.')
    print('Press 3 to get statement of previous expenses.')
    print('Press 4 to delete an expense.')
    print('Press 5 to exit.')
    print('\n')
    return

def add():
    '''
    adds new expenses to the file
    Returns
    -------
    None.
    '''
    particulers = input('Enter particulers: ')
    amt = input('Enter amount: ')
    comments = input('Enter comments: ')
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'a', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([particulers, amt, comments])
    y = str(input('Add more expenses? Y/N : '))
    if y == 'Y':
        add()
    elif y == 'N':
        return

def read():
    '''
    print the previous expenses
    Returns
    -------
    None.
    '''
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def delete():
    '''
    deletes a particuler entry of expense
    Parameters
    ----------
    val : TYPE
        DESCRIPTION.
    Returns
    -------
    None.
    '''
    val = input('enter the value you want to delete : ')
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == val:
                    lines.remove(row)
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    return
    
def find():
    '''
    finds a particular expense if needed
    Parameters
    ----------
    value : TYPE
        DESCRIPTION.
    Returns
    -------
    None.
    '''
    value = input('Enter what you want to search : ')
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == value:
                    print(row)
                else :
                    print('Did not find that.')
                    break
            break
    with open(r'C:\Users\HP\Desktop\expenses.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    inp = input('Find any other expenses?  Y/N : ')
    if inp == 'Y':
        find()
    elif inp == 'N':
        return
    return

with open(r'C:\Users\HP\Desktop\expenses.csv', 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Particulers", "Amount", "Comments"])

while True:
    ask()
    x = int(input('Enter here : '))

    if x == 1:
        # add new expenses to the file named 'expenses'
        # add the expenses i.e. amount and particulers
        # append all the expenses to existing file
        add()
        print('\n')
    
    elif x == 2:
        # find an expense
        find()
        print('\n')

    elif x == 3:
        # get statement of previous expenses
        # print the file
        read()
        print('\n')
    
    elif x == 4:
        # delete a particuler expense
        delete()
        print('\n')
        
    elif x == 5:
        # quit
        print('Thank you for using splitwise!')
        print('\n')
        break