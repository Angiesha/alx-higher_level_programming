Resources
Read or watch:

How To Create a New User and Grant Permissions in MySQL
How To Use MySQL GRANT Statement To Grant Privileges To a User
MySQL constraints
SQL technique: subqueries
Basic query operation: the join
SQL technique: multiple joins and the distinct keyword
SQL technique: join types
SQL technique: union and minus
MySQL Cheat Sheet
The Seven Types of SQL Joins
MySQL Tutorial
SQL Style Guide
MySQL 8.0 SQL Statement Syntax
Extra resources around relational database model design:
[2;2R[3;1R
Design
Normalization
[>77;30601;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000ER Modeling
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
More Info
Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
In the container, credentials are root/root

How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

Python - if/else, loops, functions
In this project, I began utilizing conditionals and loops in Python by using if, if ... else, break, continue, pass, and range statements with while and for loops. I practiced writing my own Python functions while learning about scope of variables, tracebacks, and arithmetic operators.

Function Prototypes floppy_disk
Prototypes for functions written in this project:

File	Prototype
7-islower.py	def islower(c):
8-uppercase.py	def uppercase(str):
9-print_last_digit.py	def print_last_digit(number):
10-add.py	def add(a, b):
11-pow.py	def pow(a, b):
12-fizzbuzz.py	def fizzbuzz():
13-insert_number.c	listint_t *insert_node(listint_t **head, int number);
101-remove_char_at.py	def remove_char_at(str, n):
102-magic_calculation.py	def magic_calculation(a, b, c):
Tasks page_with_curl
0. Positive anything is better than negative nothing mandatory

0-positive_or_negative.py: Python program that assigns a random signed number to the variable number each time it is executed and prints whether number is positive or negative.
Prints the number followed by:
If the number is greater than 0: is positive
If the number is 0: is zero
If the number is less than 0: is negative
Followed by a new line.
Completion of this source code.
1. The last digit mandatory

1-last_digit.py: Python program that assigns a random signed number to the variable number each time it is executed and prints its last digit.
Prints the string Last digit of [number] is [last_digit] followed by:
If the number is greater than 5: and is greater than 5
If the number is 0: and is 0
If the number is less than 6 and not 0: and is less than 6 and not 0
Followed by a new line.
Completion of this source code.
2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game mandatory

2-print_alphabet.py: Python program that prints the alphabet in lowercase, not followed by a new line.
Using only one print and one loop.
Storing characters in variables or importing modules not allowed.
3. When I was having that alphabet soup, I never thought that it would pay off mandatory

3-print_alphabt.py: Python program that prints the alphabet in lowercase, followed by a new line.
Using only one print and one loop.
Without storing characters in variables or importing modules.
Prints every letter except for q and e.
4. Hexadecimal printing mandatory

4-print_hexa.py: Python program that prints all numbers from 0 to 98 in decimal and hexadecimal.
Using only one print and one loop.
Without storing numbers or strings in variables or importing modules.
Printing format: [decimal] = [hexadecimal]
5. 00...99 mandatory

5-print_comb2.py: Python program that prints numbers from 0 to 99 two digits each.
Numbers are separated by , , except for the last number, which is followed by a new line.
Using no more than two print functions and one loop.
Without storing numbers or strings in variables or importing modules.
6. Inventing is a combination of brains and materials. The more brains you use, the less material you need mandatory

6-print_comb3.py: Python program that prints all possible different combinations of two digits in ascending order.
Numbers are separated by , , except for the last number, which is followed by a new line.
The two digits must be different - 01 and 10 are considered identical.
Using no more than three print functions and two loops.
Without storing numbers or strings in variables or importing modules.
7. islower mandatory

7-islower.py: Python function that checks for lowercase characters.
Returns True if c is lowercase, False otherwise.
Without importing modules or using str.upper() or str.isupper().
8. To uppercase mandatory

8-uppercase.py: Python function that prints a string in uppercase followed by a new line.
Using no more than two print functions and one loop.
Without importing modules or using str.upper() or str.isupper().
9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important mandatory

9-print_last_digit.py: Python function that prints the last digit of a number.
Returns the value of the last digit.
Without importing modules.
10. a + b mandatory

10-add.py: Python function that returns the addition of two integers.
Without importing modules.
11. a ^ b mandatory

11-pow.py: Python function that returns a to the power of b.
Without importing modules.
12. Fizz Buzz mandatory

12-fizzbuzz.py: Python function that prints the numbers from 1 to 100 followed by a space.
For multiples of three, Fizz is printed instead of the number.
For multiples of five, Buzz is printed instead of the number.
For multiples of three and five, FizzBuzz is printed instead of the number.
Without importing modules.
13. Insert in sorted linked list mandatory

13-insert_number.c: C function that inserts a number into a sorted linked list.
If the function fails, returns NULL.
Otherwise, returns the address of the new node.
Helper files:
linked_lists.c: C functions handling linked lists for testing 13-insert_number.c (provided by Holberton School).
lists.h: Header file containing definitions and prototypes for all types and functions used in linked_lists.c and 13-insert_number.c.
14. Smile in the mirror #advanced

100-print_tebahpla.py: Python program that prints the alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line.
Using only one print and one loop.
Without storing characters in variables or importing modules.
15. Remove at position #advanced

101-remove_char_at.py: Python function that creates a copy of a string without the character at position n.
Without importing modules.
16. ByteCode -> Python #2 #advanced

102-magic_calculation.py: Python function matching exactly a bytecode provided by Holberton School.
