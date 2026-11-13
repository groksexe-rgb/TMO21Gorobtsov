def decorator(func):
    def wrapper():
        print("Начинаем")
        result = func()
        print("Готово")
        return result
    return wrapper
@decorator
def hello():
    print("Привет!")
    return "Привет!"

hello()