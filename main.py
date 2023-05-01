print("*"*50)
print("Welcome to the 99 bottles of beer song!")
print("*"*50)
for bottles in range(99, -1, -1):
    if bottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, 99 bottles of beer on the wall...")

    elif bottles == 2:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottle of beer on the wall...")   

    elif bottles != 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall...")

    elif bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottle of beer on the wall...")
          
    print("*"*70)