def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")

    if object_type == str:
        print(f"{object} is in the kitchen : {type_name}")
    else:
        print(f"{type_name} : {object_type}")

    return 42
