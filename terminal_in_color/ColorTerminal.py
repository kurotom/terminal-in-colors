from info_colors import ansi_colors


class ColorTerminal(object):
    """
    Class that allows the use of ANSI colors in terminal,
    using numbers or name of the color.
    """

    def __init__(self):
        self.__neutro = '\033[0;0m'
        self.__bold = '\033[1;1m'
        self.__opaque = '\033[2;2m'
        self.__italic = '\033[3;3m'
        self.__underline = '\033[4;4m'
        self.__intermitent_slow = '\033[5;5m'
        self.__intermitent_rapid = '\033[6;6m'
        self.__overline = '\033[9;9m'
        self.__doubleunderline = '\033[21;21m'
        self.__base_ansi = '\x1b[38;5;_m'
        self.__base_rbg_fg = '\x1b[38;2;R;G;Bm'
        self.__base_rbg_bg = '\x1b[48;2;R;G;Bm'

    def paint(
            self,
            string,
            color=None,
            bold=False,
            italic=False,
            underline=False,
            overline=False,
            doubleunderline=False,
            blink=False,
            background=None,
            opaque=False,
            ):
        """
        Styles the phrase as indicated and returns it.
        """
        frase = ''
        if color is None:
            frase += self.__neutro
        else:
            type_color = type(color)
            if type_color is list:
                if len(color) == 3:
                    frase += self.__set_rgb(color)
                else:
                    msg = self.__error_msg("Must be a list of 3 integers.")
                    raise ValueError(msg)
            else:
                frase += self.__set_color(color)

        if background is not None:
            frase += self.__set_bg(background)

        if bold:
            frase += self.__bold
        if italic:
            frase += self.__italic
        if underline:
            frase += self.__underline
        if overline:
            frase += self.__overline
        if doubleunderline:
            frase += self.__doubleunderline
        if blink is not None:
            if str(blink) == "slow":
                frase += self.__intermitent_slow
            elif str(blink) == "rapid":
                frase += self.__intermitent_rapid
        if opaque:
            frase += self.__opaque

        return frase + string + self.__neutro

    def clear(self):
        """
        Clear all formats.
        """
        return self.__neutro

    def print_all(self):
        """
        Print all 256 colors combionations.
        """
        string = f'\nTerminal_in_Colors - {len(ansi_colors)} colors\n'
        for i in range(0, 256):
            string += f'\x1b[38;5;{i}m' + 'Hi' + self.__neutro + " "
            if i % 20 == 0:
                string += "\n"
        print(string)

    def __set_color(self, color):
        """
        Set color, must be a string, integer, or list to RGB.
        """
        base = self.__base_ansi
        type_color = type(color)
        if type_color is str:
            color = self.__exact_scan(color)
            if color is None:
                return ""
            else:
                return base.replace("_", str(color[0][0]))

        elif type_color is int:
            return base.replace("_", str(color))

    def __set_rgb(self, list_code, background=False):
        """
        Set color using RGB.
        """
        if background:
            rgb = self.__base_rbg_bg
        else:
            rgb = self.__base_rbg_fg
        keys = ["R", "G", "B"]
        dict_rbg = dict(zip(keys, list_code))
        for k, v in dict_rbg.items():
            rgb = rgb.replace(k, str(v))
        return rgb

    def __set_bg(self, color=None):
        """
        Set background color.
        """
        if color is not None:
            tipo = type(color)
            if tipo is list:
                if len(color) == 3:
                    return self.__set_rgb(color, background=True)
                else:
                    msg = self.__error_msg("Must be a list of 3 integers.")
                    raise ValueError(msg)
            elif tipo is int:
                return f'\x1b[48;5;{color}m'
            elif tipo is str:
                clr = self.__exact_scan(color)
                if clr is None:
                    clr = self.__neutro
                else:
                    clr = clr[0][0]
                return f'\x1b[48;5;{clr}m'

    def find(self, color, exact=False):
        """
        Search for color using a string or integer, and return a list of tuples of all matches.
        Optional, exact search by string.
        """
        r = None
        if type(color) is str:
            if exact:
                r = self.__exact_scan(color)
                if r is None:
                    return None
                else:
                    return r
            else:
                r = [
                        (k, v) for (k, v) in ansi_colors.items()
                        if color.lower() in v.lower()
                    ]
        elif type(color) is int:
            r = [
                    (k, v) for (k, v) in ansi_colors.items()
                    if k == color
                ]
        return r

    def __exact_scan(self, color):
        """
        Find the exact color using a string.
        """
        result = [
                (k, v) for (k, v) in ansi_colors.items()
                if color.lower() == v.lower()
            ]
        if len(result) == 0:
            return None
        else:
            return result

    def __error_msg(self, message):
        """
        Message of error.
        """
        return self.paint(
                    string=message,
                    color="red",
                    bold=True,
                    underline=True,
                    doubleunderline=True
                )



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
print(c.paint(string, color=[17, 255, 0]))
print(c.paint(string, color="brown"))
print(c.paint(string, color=[17, 255, 0, 10]))
print(c.paint(string, background=[17, 255, 0]))
