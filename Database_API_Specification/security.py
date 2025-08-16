"""
Injection vulnerabilities have been one of the most common types of vulnerabilities for many years.
SQL injection is a common form of injection vulnerability which occurs when untrusted data is used to build a query string without sufficiently sanitizing and or escaping the provided data.

"""


# Prompt a user to enter a name to lookup.
animal_name = input('Enter a name to lookup: ')
# Add the user-supplied name into the query
cursor.execute(f"SELECT Animal, Name FROM Animal WHERE Name = '{animal_name}';")
# Additional code here
...

"""
Providing a valid username produces the correct results. For example specifying the name Ada builds the following query:

SELECT Animal, Name FROM Animal WHERE Name = 'Ada';

Providing malicious input allows an attacker to change the query. For example specifying the value ' or 1=1; -- builds the following query:

SELECT Animal, Name FROM Animal WHERE Name = '' or 1=1; --';
"""

