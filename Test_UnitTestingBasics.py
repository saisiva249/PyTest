"""
Performing unit testing in python:
Module name: unittest
Class name: TestCase
Instance methods: 3 methods we have to override

	1. setUp()
	2. test(): test name should be prefixed with test
	3. tearDown()
  4.Instantiate the unittest.main()

"""


import unittest

#Test Suit
# test suit means group of test cases. so if we need to execute more than one test case then we go to test suit.

# test results will be displayed in the console only and not possible to generate the reports
# unit test frameworks always execute test cases in the alphabetical order only, and it is not possible to customize execute order.
# As a part of the batch execution, we can run all the test cases, we cannot specify the test cases particularly.
# if we are having a test suit, we dont have methods to configure the intial setup for testsuit and teardown for testsuit
# so we go for the pytest

# run a test case py filename.py
class basicSampleTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Class method executed")
        
    def setUp(self):
        print("Setup executed")

    def test_method(self):
        print("Testing method")
    
    def tearDown(self):
        print("Tear down method")
      
    @classmethod
    def tearDownClass(self):
        print("Tear down Class")
        
unittest.main() ==> this will instantiate the running of the test case identification
