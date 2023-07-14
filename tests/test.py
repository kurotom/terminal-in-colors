from terminal_in_colors.ColorTerminal import ColorTerminal

import unittest


class TestColorTerminal(unittest.TestCase):
    def setUp(self):
        self.c = ColorTerminal()
        self.string = "UNA FRASE"
        self.clean = '\033[0;0m'

    def test_paint(self):
        f = self.c.paint(self.string, bold=True)
        s = f'\033[0;0m\033[1;1m{self.string}{self.clean}'
        self.assertEqual(s, f)

    def test_find_find_exact(self):
        r1 = [(101, "Wheat4")]
        r2 = [(9, "Red")]
        self.assertEqual(self.c.find(101), r1)
        self.assertListEqual(self.c.find("Wheat4"), r1)
        self.assertEqual(self.c.find("red", exact=True), r2)

    def test_color_not_found(self):
        r = self.c.find("Plop", exact=True)
        self.assertEqual(r, None)

    def test_rgb_color(self):
        r = self.c.paint(self.string, color=[17, 255, 0])
        string = f'\x1b[38;2;17;255;0m{self.string}{self.clean}'
        self.assertEqual(string, r)

    def test_rgb_color_fail(self):
        e = "Integers must be between 0 to 255"
        with self.assertRaises(ValueError) as err:
            self.c.paint(self.string, color=[17, 300, 0])
        self.assertEqual(e in str(err.exception), True)

    def test_background(self):
        s = f'\x1b[0;0m\x1b[48;2;17;255;0m{self.string}{self.clean}'
        r = self.c.paint(self.string, background=[17, 255, 0])
        self.assertEqual(r, s)

    def test_background_fail_rgb(self):
        e = "Integers must be between 0 to 255"
        with self.assertRaises(ValueError) as err:
            self.c.paint(self.string, background=[17, 300, 0])
        self.assertEqual(e in str(err.exception), True)
