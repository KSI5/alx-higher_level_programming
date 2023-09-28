# 0x10-python-network_0 🖋️

## Mandatory Tasks 📖

This repository contains Bash and Python scripts for various tasks.
## Table of Contents

| Task | Description |
| ---  | ---         |
| [Task 0: cURL body size](#task-0-curl-body-size) | Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. The size must be displayed in bytes, and you have to use `curl` for this task. |
| [Task 1: cURL to the end](#task-1-curl-to-the-end) | Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. Display only the body of a 200 status code response, and you have to use `curl`. |
| [Task 2: cURL Method](#task-2-curl-method) | Write a Bash script that takes in a URL and displays all HTTP methods the server will accept. You have to use `curl` for this task. |
| [Task 3: cURL headers](#task-3-curl-headers) | Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`, and you have to use `curl`. |
| [Task 4: cURL POST parameters](#task-4-curl-post-parameters) | Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. Two variables, `email` with the value `test@gmail.com` and `subject` with the value `I will always be here for PLD`, must be sent as POST parameters. You have to use `curl` for this task. |
| [Task 5: Peak Finder](#task-5-peak-finder) | Write a Python function called `find_peak` that finds a peak in a list of unsorted integers. The function should return a peak element from the list. You are not allowed to import any modules, and your algorithm must have the lowest complexity. The function should work for lists with multiple peak elements. |
| [Task 6: Peak Finder Complexity](#task-6-peak-finder-complexity) | In the `6-peak.txt` file, specify the complexity of your algorithm used in Task 5 (`find_peak`). Indicate whether it's `O(log(n))`, `O(n)`, `O(nlog(n))`, or `O(n^2)`. |


##  Advanced Tasks 💪

#### Only status code

* **Task:** `100-status_code.sh`
* **Description:** Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.
* **Usage:** `./100-status_code.sh <URL>`

#### cURL a JSON file

* **Task:** `101-post_json.sh`
* **Description:** Write a Bash script that sends a JSON POST request to a URL and displays the body of the response.
* **Usage:** `./101-post_json.sh <URL> <JSON_FILE>`

#### Catch me if you can!

* **Task:** `102-catch_me.sh`
* **Description:** Write a Bash script that makes a request to 0.0.0.0:5000/catch_me and makes the server respond with a message "You got me!".
* **Usage:** `./102-catch_me.sh`

