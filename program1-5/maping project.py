# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]


print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
vertical = int(position[0])
horizontal = int(position[1])

selected_row = map[vertical]
selected_row[horizontal] = "*"
print(f"{row1},\n{row2},\n{row3}")