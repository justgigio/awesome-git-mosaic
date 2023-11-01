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

    def test_translate_with_background(self):
        charmap = BasicCharmap()

        lines = charmap.translate('FoX', True, True)

        fox = [
            'oooooo ooo oo   o',
            'o    oo   ooo   o',
            'o    oo   oo o o ',
            'ooo  oo   oo  o  ',
            'o    oo   oo o o ',
            'o    oo   ooo   o',
            'o    o ooo oo   o'
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
