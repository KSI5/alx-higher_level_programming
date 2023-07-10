This filr contains descriptions of the 0x0A-python-inheritance tasks.

#0x0A-python-inheritance

0-lookup.py:
Write a function lookup that returns the list of available attributes and methods of an object.

1-my_list.py:
Write a class MyList that inherits from the built-in list class. The class should have a method print_sorted that prints the list in sorted order (ascending).

2-is_same_class.py:
Write a function is_same_class that checks if an object is exactly an instance of the specified class. It should return True if the object is an instance of the class, and False otherwise.

3-is_kind_of_class.py:
Write a function is_kind_of_class that checks if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class. It should return True if the object is an instance of the class or a subclass, and False otherwise.

4-inherits_from.py:
Write a function inherits_from that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class. It should return True if the object is an instance of a subclass, and False otherwise.

5-base_geometry.py:
Write an empty class BaseGeometry as a base class for other classes representing geometrical shapes.

6-base_geometry.py:
Update the BaseGeometry class by adding a area method that raises an exception with the message "area() is not implemented".

7-base_geometry.py:
Update the BaseGeometry class by adding a integer_validator method that validates if a value is an integer and greater than 0.

8-rectangle.py:
Write a class Rectangle that inherits from BaseGeometry. The class should have a constructor that initializes the width and height attributes, which are validated as positive integers. It should also have an area method that calculates the area of the rectangle, and a __str__ method that provides a string representation of the rectangle.

9-rectangle.py:
Update the Rectangle class by adding a __str__ method that provides a string representation of the rectangle in the format "[Rectangle] <width>/<height>".

10-square.py:
Write a class Square that inherits from Rectangle. The class should have a constructor that initializes the size attribute, which is validated as a positive integer. It should also have a __str__ method that provides a string representation of the square in the format "[Square] <size>/<size>".

100-my_int.py:
Write a class MyInt that inherits from int. The class should have a different behavior for the equality (==) and inequality (!=) operators. The equality operator should behave as the inequality operator, and vice versa.

101-add_attribute.py:
Write a function add_attribute that adds a new attribute to an object if possible. If it's not possible (e.g., if the object is an instance of an int or a bool), raise a TypeError with the message "can't add new attribute".
