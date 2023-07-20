# API

<details>
<summary>What Bash scripting should not be used for?</summary>
<br>
Bash scripting should not be used for complex applications that require extensive data processing or heavy computational tasks. While Bash is powerful for automating tasks, it is primarily designed for shell scripting and lacks the advanced features and performance of programming languages like Python or C++.
</details>
<details>
<summary>What is an API?</summary>
<br>
An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request or exchange information.
</details>
<details>
<summary>What is a REST API?</summary>
<br>
A REST API (Representational State Transfer API) is a type of API that follows the principles of the REST architectural style. It is based on a client-server communication model and uses standard HTTP methods like GET, POST, PUT, and DELETE to interact with resources. REST APIs typically use JSON (or sometimes XML) as the data format for representing and transferring data.
</details>
<details>
<summary>What are microservices?</summary>
<br>
Microservices are an architectural approach to building software applications as a collection of small, loosely coupled services. Each microservice focuses on a specific business capability and can be developed, deployed, and scaled independently. Microservices promote modularity, flexibility, and the ability to develop and maintain complex applications more effectively.
</details>
<details>
<summary>What is the CSV format?</summary>
<br>
CSV (Comma-Separated Values) is a plain text file format commonly used for storing tabular data. Each line in a CSV file represents a row, and the values within each row are separated by commas. CSV files are widely supported and can be opened and manipulated using spreadsheet software or programming languages.
</details>
<details>
<summary>What is the JSON format?</summary>
<br>
JSON (JavaScript Object Notation) is a lightweight data interchange format. It is often used for representing structured data in a human-readable and machine-readable format. JSON data consists of key-value pairs and supports nested structures, arrays, numbers, booleans, and null values. It has become a popular format for data exchange between web services and is widely supported in various programming languages.
</details>
<details>
<summary>Pythonic Package and module name style</summary>
<br>
Pythonic package and module names should be in lowercase, with multiple words separated by underscores. For example, "my_package" or "utils_module".
</details>
<details>
<summary>Pythonic Class name style</summary>
<br>
Pythonic class names should follow the CapWords or CamelCase convention, where each word's initial letter is capitalized, without underscores. For example, "MyClass" or "DataProcessor".
</details>
<details>
<summary>Pythonic Variable name style</summary>
<br>
Pythonic variable names should be in lowercase, with words separated by underscores. For example, "my_variable" or "data_list".
</details>
<details>
<summary>Pythonic Function name style</summary>
<br>
Pythonic function names should also be in lowercase, with words separated by underscores. For example, "calculate_sum" or "process_data".
</details>
<details>
<summary>Pythonic Constant name style</summary>
<br>
Pythonic constant names should be in uppercase, with words separated by underscores. For example, "MAX_VALUE" or "DEFAULT_TIMEOUT".
</details>
<details>
<summary>Significance of CapWords or CamelCase in Python</summary>
<br>
CapWords or CamelCase convention in Python is significant as it improves readability and adheres to the widely adopted naming conventions in the Python community. It helps distinguish class names from functions, variables, or constants, making the code easier to understand and maintain.
</details>

# API: Tasks

<details>
<summary>0. Gather data from an API</summary>
<br>Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
</details>

<details>
<summary>1. Export to CSV</summary>
<br>Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
</details>

<details>
<summary>2. Export to JSON</summary>
<br>Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
</details>
