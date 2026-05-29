def concatenate(*args, **kwargs):
    result = "".join(args)
    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result

#Test cases
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print("==========================")
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))