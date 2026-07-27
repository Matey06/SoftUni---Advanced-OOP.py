def vowel_filter(function):
    def wrapper(*args, **kwargs):
        data = function(*args, **kwargs)
        result = [el for el in data if el.lower() in 'aeiouy']
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())