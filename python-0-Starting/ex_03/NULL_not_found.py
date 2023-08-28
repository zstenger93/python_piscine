import math

def isNaN(value):
    return value != value

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        0: "Zero",
        '': "Empty",
        False: "Fake"
    }

    flag = 0
    type_name = type_names.get(object, "Type not Found")
    if type_name == "Type not Found":
        flag = 1

    if object == None:
        print(f"Nothing: {object} {type(object)}")
    elif object == 0 and type(object) == int:
        print(f"Zero: {object} {type(object)}")
    elif type(object) == float:
        print(f"Cheese: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {object} {type(object)}")
    elif type(object) == str and type_name != "Type not Found":
        print(f"{type(object)}: {object}")
    elif not object and type(object) == bool:
        print(f"Fake: {object} {type(object)}")
    else:
        print(f"Type not Found")
    
    if flag == 1:
        return 1
    return 0
