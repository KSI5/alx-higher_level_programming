# 0x0F-python-object_relational_mapping

## Description 📃
This project aims to learn about how to connect to a MySQL database from a Python script, what ORM means and how to map a Python Class to a MySQL table.

## Technologies 💻
* `MySQL 8`.
* `MySQLdb`, version 2.0.x.
* `sqlalchemy`, version 1.4.x.
* Python Scripts are written with Python 3.8.
* Tested on Ubuntu 20.04 LTS.





## Mandatory Tasks 📌


### 0-select_states.py

**Description:**
This script connects to a MySQL database and retrieves a list of states from the states table. It then displays the results in ascending order based on the state's ID. The script serves as an introductory task for establishing a database connection and performing a basic query using Python and the MySQL database.

### 1-filter_states.py

**Description:**  
This script establishes a connection to a MySQL database and retrieves a list of states from the `states` table. It then filters and displays the states whose names start with the letter 'N'. The results are presented in ascending order based on the state's ID.

### 2-my_filter_states.py

**Description:**  
In this script, a connection to a MySQL database is established, and all state records from the `states` table are retrieved. The script filters and displays states that match a user-specified argument. The results are sorted in ascending order by state ID.

### 3-my_safe_filter_states.py

**Description:**  
Building upon Task 2, this script connects to a MySQL database, retrieves state records from the `states` table, and filters states based on user-provided input. It incorporates secure SQL injection prevention techniques to safeguard against potential SQL injection attacks. The results are ordered by state ID in ascending order.

### 4-cities_by_state.py

**Description:**  
This script establishes a connection to a MySQL database and retrieves data from the `cities` and `states` tables. It displays a list of cities along with their respective state names, sorted in ascending order by city ID. The output format is `<state name>: (<city id>) <city name>`.

### 5-filter_cities.py

**Description:**  
In this script, a connection to a MySQL database is established to retrieve city records from the `cities` table. The script then filters and displays cities based on a user-provided argument. The results are sorted in ascending order by city ID.

### 6-model_state.py

**Description:**  
This module defines the SQLAlchemy model class `State`, representing the `states` table. It includes attributes for `id` (a unique, non-null, auto-generated integer and primary key) and `name` (a non-null string with a maximum length of 128 characters).

### 7-model_state_fetch_all.py

**Description:**  
This script connects to a MySQL database, retrieves all state records from the `states` table, and displays them. It illustrates how to utilize SQLAlchemy to fetch all records from a database table and presents the results.

### 8-model_state_fetch_first.py

**Description:**  
In this script, a connection to a MySQL database is established. It fetches the first state record from the `states` table and displays it. The script demonstrates how to use SQLAlchemy to retrieve the initial record from a database table.

### 9-model_state_filter_a.py

**Description:**  
This script establishes a connection to a MySQL database and retrieves state records from the `states` table containing the letter 'a' in their names. It displays the filtered results. The script showcases SQLAlchemy's filtering capabilities.

### 10-model_state_my_get.py

**Description:**  
In this script, a connection to a MySQL database is established. It retrieves a state record from the `states` table based on a user-specified argument (state name) and displays it. The script demonstrates how to use SQLAlchemy to fetch a specific record from a database table.

### Task 11: 11-model_state_insert.py

**Description:**  
This script connects to a MySQL database, creates a new state record with the name "Louisiana," inserts it into the `states` table, and displays the newly assigned state ID. It exemplifies how to use SQLAlchemy to insert new records into a database table.

### Task 12: 12-model_state_update_id_2.py

**Description:**  
In this script, a connection to a MySQL database is established. It retrieves the state record with `id = 2` from the `states` table, updates its name to "New Mexico," and commits the changes. The script showcases how to use SQLAlchemy to modify an existing record in a database table.

### Task 13: 13-model_state_delete_a.py

**Description:**  
This script connects to a MySQL database, retrieves state records from the `states` table containing the letter 'a' in their names, deletes them, and commits the changes. It demonstrates how to use SQLAlchemy to delete records from a database table based on specific criteria.

### model_city.py

**Description:**  
This module defines the SQLAlchemy model class `City`, representing the `cities` table. It includes attributes for `id` (a unique, non-null, auto-generated integer and primary key), `name` (a non-null string with a maximum length of 128 characters), and `state_id` (an integer, non-null, foreign key referencing `states.id`).

### 14-model_city_fetch_by_state.py

**Description:**  
This script connects to a MySQL database, retrieves all city records from the `cities` table, and includes their corresponding state names. It displays the results in the format `<state name>: (<city id>) <city name>`. The script demonstrates how to utilize SQLAlchemy for complex queries and table joins to retrieve data.

---

## Advanced Tasks 💪


### relationship_city.py

**Description:**  
In this task, you will create a Python script `relationship_city.py` that defines a SQLAlchemy model class `City` representing the `cities` table. The `City` class will establish a bidirectional relationship with the `State` class, reflecting the relationship between cities and states in the database. This task introduces the concept of relationships in SQLAlchemy and demonstrates how to establish connections between tables.

### relationship_state.py

**Description:**  
In this task, you will create a Python script `relationship_state.py` that defines a SQLAlchemy model class `State` representing the `states` table. The `State` class will establish a bidirectional relationship with the `City` class, reflecting the relationship between states and cities in the database. Similar to Task 1, this task focuses on relationships in SQLAlchemy and demonstrates how to establish connections between tables.

### 100-relationship_states_cities.py

**Description:**  
This task involves creating a Python script `100-relationship_states_cities.py` that defines the `State` and `City` classes using SQLAlchemy. These classes establish a one-to-many (1:N) relationship between states and cities, where each state can have multiple associated cities. The script demonstrates how to create and manipulate database relationships using SQLAlchemy.

### 101-relationship_states_cities_list.py

**Description:**  
In this task, you will develop a Python script `101-relationship_states_cities_list.py` that connects to a MySQL database, retrieves all states, and displays their associated cities. This script demonstrates how to query and retrieve related data using SQLAlchemy relationships. The results are presented in a format that lists each state along with its cities.

### 102-relationship_cities_states_list.py

**Description:**  
This task involves creating a Python script `102-relationship_cities_states_list.py` that connects to a MySQL database, retrieves all cities, and displays their associated states. The script demonstrates how to query and retrieve related data using SQLAlchemy relationships. The results are presented in a format that lists each city along with its corresponding state.

