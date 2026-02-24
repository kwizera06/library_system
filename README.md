library_system



 # Library Management System (Advanced Python Concepts)

 Project Description

This is a simple **Library Management System** built in Python to demonstrate advanced programming concepts such as:

*  Object-Oriented Programming (OOP)
*  Decorators
*  Closures
*  Access Control
*  Logging with timestamps

The system allows users to:

* Add books
* Borrow books
* Return books
* Control access based on user roles (Admin/User)
* Automatically log book transactions

 Advanced Concepts Used

# Logging Decorator – `@track_access`

A custom decorator that:

* Logs method name
* Logs arguments
* Logs precise timestamp
* Runs whenever a book is borrowed or returned

Example:

```
[2026-02-24 20:15:03] Method: borrow_book | Args: ('Clean Code',)
```



# Access Control Using Closure

We implemented a closure:

```python
permission_check(required_role)
```

This returns a decorator that:

* Allows only users with the required role
* Prevents unauthorized access
* Used for methods like `add_book()`

Example:

* Only **Admin** can add books
* Normal users cannot add books

---

#  Project Structure

```
library_system/
│
├── __init__.py
├── __main__.py
├── core.py
├── util.py
```

---

# How to Run the Project (IMPORTANT)

 Do NOT run like this:

```
python __main__.py
```

 Run it as a module instead:

```powershell
cd C:\Users\hp\Desktop\School
C:/Users/hp/AppData/Local/Programs/Python/Python313/python.exe -m library_system
```

Or if Python is added to PATH:

```
python -m library_system
```


# User Roles       

 Admin | Can add books             
 User  | Can borrow & return books 


