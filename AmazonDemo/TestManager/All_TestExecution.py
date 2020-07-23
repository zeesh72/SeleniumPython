import unittest
from AmazonDemo.AmazonTest.AmzTestCase import AmzTestDemo

tc = unittest.TestLoader().loadTestsFromTestCase(AmzTestDemo)

unittest.TextTestRunner().run(tc)