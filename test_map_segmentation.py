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
