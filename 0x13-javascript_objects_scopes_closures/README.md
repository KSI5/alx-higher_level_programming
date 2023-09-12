This README file contains descriptions for the 0x13-javascript_objects_scopes_closures tasks.

#### 0x13-javascript_objects_scopes_closures


## Tests 

* [tests](./tests): Folder of test files. Provided by ALX.

## Function Prototypes :open_book:

Prototypes for functions written in this project:

| File               | Prototype                                               |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.esrever = function (list)`                     |
| `9-logme.js`       | `exports.logMe = function (item)`                       |
| `10-converter.js`  | `exports.converter = function (base)`                   |


## Tasks Descriptions :page_with_curl:




### Task 0: Empty Rectangle Class (0-rectangle.js)

- **Description:** Create a JavaScript class named `Rectangle` using the class notation. The class should be empty, with no properties or methods defined.

### Task 1: Rectangle Class with Constructor (1-rectangle.js)

- **Description:** Define a JavaScript class named `Rectangle` using the class notation. The class should include a constructor that takes two arguments, `width` and `height`, representing the width and height of the rectangle. Inside the constructor, initialize instance attributes `width` and `height` with the provided values.

### Task 2: Rectangle Class with Validation (2-rectangle.js)

- **Description:** Build upon Task 1 by adding validation to the `Rectangle` class. Create a JavaScript class named `Rectangle` using the class notation. The class should include a constructor that takes two arguments, `width` and `height`, representing the width and height of the rectangle. Inside the constructor, initialize instance attributes `width` and `height` with the provided values. If either `width` or `height` is equal to 0 or not a positive integer, create an empty object instead of a `Rectangle` object.

### Task 3: Rectangle Class with Print Method (3-rectangle.js)

- **Description:** Extend the `Rectangle` class from Task 2. Create a JavaScript class named `Rectangle` using the class notation. The class should include a constructor that takes two arguments, `width` and `height`, representing the width and height of the rectangle. Inside the constructor, initialize instance attributes `width` and `height` with the provided values. Additionally, add an instance method called `print()` that prints the rectangle using the character 'X'.


### Task 4: Rectangle Class with Rotate and Double Methods (4-rectangle.js)

- **Description:** Extend the `Rectangle` class created in Task 3 (`3-rectangle.js`) to add two new instance methods: `rotate()` and `double()`. The `rotate()` method should swap the `width` and `height` attributes of the rectangle, effectively rotating it by 90 degrees. The `double()` method should double the values of the `width` and `height` attributes. Ensure that the methods modify the instance attributes in place and do not return new instances.

### Task 5: Square Class with Inheritance (5-square.js)

- **Description:** This task involves creating a JavaScript class named `Square` that defines a square and inherits from a parent `Square` class (provided in `5-square.js`). The child class should use the `extends` keyword to inherit from the parent class.

### Task 6: Square Class with CharPrint Method (6-square.js)

- **Description:** In this task, you need to create a JavaScript class named `Square` that defines a square and inherits from a parent `Square` class (provided in `5-square.js`). Additionally, add an instance method called `charPrint(c)` to the child class, which prints the square using the character `c`. If `c` is undefined, it should default to 'X'.

### Task 7: Count Occurrences in a List (7-occurrences.js)

- **Description:** This task involves creating a JavaScript function `nbOccurences` that takes a list and a search element as arguments and returns the number of occurrences of the search element in the list. The function should be exported as a module.

### Task 8: Reverse a List (8-esrever.js)

- **Description:** In this task, you are required to create a JavaScript function `esrever` that reverses a list without using the built-in `reverse` method. The function should be exported as a module.

### Task 9: Log Number of Arguments (9-logme.js)

- **Description:** This task involves creating a JavaScript function `logMe` that prints the number of arguments already printed and the new argument value in a specific format. The function should keep track of the number of arguments printed across multiple function calls.

### Task 10: Base Converter (10-converter.js)
Description: This JavaScript module exports a function named converter that converts a number from base 10 to another base specified as an argument. The module does not import any external files, and it does not declare any new variables using var, let, or const. The converter function takes a single argument, base, which represents the target base for the conversion. The function converts a decimal number to the specified base and returns the result as a string.


###  Advanced Tasks :Mattock_tool:


### Task 100: Map with JavaScript (100-map.js)

- **Description:** This JavaScript script demonstrates the use of the `map` method to create a new array by applying a function to each element of an existing array. It imports an array from an external module, applies the `map` method to double each element of the array, and then prints both the original and new arrays.

### Task 101: Sorted Occurrences (101-sorted.js)

- **Description:** This JavaScript script imports a dictionary of occurrences by user id from an external module and computes a new dictionary of user ids by occurrence. In the new dictionary, the keys represent the number of occurrences, and the values are lists of user ids. The script prints the new dictionary as output.

### Task 102: Concatenate Files (102-concat.js)

- **Description:** This Node.js script concatenates the content of two source files and writes the result to a destination file. It takes three command-line arguments: the file paths of two source files and the file path of the destination file. The script reads the content of the source files, concatenates them, and then writes the concatenated data to the destination file.
