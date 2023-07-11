https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
https://code-maven.com/ansi-command-line-colors-with-python


# 256 Colors

The following escape codes tells the terminal to use the given color ID:

| ESC Code Sequence | Description |
|-|-|
| ESC[38;5;{ID}m | Set foreground color. |
| ESC[48;5;{ID}m | Set background color. |


0 - 256



```python
black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"

color = f'{red} --->  una frase'
print(color)
```
