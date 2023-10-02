import unittest
import dnaseq

class MyTestCase(unittest.TestCase):


    def test_something(self):

        print ("a")
        self.assertEqual([1], dnaseq.DNAadd([],1))  # add assertion here
        print("b")

if  __name__ == '__main__':
    unittest.main()
