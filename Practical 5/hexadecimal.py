COLORS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
          "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
          "aquamarine4": "#458b74", "azure1": "#f0ffff"}

color = input("Enter color name: ")
while color != "":
    if color in COLORS:
        print("Color code for", color, "is", COLORS[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ")
