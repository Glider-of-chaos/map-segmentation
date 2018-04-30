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

    def test_find_sections_complex(self):
        g_line = GeoLine((0.0265972,0.0135786), (-0.0175864,-0.0044862))
        g_line_sections = g_line.find_sections()
        self.assertEqual(g_line_sections, [(-0.02, -0.01), (-0.01, -0.01), (-0.01, 0.0), (0.0, 0.0), (0.01, 0.0), (0.01, 0.01), (0.02, 0.01)])
