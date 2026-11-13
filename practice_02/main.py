def tasks_per_hour(tasks, hours):
    return tasks / hours
assert tasks_per_hour(18, 3) == 6.0
assert tasks_per_hour(10, 2) == 5.0
words = ["мяч", "ракетка", "велосипед"]
sorted_words = sorted(words)
assert sorted_words == ["велосипед", "мяч", "ракетка"]
print("Все проверки пройдены")
print(tasks_per_hour(18, 3))
print(sorted_words)