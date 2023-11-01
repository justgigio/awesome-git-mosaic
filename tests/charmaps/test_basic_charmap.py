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

    def test_pixel(self):
        charmap = BasicCharmap()
        assert charmap.is_pixel(CHARMAP_PIXEL)
