# 🎓 Inheritance-Based Learning Platform

A simple **Python Object-Oriented Programming (OOP)** project that demonstrates **Inheritance** and **Method Overriding** by building a small learning platform.

The platform contains a parent `User` class and three child classes:

- `Student`
- `Mentor`
- `Admin`

Each child class inherits common properties and methods from the `User` class while implementing its own role-specific functionality.

---

## 📌 Project Objective

The objective of this project is to understand and demonstrate:

- Classes and Objects
- Constructors (`__init__`)
- Parent and Child Classes
- Inheritance
- Method Overriding
- `super()` function
- Code Reusability
- Exception Handling
- Custom Exceptions
- Logging
- Python Packages and Modules

---

## 🏗️ Class Architecture

```text
                    User
                     │
          ┌──────────┼──────────┐
          │          │          │
       Student     Mentor      Admin
```

### User

The `User` class acts as the **parent/base class**.

Common attributes:

```text
user_id
name
email
```

Common methods:

```text
display_info()
get_role()
```

### Student

`Student` inherits from `User`.

Additional functionality includes:

```text
course
completed_courses
enroll_course()
complete_course()
```

### Mentor

`Mentor` inherits from `User`.

Additional functionality includes:

```text
expertise
students
assign_student()
```

### Admin

`Admin` inherits from `User`.

Additional functionality includes:

```text
managed_users
add_user()
remove_user()
```

---

## 🔄 Method Overriding

Method overriding occurs when a child class provides its own implementation of a method already available in the parent class.

The parent `User` class contains:

```python
def get_role(self):
    return "User"
```

The `Student` class overrides it:

```python
def get_role(self):
    return "Student"
```

Similarly, `Mentor` and `Admin` provide their own implementations.

```python
for user in users:
    print(user.get_role())
```

Output:

```text
Student
Mentor
Admin
```

The same method behaves differently depending on the object calling it.

---

## ♻️ Using `super()`

The child classes use `super()` to call the constructor of the parent `User` class.

Example:

```python
class Student(User):

    def __init__(self, user_id, name, email, course):

        super().__init__(user_id, name, email)

        self.course = course
```

This allows the child class to reuse the initialization logic from the parent class instead of rewriting it.

---

## 📂 Project Structure

```text
inheritance_learning_platform/
│
├── learning_platform/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   ├── admin.py
│   ├── exceptions.py
│   └── logger.py
│
├── logs/
│   └── platform.log
│
├── main.py
├── README.md
└── .gitignore
```

---

## ⚙️ Module Description

| File | Purpose |
|---|---|
| `user.py` | Contains the parent `User` class |
| `student.py` | Contains the `Student` child class |
| `mentor.py` | Contains the `Mentor` child class |
| `admin.py` | Contains the `Admin` child class |
| `exceptions.py` | Contains custom exceptions |
| `logger.py` | Configures application logging |
| `__init__.py` | Initializes the Python package |
| `main.py` | Entry point of the application |

---

## 🚀 Features

### Student

A student can:

- Enroll in a course
- Complete a course
- View student information
- Maintain completed courses

### Mentor

A mentor can:

- Maintain expertise information
- Receive assigned students
- View mentor information

### Admin

An admin can:

- Add users
- Remove users
- Maintain a list of managed users
- View admin information

---

## ⚠️ Exception Handling

The project contains a custom exception:

```python
class InvalidUserError(Exception):
    pass
```

It can be raised when invalid user information is provided.

Example:

```python
if not name.strip():
    raise InvalidUserError("User name cannot be empty.")
```

Exception handling helps prevent the application from terminating unexpectedly when invalid data is provided.

---

## 📝 Logging

The project uses Python's built-in `logging` module.

Application activities are recorded in:

```text
logs/platform.log
```

Examples of logged activities include:

- Student creation
- Mentor creation
- Admin creation
- Course enrollment
- Course completion
- Student assignment
- Admin operations
- Application errors

---

## 💻 Requirements

- Python 3.x
- VS Code or another Python IDE
- Git
- GitHub account

No external Python packages are required.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd inheritance_learning_platform
```

### 3. Run the application

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

---

## 🖥️ Sample Output

```text
==================================================
       EVOLVE LEARNING PLATFORM
==================================================

--- Student Activity ---

Amrutha enrolled in Advanced Python.
Amrutha completed Python Fundamentals.

--- Mentor Activity ---

Amrutha assigned to mentor Arjun.

--- Admin Activity ---

Admin Meera added Amrutha.
Admin Meera added Arjun.

==================================================
METHOD OVERRIDING DEMONSTRATION
==================================================

Amrutha -> Student
Arjun -> Mentor
Meera -> Admin

Learning Platform execution completed.
```

---

## 🧠 OOP Concepts Demonstrated

### 1. Class

Classes such as `User`, `Student`, `Mentor`, and `Admin` act as blueprints for creating objects.

### 2. Object

Objects are created from the classes.

Example:

```python
student1 = Student(
    101,
    "Amrutha",
    "amrutha@example.com",
    "Python"
)
```

### 3. Inheritance

Child classes inherit common functionality from `User`.

```python
class Student(User):
```

### 4. Method Overriding

Child classes provide their own implementations of inherited methods.

```python
def get_role(self):
    return "Student"
```

### 5. `super()`

`super()` is used to access the parent class constructor and reuse its initialization logic.

```python
super().__init__(user_id, name, email)
```

### 6. Polymorphic Behavior

The same method call can produce different results depending on the object.

```python
for user in users:
    print(user.get_role())
```

---

## 🌍 Real-World Application

This architecture is similar to real learning platforms.

All platform members may share basic information such as:

```text
Name
Email
User ID
```

However, their responsibilities are different.

```text
Student → Learns and completes courses

Mentor → Guides students

Admin → Manages platform users
```

Inheritance allows us to model these relationships while avoiding duplicate code.

---

## 📚 Key Learning

This project demonstrates how inheritance can be used to build a clean and reusable application architecture.

Instead of defining common user information separately inside `Student`, `Mentor`, and `Admin`, the common functionality is placed in the parent `User` class.

The child classes then extend or override that functionality according to their individual responsibilities.

---

## 👩‍💻 Author

**Amrutha Varshini Alva**

Python | OOP | Git & GitHub | AI & Technology Learning

---

## 📄 License

This project is created for educational purposes.
