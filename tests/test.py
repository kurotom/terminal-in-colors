from ColorTerminal import ColorTerminal

string = "UNA FRASE"
c = ColorTerminal()
# c.print_all()
# c.find(100)
# c.find("red")
# c.find("green", exact=True)
# print("====")
# print(c.paint(string, color=2))
# print(c.paint(string, color="grey"))
# print("====")
# print(c.paint(string, 2, True, False, False, False, False, False))
# print(c.paint(string, 2, True, True, False, False, False, False))
# print(c.paint(string, 2, True, True, True, False, False, False))
# print(c.paint(string, 2, True, True, True, True, False, False))
# print(c.paint(string, 2, True, True, True, True, True, False))
# print(c.paint(string, 2, True, True, True, True, True, "slow"))
# print(c.paint(string, 2, True, True, True, True, True, "rapid"))
# print(c.paint(string, 2, True, True, True, True, True, 1))
# print(c.paint(string, 12, background="red", bold=True))
# print("---")
# print(c.paint(string, doubleunderline=True))
# print("---")
print(c.paint(string, italic=True))
print(c.paint(string, color=[17, 255, 0]))
print(c.paint(string, color="brown"))
print(c.paint(string, color=[17, 255, 0, 10]))
print(c.paint(string, background=[17, 255, 0]))