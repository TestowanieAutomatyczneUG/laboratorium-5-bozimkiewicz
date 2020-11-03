import unittest

from sample.zad03 import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    def test_print_one_line(self):
        self.assertEqual(self.temp.one_line(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_print_section(self):
        self.assertEqual(self.temp.section(1, 3), ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.', 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.', 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'])

    def test_print_whole_song(self):
        self.assertEqual(self.temp.whole_song(), ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
                     'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                     'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'])

    @unittest.skip('Solution not added')
    def test_disallow_number_of_verse_negative(self):
        with self.assertRaises(ValueError):
            self.temp.one_line(-1)

    @unittest.skip('Solution not added')
    def test_disallow_bigger_number_of_verse(self):
        with self.assertRaises(ValueError):
            self.temp.one_line(15)

    @unittest.skip('Solution not added')
    def test_disallow_bigger_second_number_of_verse(self):
        with self.assertRaises(ValueError):
            self.temp.section(1, 15)

    @unittest.skip('Solution not added')
    def test_disallow_first_verse_bigger_than_second(self):
        with self.assertRaises(ValueError):
            self.temp.section(3, 1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
