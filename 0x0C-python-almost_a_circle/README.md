This README file contaians descriptions of the 0x0C-python-almost_a_circle tasks; The project focuses on object-oriented programming (OOP) concepts in Python. The main goal is to build and work with classes and objects that represent geometric shapes, specifically rectangles and squares.


#0x0C-python-almost_a_circle


0. If it's not tested, it doesn't work
Create a directory tests and a file test_models to contain all the test files for this project. Perform thorough testing of the Base class.

1. Base class
Create a class called Base that serves as the base of all other classes in this project. It manages the id attribute and provides serialization and deserialization functions.

2. First Rectangle
Create a class called Rectangle that inherits from Base. Implement the initialization method to set the width and height attributes.

3. Validate attributes
Update the Rectangle class by adding validation for the width and height attributes. Implement getter and setter methods for these attributes.

4. Area first
Add a method to the Rectangle class that calculates and returns the area of the rectangle.

5. Display #0
Add a method to the Rectangle class that prints a representation of the rectangle using the # character.

6. str
Override the __str__ method in the Rectangle class to return a formatted string representation of the rectangle.

7. Display #1
Update the Rectangle class to include an instance method that prints a representation of the rectangle using the # character, considering an offset.

8. Update #0
Add additional attributes and update the Rectangle class to allow for dynamic changes of the rectangle's position and size.

9. Update #1
Implement a method in the Rectangle class that updates the attributes with new values.

10. And now, the Square!
Create a class called Square that inherits from Rectangle. Update the initialization method to set the size attribute.

11. Square size
Update the Square class by adding validation for the size attribute. Implement getter and setter methods for this attribute.

12. Square update
Implement the update method in the Square class to allow for updating the attributes with new values.

13. Rectangle instance to dictionary representation
Add a method to the Rectangle class that returns the dictionary representation of a rectangle.

14. Square instance to dictionary representation
Add a method to the Square class that returns the dictionary representation of a square.

15. Dictionary to JSON string
Update the Base class by adding a static method that returns the JSON string representation of a list of dictionaries.

16. JSON string to file
Update the Base class by adding a class method that writes the JSON string representation of a list of objects to a file.

17. JSON string to dictionary
Update the Base class by adding a static method that returns the deserialization of a JSON string representation.

18. Dictionary to Instance
Update the Base class by adding a class method that returns an instance with all attributes already set.

19. File to instances
Update the Base class by adding a class method that returns a list of instances from a file containing JSON string representations

20. JSON ok, but CSV?
Update the Base class by adding the following methods:

A class method save_to_file_csv(cls, list_objs) that writes the CSV string representation of a list of instances to a file. The CSV format should contain the object's attributes as columns.
A class method load_from_file_csv(cls) that returns a list of instances from a CSV file. The CSV file should contain the object's attributes as columns.
