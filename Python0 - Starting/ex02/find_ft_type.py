def all_thing_is_obj(object: any) -> int:
    """Prints the formatted type message and returns 42."""
    
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "{} is in the kitchen"
    }
    
    if type(object) in type_map:
        if isinstance(object, str):
            print(f"{object} is in the kitchen : {type(object)}")
        else:
            print(f"{type_map[type(object)]} : {type(object)}")
    else:
        print("Type not found")

    return 42
