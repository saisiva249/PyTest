"""
Naming Conventions:
File Name, should start or end with test
test functions should start with test, and which are, not starting with test are not considered as py test, and we cannot make it explicitly detect if we give command

Commands:
>pytest, with out mentioning file name then it will run the files of format test_*.py or *_test.py in the current
directory and subdirectories.

>pytest -v, which gives us result more readable

>if we want to run a particular file then we have to use
pytest <filename> -v

> execute substring match test cases (-k substring)
pytest -k <substring> -v

> markers: markers used to group the test cases, markers are also used to set different various features,
inbuilt markers provided by pytest are xfail, skip parametrize.
@pytest.mark.<marker_Name>
pytest -m <marker_name> -v  (-m marker)

>fixtures: they are functions holding the common data which we can execute before running each test case, so that we can
avoid duplicate code running in each test case,
--defining a function as a fixture using @pytest.fixture
--to use fixture, for a particular test , function name should ne provided as input to test
we cannot use the fixture defined in a file in another file, for which we have ot use conftest.py

>conftest.py: if we have a fixture function, which is common to be executed for more than a file then we use
conftest, so we define the fixture there and use that fixture function name in the test. test will look for the fixture
in the same file, and if that fixture is not avaiable then it will search for the conftest
* conftest should be in the same root directory else it will not work

>paramterizing test: we can provide multiple sets of inputs, and run tests with these inputs. this can be done
using the marker
@pytest.mark.parameterize(" patameters names seperated by comma", [(input1, values1),(input2, values2)])

>xfail/skip:
@pytest.mark.xfail
@pytest.mark.skip
difference is xfail is like ignoring after execution, means test will run but tests will not
be printed. where as in skip tests will not be executed

> stop test suit after N test failures
pytest --maxfail = <num>
so after the max number of failures test case execution will stop

>Run pytests in parallel: by default pytests will run in sequential order, if we have to run in parallel,
we need pytest distributed test plugin
pip install pytest-xdist
pytest -n <num>, num is the number of test run in multiple workers

>Test execution result in XML format
we can generate the details of the test execution in an xml using
pytest test_fileName.py -v --junitxml="result.xml"

>for generating report in the html format:
pip install pytest-cov

coverage can be generated in the xml and html format,
pytest --cov=. --cov-report xml:coverage-> generates the file and shows result
pytest --cov=. --cov-report html:coverage --> this will generate a folder of coverage and shows the result
*****
Summary: 
Installing pytest..
Identifying test files and test functions.
Executing all test files using pytest –v.
Executing specific file usimng pytest <filename> -v.
Execute tests by substring matching pytest -k <substring> -v.
Execute tests based on markers pytest -m <marker_name> -v.
Creating fixtures using @pytest.fixture.
conftest.py allows accessing fixtures from multiple files.
Parametrizing tests using @pytest.mark.parametrize.
Xfailing tests using @pytest.mark.xfail.
Skipping tests using @pytest.mark.skip.
Stop test execution on n failures using pytest --maxfail = <num>.
Running tests in parallel using pytest -n <num>.
Generating results xml using pytest -v --junitxml = "result.xml".
**Source: https://www.tutorialspoint.com/**
 """


import math
import pytest


@pytest.mark.sample_mark
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def testSquare():
    num = 7
    assert 7 * 7 == 49


def testquality():
    assert 1 == 2


def test_fixture(input_sample):
    assert 9 == input_sample


@pytest.mark.parametrize("num,output", [(1, 11), (2, 22), (3, 33)])
def test_multiple_param(num, output):
    assert 11 * num == output
