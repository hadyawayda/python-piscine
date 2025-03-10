def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class '{type(object).__name__}'>")
        return 0

    if isinstance(object, float) and object != object:
        print(f"Cheese: nan <class 'float'>")
        return 0

    if object is False:
        print(f"Fake: {object} <class '{type(object).__name__}'>")
        return 0

    if object == 0 and isinstance(object, int):
        print(f"Zero: {object} <class '{type(object).__name__}'>")
        return 0

    if object == "":
        print(f"Empty: <class '{type(object).__name__}'>")
        return 0

    print("Type not Found")
    return 1
