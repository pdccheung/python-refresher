# *args parameters 
# the type for the args is a tuple (immutable list)

def numbers (name, *args):
    print(type(args))
    print(type(name))

numbers("Philip", 1,2,3,4,5,)


# **kwargs parameters
# the type for the key-word args is a dictionary (dict) 
def kw_args (**kwargs):
    print(kwargs)
    print(type(kwargs))

kw_args(first_key="My first name", next_key="My last name", age=28)

