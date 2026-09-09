
# I en nästlad loop körs den inre loopen fullständigt
# för varje varv i den yttre

# I den yttre går x mellan 0 och (upp till) 4
for x in range(4):
    # För varje yttre varv går y mellan 0 och (upp till) 4
    for y in range(4):
        # Den här raden körs totalt 16 gånger
        print(f"({x},{y})")



