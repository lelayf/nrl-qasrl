import unittest

from nrl.modules.span_rep_assembly import SpanRepAssembly

class TestSpanRepAssembly(unittest.TestCase):

    def setUp(self):        
        self.assembly = SpanRepAssembly(1,1,1)

    def test_1(self):        
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
