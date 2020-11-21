var_dict = dict()

def asign(user):
    global var_dict
    val = [i.strip() for i in user.split('=')]
    if len(val)!=2:
        print('Invalid assignment')
    else:
        if val[0].isalpha():
            if val[1].isdigit():
                    var_dict[val[0]]=int(val[1])
            elif val[1].isalpha():
                if val[1] in var_dict:
                    var_dict[val[0]] = var_dict[val[1]]
                else:
                    print('Unknown variable')
            else:
                print('Invalid assignment')
        else:
            print('Invalid identifier')

def variable(user):
    global var_dict
    if user in var_dict:
        print(var_dict[user])
    else:
        print('Unknown variable')

def solve(user):
    global var_dict
    print(eval(user,var_dict))

def check(user):
    if '=' in user:
        asign(user)
    elif user=="":
        pass
    elif '+' in user or '-' in user:
        solve(user)
    elif '/' in user:
        if user == '/exit':
            print('Bye!')
            return 1
        elif user == '/help':
            print('The program performs basic mathematical operations on numbers')
        else:
            print('Unknown command')
    elif len(user.split())==1:
        variable(user)
    return 0

while check(input())!=1:
    pass