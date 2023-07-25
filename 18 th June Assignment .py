#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the role of the 'else' block in a try-except statement? Provide an examplescenario where it would be useful.

# The role of the ‘else’ block in a try-except statement is to execute some code when there is no exception raised by the try block. It is useful when you want to perform some action that depends on the success of the try block, but does not need to be inside it. For example, you may want to print a message or log some information when the try block completes without errors, but you don’t want to catch any exceptions that may occur in the printing or logging process. Here is a simple example of using the ‘else’ block in a try-except statement.
# 
# 

# # Q2. Can a try-except block be nested inside another try-except block? Explain with an example.

# Yes, a try-except block can be nested inside another try-except block in Python. This means that you can have a try-except block inside the try, except, or finally clause of another try-except block. This is useful when you want to handle different types of exceptions at different levels of your code, or when you want to perform some actions that may raise exceptions themselves.
# 
# For example, suppose you want to write a function that reads a file and returns its contents as a list of numbers. You may want to use a nested try-except block to handle the following scenarios:
# 
# The file may not exist, in which case you want to catch the FileNotFoundError exception and print an error message.
# The file may exist, but it may not be readable, in which case you want to catch the PermissionError exception and print an error message.
# The file may be readable, but it may contain invalid data, such as non-numeric characters or empty lines, in which case you want to catch the ValueError exception and print an error message.
# The file may be valid, but you may encounter some other unexpected exception while reading it, in which case you want to catch the generic Exception class and print an error message.

# # Q3. How can you create a custom exception class in Python? Provide an example that demonstrates its usage.

# A custom exception class in Python is a class that inherits from the built-in Exception class or one of its subclasses. Users can define custom exceptions by creating a new class with the Exception class as an argument. Custom exceptions can have additional features such as logging errors or inspecting objects. The raise keyword is used to trigger custom exceptions, and the try…except blocks are used to handle them1.
# 
# For example, suppose you want to create a custom exception class called NegativeNumberError that is raised when a negative number is encountered. You can define it as follows:
# 
# class NegativeNumberError(Exception):
# 
# constructor with an optional message argument
# def init(self, message=“Negative number is not allowed”): # call the base class constructor with the message super().init(message)
# 
# Now, you can use this custom exception class in your code. For example, suppose you have a function that calculates the square root of a number. You can raise the NegativeNumberError exception if the input is negative, and handle it in a try…except block:
# 
# import math
# 
# def square_root(x):
# 
# check if x is negative
# if x < 0: # raise the custom exception with the input value raise NegativeNumberError(f"Cannot calculate square root of {x}") else: # return the square root of x return math.sqrt(x)
# 
# test the function with different inputs
# try: print(square_root(9)) print(square_root(-4)) except NegativeNumberError as e:
# 
# print the error message
# print(e)
# 
# The output of this code is:
# 
# 3.0 Cannot calculate square root of -4
# 
# You can learn more about custom exceptions in Python from these sources

# # Q4. What are some common exceptions that are built-in to Python?

# Some common exceptions that are built-in to Python are:
# 
# 1. SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# 2. NameError: This exception is raised when a variable or a function name is not found in the local or global scope.
# 3. TypeError: This exception is raised when an operation or a function is applied to an object of an inappropriate type, such as adding a string and an integer.
# 4. ValueError: This exception is raised when an operation or a function receives an argument that has the right type but an inappropriate value, such as converting a string that does not represent a number to an integer.
# 5. IndexError: This exception is raised when a sequence subscript is out of range, such as accessing the fifth element of a list that has only four elements.
# 6. KeyError: This exception is raised when a key is not found in a dictionary.
# 7. ZeroDivisionError: This exception is raised when the second operand of a division or modulo operation is zero.
# 8. FileNotFoundError: This exception is raised when a file or directory is requested but does not exist.
# 9. ImportError: This exception is raised when the imported module or package is not found

# # Q5. What is logging in Python, and why is it important in software development

# Logging in Python is a way of recording events that happen during the execution of a program. It is important in software development because it can help you:
# 
# 1. Debug your code by finding and fixing errors or bugs
# 2. Monitor your application’s performance, behavior, and status
# 3. Analyze your application’s usage patterns, user feedback, and statistics
# 4. Audit your application’s security, compliance, and accountability
# 
# Logging in Python is done using the built-in logging module1, which provides a flexible and powerful framework for creating and managing log messages. You can use different levels of severity to indicate the importance of each log message, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. You can also use different handlers to send the log messages to different destinations, such as files, consoles, emails, or web servers. You can also use different formatters to customize the layout and format of the log messages, such as adding timestamps, filenames, line numbers, or colors.
# 
# Logging in Python is easy to use and configure. You can start logging with just a few lines of code:

# In[1]:


import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the logging level
logger.setLevel(logging.INFO)

# Create a handler object
handler = logging.StreamHandler()

# Set the handler format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log some messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


# # Q6. Explain the purpose of log levels in Python logging and provide examples of when each log level would be appropriate.

# Log levels in Python logging are a way of categorizing the importance or severity of log messages. They help you control what kind of information you want to record and display when your program runs. Depending on the level you set for your logger or handler, you can filter out less important messages and focus on the more critical ones.
# 
# The log levels in Python logging are:
# 
# 1. DEBUG: This level is used for detailed information that is typically only useful for debugging purposes. For example, you can use this level to log the values of variables, the execution flow of your code, or the results of intermediate calculations. This level is the lowest and shows all messages.
# 2. INFO: This level is used for confirmation that things are working as expected. For example, you can use this level to log the start and end of a function, the status of a process, or the completion of a task. This level is useful for normal operation and shows all messages except DEBUG.
# 3. WARNING: This level is used for indication that something unexpected or problematic happened, or may happen in the near future. For example, you can use this level to log a deprecated feature, a low disk space, or a network error. This level is useful for warning about potential issues and shows all messages except DEBUG and INFO.
# 4. ERROR: This level is used for reporting that an error occurred and some function or operation failed. For example, you can use this level to log an exception, a database query failure, or a file not found. This level is useful for identifying and fixing errors and shows all messages except DEBUG, INFO, and WARNING.
# 5. CRITICAL: This level is used for reporting that a serious error occurred and the program may not be able to continue running. For example, you can use this level to log a fatal exception, a memory overflow, or a system crash. This level is useful for alerting about critical situations and shows only CRITICAL messages.

# # Q7. What are log formatters in Python logging, and how can you customise the log message format using formatters?

# Log formatters in Python logging are objects that specify the layout and format of log messages. They can be used to customize the appearance and content of the logs, such as adding timestamps, filenames, line numbers, or colors. Log formatters can also be used to create different formats for different handlers or loggers, depending on the needs of the application12.
# 
# To use log formatters in Python logging, you need to do the following steps:
# 
# 1. Import the logging module
# 2. Create a logger object using logging.getLogger(name)
# 3. Create a handler object using logging.StreamHandler(), logging.FileHandler(), or other subclasses of logging.Handler
# 4. Create a formatter object using logging.Formatter(fmt, datefmt), where fmt is a string that defines the log message format, and datefmt is a string that defines the date and time format
# 5. Set the formatter on the handler using handler.setFormatter(formatter)
# 6. Add the handler to the logger using logger.addHandler(handler)
# 7. Log some messages using logger.debug(), logger.info(), logger.warning(), logger.error(), or logger.critical()
#  
#  The fmt string can contain any literal text and placeholders for variable data, such as %(levelname)s for the log level name, %(message)s for the log message, %(asctime)s for the date and time, and so on. You can find a full list of available placeholders in the Python documentation3. The datefmt string can contain any directives supported by time.strftime(), such as %Y for the year, %m for the month, %d for the day, and so on. You can find a full list of available directives in the Python documentation4.
# 
# Here is an example of using log formatters in Python logging:

# In[2]:


import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the logging level
logger.setLevel(logging.INFO)

# Create a handler object
handler = logging.StreamHandler()

# Create a formatter object
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set the formatter on the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log some messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


# # Q8. How can you set up logging to capture log messages from multiple modules or classes in a Python application?

# One way to set up logging to capture log messages from multiple modules or classes in a Python application is to use the following steps:
# 
# * In each module or class, create a logger object using logging.getLogger(__name__), where __name__ is a variable that contains the name of the current module or class. This will create a logger with a hierarchical name that reflects the package structure of your application. For example, if you have a module called myapp.utils and a class called MyClass inside it, the logger name will be myapp.utils.MyClass.
# * In each module or class, use the logger object to log messages at different levels, such as logger.debug(), logger.info(), logger.warning(), and so on. You can also use the logging module’s convenience functions, such as logging.debug(), logging.info(), and so on, which will use the root logger by default.
# * In the main module or script of your application, configure the logging system using logging.basicConfig() or logging.config.dictConfig() to set up the handlers, formatters, filters, and levels for the root logger and its children. You can also create and configure individual loggers using logging.getLogger(name) and logger.addHandler(), logger.setFormatter(), logger.addFilter(), and logger.setLevel(). You can use different handlers to send the log messages to different destinations, such as files, consoles, emails, or web servers. You can use different formatters to customize the layout and format of the log messages, such as adding timestamps, filenames, line numbers, or colors. You can use different filters to filter out unwanted log messages based on some criteria, such as level, name, or message content. You can use different levels to control the verbosity of the log messages, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.
# * Run your application and observe the log messages from different modules or classes in your chosen destinations.
# 
# 

# # Q9. What is the difference between the logging and print statements in Python? When should you use logging over print statements in a real-world application?

# The difference between the logging and print statements in Python is that logging is a module that provides a flexible and powerful framework for creating and managing log messages, while print is a built-in function that simply prints the specified value or values to the console. Logging and print serve different purposes and have different advantages and disadvantages.
# 
# * Logging is mainly used for recording events and errors that occur during the execution of a Python program. Logging can help you debug, monitor, analyze, and audit your application. Logging has features such as:
# 
# * Log levels: You can categorize your log messages based on their importance or severity, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. You can also filter out less important messages and focus on the more critical ones.
# * Log handlers: You can send your log messages to different destinations, such as files, consoles, emails, or web servers. You can also use different handlers for different loggers or modules.
# * Log formatters: You can customize the layout and format of your log messages, such as adding timestamps, filenames, line numbers, or colors. You can also use different formatters for different handlers or loggers.
# * Log filters: You can filter out unwanted log messages based on some criteria, such as level, name, or message content. You can also use different filters for different handlers or loggers.
# 
# Print is mainly used for displaying information to the console for debugging purposes. Print is not recommended for logging information in production code. Print has limitations such as:
# 
# * Print does not have any log levels. You cannot easily control the verbosity of your print messages.
# * Print does not have any log handlers. You cannot easily send your print messages to different destinations.
# * Print does not have any log formatters. You cannot easily customize the appearance and content of your print messages.
# * Print does not have any log filters. You cannot easily filter out unwanted print messages.
# 
# In a real-world application, you should use logging over print statements for the following reasons:
# 
# * Logging is more flexible and configurable than print. You can adjust the logging system according to your needs and preferences.
# * Logging is more informative and descriptive than print. You can add more details and context to your log messages.
# * Logging is more reliable and consistent than print. You can ensure that your log messages are recorded and stored properly.
# * Logging is more professional and standard than print. You can follow the best practices and conventions for logging information in production code.

# # Q10. Write a Python program that logs a message to a file named "app.log" with the following requirements:
# ### ● Thelogmessage should be "Hello, World!"
# ### ● Theloglevel should be set to "INFO."
# ### ● Thelogfile should append new log entries without overwriting previous ones.

# One possible Python program that logs a message to a file named “app.log” with the given requirements is:

# In[4]:


# Import the logging module
import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the logging level to INFO
logger.setLevel(logging.INFO)

# Create a file handler object
file_handler = logging.FileHandler("app.log", mode="a")

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log the message "Hello, World!"
logger.info("Hello, World!")


# # Q11. Create a Python program that logs an error message to the console and a file named "errors.log" if an exception occurs during the program's execution. The error message should include the exception type and a timestamp

# One possible Python program that logs an error message to the console and a file named “errors.log” if an exception occurs during the program’s execution is:

# In[8]:


# Import the logging module
import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the logging level to ERROR
logger.setLevel(logging.ERROR)

# Create a console handler object
console_handler = logging.StreamHandler()

# Create a file handler object
file_handler = logging.FileHandler("errors.log", mode="a")

# Create a formatter object with the exception type and a timestamp
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(exc_info)s")

# Set the formatter on both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Try to execute some code that may raise an exception
try:
  # Try to divide by zero
  result = 10 / 0
except Exception as e:
  # Log the error message using the logger object
  logger.error(f"An exception occurred: {e}")


# In[ ]:




