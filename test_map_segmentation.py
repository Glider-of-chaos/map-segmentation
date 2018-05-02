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
    
    def test_ray_intersection_general_01(self):
        g_line_01 = GeoLine((22.293647, 106.903992), (86.610163, 153.044101))
        g_line_02 = GeoLine((67.035571, 101.311252), (50.25735, 50.277495))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (83.2514661, 150.6346011))
    
    def test_ray_intersection_general_02(self):
        g_line_01 = GeoLine((-7.4177856, 7.9823959), (49.2087112, 21.2651539))
        g_line_02 = GeoLine((60.044646, 48.1802177), (29.284573, 90.1257713))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (75.2950757, 27.3841774))

    def test_ray_intersection_lat_const_03(self):
        g_line_01 = GeoLine((1.2176574, 21.4053877), (25.9151993, 11.0252614))
        g_line_02 = GeoLine((8,12.6), (8,0))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (8, 18.5548379))
    
    def test_ray_intersection_lat_const_inverted_04(self):
        g_line_02 = GeoLine((1.2176574, 21.4053877), (25.9151993, 11.0252614))
        g_line_01 = GeoLine((8,12.6), (8,0))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (8, 18.5548379))

    def test_ray_intersection_lon_const_05(self):
        g_line_01 = GeoLine((15.3561053, 29.1009986), (8.9579386, 21.9989878))
        g_line_02 = GeoLine((19.3672, 12.94929), (9.39776, 12.94929))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (0.8051102, 12.94929))
    
    def test_ray_intersection_lon_const_inverted_06(self):
        g_line_02 = GeoLine((15.3561053, 29.1009986), (8.9579386, 21.9989878))
        g_line_01 = GeoLine((19.3672, 12.94929), (9.39776, 12.94929))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        ray_inter_lat = round(ray_intersection_point[0], 7)
        ray_inter_lon = round(ray_intersection_point[1], 7)
        self.assertEqual((ray_inter_lat, ray_inter_lon), (0.8051102, 12.94929))
    
    def test_ray_intersection_parallel_07(self):
        g_line_01 = GeoLine((22.8734816, 22.8918447), (20.1303564, 16.6153532))
        g_line_02 = GeoLine((10.4842716, 6.5026147), (7.7411464, 0.2261232))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertTrue(math.isnan(ray_intersection_point))
    
    def test_ray_intersection_match_08(self):
        g_line_01 = GeoLine((1.8649518, 18.3134547), (7.3765884, 14.2709781))
        g_line_02 = GeoLine((12.888225, 10.2285015), (18.3998616, 6.1860249))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertEqual(ray_intersection_point, g_line_01)
    
    def test_ray_intersection_parallel_lat_const_09(self):
        g_line_01 = GeoLine((22.8734816, 22.8918447), (22.8734816, 16.6153532))
        g_line_02 = GeoLine((10.4842716, 6.5026147), (10.4842716, 0.2261232))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertTrue(math.isnan(ray_intersection_point))
    
    def test_ray_intersection_parallel_lon_const_10(self):
        g_line_01 = GeoLine((1.8649518, 2.818447), (22.8734816, 2.818447))
        g_line_02 = GeoLine((-1.8321716, 0.2361232), (10.4842716, 0.2361232))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertTrue(math.isnan(ray_intersection_point))
    
    def test_ray_intersection_match_lat_const_11(self):
        g_line_01 = GeoLine((22.8734816, 22.8918447), (22.8734816, 16.6153532))
        g_line_02 = GeoLine((22.8734816, 6.5026147), (22.8734816, 0.2261232))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertEqual(ray_intersection_point, g_line_01)
    
    def test_ray_intersection_match_lon_const_12(self):
        g_line_01 = GeoLine((1.8649518, 2.818447), (22.8734816, 2.818447))
        g_line_02 = GeoLine((-1.8321716, 2.818447), (10.4842716, 2.818447))
        ray_intersection_point = g_line_01.ray_intersection(g_line_02)
        self.assertEqual(ray_intersection_point, g_line_01)
    
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

    def test_intersects_lat_const_05(self):
        g_line_01 = GeoLine((1.2176574, 21.4053877), (25.9151993, 11.0252614))
        g_line_02 = GeoLine((8,22.6), (8,0))
        self.assertTrue(g_line_01.intersects(g_line_02))
    
    def test_intersects_lat_const_06(self):
        g_line_01 = GeoLine((1.2176574, 21.4053877), (25.9151993, 11.0252614))
        g_line_02 = GeoLine((1,12.6), (1,0))
        self.assertFalse(g_line_01.intersects(g_line_02))

    def test_intersects_lon_const_07(self):
        g_line_01 = GeoLine((15.3561053, 29.1009986), (8.9579386, 21.9989878))
        g_line_02 = GeoLine((19.3672, 12.94929), (9.39776, 12.94929))
        self.assertFalse(g_line_01.intersects(g_line_02))
    
    def test_intersects_lon_const_08(self):
        g_line_01 = GeoLine((15.3561053, 29.1009986), (8.9579386, 21.9989878))
        g_line_02 = GeoLine((1.3672, 22.2939279), (9.39776, 22.2939279))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_intersects_parallel_09(self):
        g_line_01 = GeoLine((22.8734816, 22.8918447), (20.1303564, 16.6153532))
        g_line_02 = GeoLine((10.4842716, 6.5026147), (7.7411464, 0.2261232))
        self.assertFalse(g_line_01.intersects(g_line_02))

    def test_intersects_match_10(self):
        g_line_01 = GeoLine((1.8649518, 18.3134547), (7.3765884, 14.2709781))
        g_line_02 = GeoLine((12.888225, 10.2285015), (18.3998616, 6.1860249))
        self.assertFalse(g_line_01.intersects(g_line_02))

    def test_intersects_match_11(self):
        g_line_01 = GeoLine((1.8649518, 18.3134547), (7.3765884, 14.2709781))
        g_line_02 = GeoLine((12.888225, 10.2285015), (7.3765884, 14.2709781))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_intersects_match_12(self):
        g_line_01 = GeoLine((1.8649518, 18.3134547), (7.3765884, 14.2709781))
        g_line_02 = GeoLine((12.888225, 10.2285015), (4.6207701, 16.2922164))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_intersects_parallel_lat_const_13(self):
        g_line_01 = GeoLine((22.8734816, 22.8918447), (22.8734816, 16.6153532))
        g_line_02 = GeoLine((10.4842716, 36.5026147), (10.4842716, 0.2261232))
        self.assertFalse(g_line_01.intersects(g_line_02))

    def test_intersects_parallel_lon_const_14(self):
        g_line_01 = GeoLine((1.8649518, 2.818447), (22.8734816, 2.818447))
        g_line_02 = GeoLine((-1.8321716, 0.2361232), (10.4842716, 0.2361232))
        self.assertFalse(g_line_01.intersects(g_line_02))

    def test_intersects_match_lat_const_15(self):
        g_line_01 = GeoLine((10.4842716, 22.8918447), (10.4842716, 16.6153532))
        g_line_02 = GeoLine((10.4842716, 36.5026147), (10.4842716, 0.2261232))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_intersects_match_lon_const_16(self):
        g_line_01 = GeoLine((1.8649518, 0.2361232), (22.8734816, 0.2361232))
        g_line_02 = GeoLine((-1.8321716, 0.2361232), (10.4842716, 0.2361232))
        self.assertTrue(g_line_01.intersects(g_line_02))

    def test_find_sections_complex(self):
        g_line = GeoLine((0.0265972, 0.0135786), (-0.0175864,-0.0044862))
        g_line_sections = g_line.find_sections()
        self.assertEqual(g_line_sections, [(-0.02, -0.01), (-0.01, -0.01), (-0.01, 0.0), (0.0, 0.0), (0.01, 0.0), (0.01, 0.01), (0.02, 0.01)])
