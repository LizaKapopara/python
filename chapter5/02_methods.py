marks = {
    "liza": 100,
    "vrund": 80,
    "haru": 90,
    0:"liza"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"liza": 99, "liz":98})
print(marks)
print(marks.get("liza"))
print(marks.clear())