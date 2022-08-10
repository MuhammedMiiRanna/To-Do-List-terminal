# test = []
# test.append(
#     {"state": 0,
#      "toDoI": "jdhjfhdjfh"})

# test.append({
#     "state": 0,
#     "toDoI": "fsfsfsf"
# })


# for id, i in enumerate(test):
#     print("{} {}! {} ".format(id+1, i["state"], i["toDoI"]))

# def test():
#     if not len([]):
#         return
#     print("hahah")

# test()


# test = []
# test.append(
#     {"state": "WAit",
#      "toDoI": "jdhjfhdjfh"})

# test.append({
#     "state": "Done",
#     "toDoI": "fsfsfsf"
# })

# print(test[0]["state"], test[0]["toDoI"])
# print(test[1]["state"], test[1]["toDoI"])


# def test():
#     print("haha")
#     return 1
# test()


# while True:
#     try:
#         perform = int(input(">> What task to Remove!!"))
#     except ValueError as identifier:
#         print(f"  §§ Oopss {identifier} §§")
#     else:
#         print("hh bsahtek")
#         break


# test = [1, 2, 3, 5, 8]
# test.pop(2)
# print(test)


f = open("test.txt", 'r', encoding='utf-8')
test = f.readlines()
for line in test :
    print(">>>>", line)

print(type(test), test)
f.close()
