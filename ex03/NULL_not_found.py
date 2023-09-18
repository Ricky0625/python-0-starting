def NULL_not_found(object: any) -> int:
    objectType = type(object)
    objectTypeName = objectType.__name__
    prefix = ""
    suffix = ""

    if objectTypeName == "NoneType" and object == None:
        prefix = "Nothing"
    elif objectTypeName == "float" and str(object) == "nan":
        prefix = "Cheese"
    elif objectTypeName == "int" and object == 0:
        prefix = "Zero"
    elif objectTypeName == "str" and object == "":
        prefix = "Empty"
    elif objectTypeName == "bool" and object == False:
        prefix = "Fake"
    
    if prefix == "" and suffix == "":
        print("Type not found")
        return 1
    elif prefix != "" and prefix == "Nothing":
        suffix = ": " + f"None {objectType}"
    else:
        suffix = ": " + f"{object} {objectType}"

    print(f"{prefix}{suffix}")
    return 0