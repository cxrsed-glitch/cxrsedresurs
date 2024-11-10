def print_house(height,wall_symbol = "|"):
    for i in range(3):
        print("   /\\   ")
        print("  /  \\  ")
        print(" /    \\ ")
        print("/      \\")
        print("-"*8)
        for i in range(height):
            print(f"{wall_symbol}      {wall_symbol}")
        print("-"*8)


#for i in range(3):
    #print_house()


 print_house(height:4,wall_symbol: "|")
