This README file contains descriptions of the 0x07-python-test_driven_development tasks


#0x07-python-test_driven_development

**0-add_integer.py**:
Write a function def add_integer(a, b=98): that adds two integers and returns the result. The function should handle both integer and float input types and typecast float inputs to integers before performing the addition.

**2-matrix_divided.py**:
Write a function def matrix_divided(matrix, div): that divides all elements of a matrix by a given divisor and returns a new matrix. The function should validate the matrix input to ensure it is a list of lists containing only integers or floats, and that all rows have the same size. The divisor should be a non-zero integer or float.

**3-say_my_name.py**:
Write a function def say_my_name(first_name, last_name=""): that prints "My name is <first_name> <last_name>". The function should validate the inputs to ensure that first_name and last_name are strings. If last_name is not provided, an empty string should be printed instead.

**4-print_square.py**:
Write a function def print_square(size): that prints a square using the # character. The function should validate the input size to ensure it is a positive integer.

**5-text_indentation.py**:
Write a function def text_indentation(text): that indents a given text. The function should add two newlines after each ., ?, or : character in the text. The function should validate the input text to ensure it is a string.

**tests/6-max_integer_test.py** :
Write unittests for the function def max_integer(list=[]): that finds the largest integer in a list. The tests should cover various scenarios, including an empty list, a list with one element, and a list with multiple elements.

**100-matrix_mul.py**:
Write a function def matrix_mul(m_a, m_b): that multiplies two matrices and returns the result. The function should validate the input matrices to ensure they are valid matrices for multiplication, and return a new matrix as the result.

**101-lazy_matrix_mul.py**:
Write a function def lazy_matrix_mul(m_a, m_b): that multiplies two matrices using the numpy.matmul function and returns the result. The function should validate the input matrices to ensure they are valid matrices for multiplication, and return a new matrix as the result.

**102-python.c**:
Write a C function void print_python_string(PyObject *p); that prints information about Python strings. The function should take a PyObject string object as input and print its type, length, and value. If the input is not a valid string object, an error message should be printed instead.
