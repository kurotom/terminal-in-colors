# How to use it

It must be installed using `pip`.

```bash
$ pip install termina-in-colors
```

Once installed, the class must be imported and initialized.

```python
# into your program

from terminal_in_color.ColorTerminal import ColorTerminal

string = "Hi"

c = ColorTerminal()

print(c.paint(string, color="red", blink="slow"))
```

Now, the methods of the class can be accessed.

Available methods:

* `paint(string, color, bold, italic, underline, overline, doubleunderline, blink, background, opaque)` - Formats the string using the available options, returns a string.
* `find(color, exact)` - Searches by color name, integer, and returns list of matches, optionally, searches for exact matches or returns None.
* `clear()` - Clear the string formatting.
* `print_all()` - Print all 256 colors.
