import unittest
import calculator
import argparse

class TestFirst(unittest.TestCase):

    def test_multiplies_2_num(self):
        # parser = argparse.ArgumentParser()
        self.assertEqual(calculator.multi_2_num(123, 456), 56088)


if __name__ == "__main__":
    unittest.main(verbosity=2)