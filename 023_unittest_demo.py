# unittest_demo.py - 简单的单元测试示例
import unittest

def add(a, b): return a + b

class TestAdd(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(1,2), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
