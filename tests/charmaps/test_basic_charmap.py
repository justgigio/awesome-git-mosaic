from awesome_git_mosaic.charmaps.basic.basic_charmap import BasicCharmap, CHARMAP_PIXEL


class TestBasicCharmap:

    def test_translate(self):
        charmap = BasicCharmap()

        lines = charmap.translate('FoX')

        fox = [
            'ooooo  ooo  o   o',
            'o     o   o o   o',
            'o     o   o  o o ',
            'ooo   o   o   o  ',
            'o     o   o  o o ',
            'o     o   o o   o',
            'o      ooo  o   o'
        ]

        assert lines == fox

    def test_translate_inverted(self):
        charmap = BasicCharmap()

        lines = charmap.translate('FoX', True, True)

        fox = [
            '     oo   oo ooo ',
            ' ooooo ooo o ooo ',
            ' ooooo ooo oo o o',
            '   ooo ooo ooo oo',
            ' ooooo ooo oo o o',
            ' ooooo ooo o ooo ',
            ' oooooo   oo ooo '
        ]

        assert lines == fox

    def test_translate_without_spaces(self):
        charmap = BasicCharmap()

        lines = charmap.translate('FoX', False)

        fox = [
            'ooooo ooo o   o',
            'o    o   oo   o',
            'o    o   o o o ',
            'ooo  o   o  o  ',
            'o    o   o o o ',
            'o    o   oo   o',
            'o     ooo o   o'
        ]

        assert lines == fox

    def test_pixel(self):
        charmap = BasicCharmap()
        assert charmap.is_pixel(CHARMAP_PIXEL)
