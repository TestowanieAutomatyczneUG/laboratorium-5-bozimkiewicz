import unittest

from sample.zad02 import Roman


class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.temp = Roman()

    @unittest.skip("Solution not added")
    def test_1_is_a_single_i(self):
        self.assertEqual(self.temp(1), "I")

    @unittest.skip("Solution not added")
    def test_2_is_two_i_s(self):
        self.assertEqual(self.temp(2), "II")

    @unittest.skip("Solution not added")
    def test_3_is_three_i_s(self):
        self.assertEqual(self.temp(3), "III")

    @unittest.skip("Solution not added")
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.temp(4), "IV")

    @unittest.skip("Solution not added")
    def test_5_is_a_single_v(self):
        self.assertEqual(self.temp(5), "V")

    @unittest.skip("Solution not added")
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.temp(6), "VI")

    @unittest.skip("Solution not added")
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.temp(9), "IX")

    @unittest.skip("Solution not added")
    def test_20_is_two_x_s(self):
        self.assertEqual(self.temp(27), "XXVII")

    @unittest.skip("Solution not added")
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.temp(48), "XLVIII")

    @unittest.skip("Solution not added")
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.temp(49), "XLIX")

    @unittest.skip("Solution not added")
    def test_50_is_a_single_l(self):
        self.assertEqual(self.temp(59), "LIX")

    @unittest.skip("Solution not added")
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.temp(93), "XCIII")

    @unittest.skip("Solution not added")
    def test_100_is_a_single_c(self):
        self.assertEqual(self.temp(141), "CXLI")

    @unittest.skip("Solution not added")
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.temp(163), "CLXIII")

    @unittest.skip("Solution not added")
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.temp(402), "CDII")

    @unittest.skip("Solution not added")
    def test_500_is_a_single_d(self):
        self.assertEqual(self.temp(575), "DLXXV")

    @unittest.skip("Solution not added")
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.temp(911), "CMXI")

    @unittest.skip("Solution not added")
    def test_1000_is_a_single_m(self):
        self.assertEqual(self.temp(1024), "MXXIV")

    @unittest.skip("Solution not added")
    def test_3000_is_three_m_s(self):
        self.assertEqual(self.temp(3000), "MMM")


if __name__ == '__main__':
    unittest.main()