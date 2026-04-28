### To run test fixtures
pytest -s -v test_file_one.py test_file_two.py

### classic way of organising like unittest framework 
pytest -s -v test_classic.py

### to run markers  
pytest -m setexample

### To run using specific keyword
`pytest test_example.py -k "keyword"`


### To run whole of tests folder
`pytest Tests/`

### Run a specific test within a test file
`pytest test_example.py::test_addition`

### to run all test cases in a specific class
`pytest test_example.py::TestClass`

### to run specific test 
`pytest test_example.py::TestClass::test_addition`

