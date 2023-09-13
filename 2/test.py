for row in range(5):
    for col in range(5):
        print(f"col{col}", end="")
    print(f"row{row}")
# col0col1col2col3col4row0
# col0col1col2col3col4row1
# col0col1col2col3col4row2
# col0col1col2col3col4row3
# col0col1col2col3col4row4

print()

for row in range(5):
    print(f"row{row}",end="")
    for col in range(5):
        print(f"col{col}", end="")
    print()
# row0col0col1col2col3col4
# row1col0col1col2col3col4
# row2col0col1col2col3col4
# row3col0col1col2col3col4
# row4col0col1col2col3col4