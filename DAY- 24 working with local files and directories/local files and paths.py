# # LOCAL FILES
# with open("main_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# # this is for delete the before text and add new text, mode default takes read,
# # "w" is for write, "a" for append, "r" for read
# # you give unknown file name it will create automatically while execution
# with open("mains_file.txt", mode="a") as file:
#     file.write("\nNew,text")

# 2.directories relative path , ../ is one folder up ⬆️
with open("../../Desktop/main_file.txt") as file:
    contents = file.read()
    print(contents)