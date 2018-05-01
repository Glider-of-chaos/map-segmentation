import math
import unittest
from map_segmentation import *

class TestMapSegmentation(unittest.TestCase):
    
    def test_init_int_order_by_1st_preserved(self):
        g_line = GeoLine((0,1), (1, 0))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((0, 1), (1, 0))")

    def test_init_int_order_by_1st_swapped(self):
        g_line = GeoLine((1, 0), (0,1))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((0, 1), (1, 0))")
    
    def test_init_int_order_by_2nd_preserved(self):
        g_line = GeoLine((1, 0), (1,1))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((1, 0), (1, 1))")
    
    def test_init_int_order_by_2nd_swapped(self):
        g_line = GeoLine((1, 1), (1,0))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((1, 0), (1, 1))")
    
    def test_init_float_order_by_1st_preserved(self):
        g_line = GeoLine((59.9960746,1.28), (59.9960747, 0.7))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((59.9960746, 1.28), (59.9960747, 0.7))")

    def test_init_float_order_by_1st_swapped(self):
        g_line = GeoLine((60.3250672, 0.2), (60.3250671,1.33))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((60.3250671, 1.33), (60.3250672, 0.2))")
    
    def test_init_float_order_by_2nd_preserved(self):
        g_line = GeoLine((1.3218950, 59.9644748), (1.3218950,59.9644749))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((1.321895, 59.9644748), (1.321895, 59.9644749))")
    
    def test_init_float_order_by_2nd_swapped(self):
        g_line = GeoLine((30.2555953, 59.9647746), (30.2555953,59.9647745))
        g_line_str = g_line.__str__()
        self.assertEqual(g_line_str, "((30.2555953, 59.9647745), (30.2555953, 59.9647746))")

    def test_slope_01(self):
        g_line = GeoLine((3.9616641, 5.5348993), (1.9616641, 3.5348993))
        slope = g_line.slope()
        self.assertEqual(slope, 1)

    def test_slope_02(self):
        g_line = GeoLine((3.2018704, 1.2320616), (1.7426647, -0.6233884))
        slope = round(g_line.slope(), 7)
        self.assertEqual(slope, 0.786443)

    def test_slope_const_lat_01(self):
        g_line = GeoLine((2.3256611, 12.97), (2.3256611, 3.53489))
        slope = g_line.slope()
        self.assertEqual(slope, 0)

    def test_slope_const_lon_01(self):
        g_line = GeoLine((2.3256611, 1.129437), (11.638641, 1.129437))
        slope = g_line.slope()
        self.assertTrue(math.isnan(slope))

    def test_lat_simple_01(self):
        g_line = GeoLine((43.6159712, 36.6451906), (27.8863884, 79.4646098))
        lon = 65.0125803
        lat = round(g_line.lat(lon), 7)
        self.assertEqual(lat, 33.1952973)

    def test_lat_simple_02(self):
        g_line = GeoLine((-11.8248652, -6.2762962), (-27.554448, -16.5669387))
        lon = -10.3030693
        lat = round(g_line.lat(lon), 7)
        self.assertEqual(lat, -17.9799193)

    def test_lat_const_lat_01(self):
        g_line = GeoLine((-5.8003561, 1.0096977), (-5.8003561, 0.05478))
        lon = 3.80924
        lat = round(g_line.lat(lon), 7)
        self.assertEqual(lat, -5.8003561)

    def test_lat_const_lon_01(self):
        g_line = GeoLine((-37.9665447, 7.9132985), (-36.9248352, 7.9132985))
        lon = 3.80924
        lat = round(g_line.lat(lon), 7)
        self.assertTrue(math.isnan(lat))

    def test_intersects_general_01(self):
        g_line_01 = GeoLine((4.782038, 2.0254964), (-0.0822909, 5.0007656))
        g_line_02 = GeoLine((2.722226, 3.053882), (1.26302, 2.6541794))
        self.assertFalse(g_line_01.intersects(g_line_02))
    
    def test_intersects_general_02(self):
        g_line_01 = GeoLine((10.8774381, -1.5397387), (5.539708, -2.8001155))
        g_line_02 = GeoLine((9.058726, -3.4287985), (10.5896516, -0.8460996))
        self.assertTrue(g_line_01.intersects(g_line_02))
    
    def test_intersects_general_03(self):
        g_line_01 = GeoLine((-4.68627214, -0.389677), (-6.25988931, 1.337293))
        g_line_02 = GeoLine((-5.72469, 0.219503), (-3.7063022, 0.74454064))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_intersects_T_cross_04(self):
        g_line_01 = GeoLine((-4.68627214, -0.389677), (-6.25988931, 1.337293))
        g_line_02 = GeoLine((-5.296469, 0.27998503), (-3.7063022, 0.74454064))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_find_sections_complex(self):
        g_line = GeoLine((0.0265972, 0.0135786), (-0.0175864,-0.0044862))
        g_line_sections = g_line.find_sections()
        self.assertEqual(g_line_sections, [(-0.02, -0.01), (-0.01, -0.01), (-0.01, 0.0), (0.0, 0.0), (0.01, 0.0), (0.01, 0.01), (0.02, 0.01)])
