import unittest
from square2 import Square2 as S2

class TestSquare2(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_load(self):
        magic_3 = [[8,1,6],[3,5,7],[4,9,2]]
        test_obj_3 = S2(3)
        test_obj_3.load(magic_3)
        self.assertListEqual(test_obj_3, magic_3)
        
    @unittest.skip
    def test__hash_(self):
        # Rotation
        test_obj_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_obj_3_rotated = S2(3, [[4,3,8],[9,5,1],[2,7,6]])
        self.assertEqual(test_obj_3._hash_(), test_obj_3_rotated._hash_())
        # Reflection
        test_obj_3_reflected = S2(3, [[4,9,2],[3,5,7],[8,1,6]])
        test_obj_3_reflected_dia = S2(3, [[6,7,2],[1,5,7],[8,3,4]])
        self.assertEqual(test_obj_3._hash_(),
                         test_obj_3_reflected._hash_())
        self.assertEqual(test_obj_3._hash_(),
                         test_obj_3_reflected_dia._hash_())
        self.assertEqual(test_obj_3_rotated._hash_(),
                         test_obj_3_reflected._hash_())
        self.assertEqual(test_obj_3_reflected_dia._hash_(),
                         test_obj_3_reflected._hash_())
               
    def test_rotate(self):
        test_obj_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_obj_3_r = S2(3, [[4,3,8],[9,5,1],[2,7,6]])
        test_obj_3.rotate()
        self.assertListEqual(test_obj_3, test_obj_3)
        
    def test_populateRandom(self):
        test_obj_3 = S2(3)
        test_obj_3.populateRandom()
        self.assertIs(type(test_obj_3[0]), list)
        self.assertIs(type(test_obj_3[0][0]), int)
        
    def test_loadFlat(self):
        flat_3 = [8,1,6,3,5,7,4,9,2]
        magic_3 = [[8,1,6],[3,5,7],[4,9,2]]
        test_obj_3 = S2(3)
        test_obj_3f = S2(3)
        test_obj_3.load(magic_3)
        test_obj_3f.loadFlat(flat_3)
        self.assertListEqual(test_obj_3, test_obj_3f)
        
    def test_getTotals(self):
        magic_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        totals = ((15, 15, 15),
                  (15, 15, 15),
                  (15, 15))
        self.assertTupleEqual(magic_3.getTotals(), totals)
        
    def test_isEmpty(self):
        magic_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        magic_4 = S2(4)
        self.assertTrue(magic_4.isEmpty())
        self.assertFalse(magic_3.isEmpty())
        
    def test_isMagic(self):
        magic = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        non_m = S2(3, [[8,1,12],[3,5,7],[4,9,2]])
        semi  = S2(3, [[1,5,9],[6,7,2],[8,3,4]])
        self.assertTrue(magic.isMagic())
        self.assertFalse(non_m.isMagic())
        
    def test_isMagic(self):
        magic = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        non_m = S2(3, [[8,1,12],[3,5,7],[4,9,2]])
        semi  = S2(3, [[1,5,9],[6,7,2],[8,3,4]])
        self.assertTrue(magic.isSemiMagic())
        self.assertFalse(non_m.isSemiMagic())
        self.assertTrue(semi.isSemiMagic())
        
    def test_reflectX(self):
        test_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_3_reflectx = S2(3, [[4,9,2],[3,5,7],[8,1,6]])
        test_3.reflectX()
        self.assertListEqual(test_3, test_3_reflectx)
        test_4 = S2(4, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        test_4_reflectx = S2(4, [[13,14,15,16],[9,10,11,12],[5,6,7,8],[1,2,3,4]])
        test_4.reflectX()
        self.assertListEqual(test_4, test_4_reflectx)
        
    def test_reflectY(self):
        test_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_3_reflecty = S2(3, [[6,1,8],[7,5,3],[2,9,4]])
        test_3.reflectY()
        self.assertListEqual(test_3, test_3_reflecty)
        test_4 = S2(4, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        test_4_reflecty = S2(4, [[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]])
        test_4.reflectY()
        self.assertListEqual(test_4, test_4_reflecty)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestSquare2)
unittest.TextTestRunner(verbosity=4).run(suite)