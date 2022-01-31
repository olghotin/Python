import names

def r_name(u_name):

    result = 'hello, ' + u_name
    print(result)

for i in range(0, 10):
    user_name = names.get_full_name()

    r_name(user_name)