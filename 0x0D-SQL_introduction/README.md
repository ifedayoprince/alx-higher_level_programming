# 0x0D. SQL - Introduction

## Description

This project is an introduction to SQL using MySQL. It covers fundamental concepts and operations of databases, specifically focusing on relational databases and SQL commands. By the end of this project, you will be able to perform basic database operations such as creating databases, creating tables, inserting data, querying data, and more.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- The differences between DDL (Data Definition Language) and DML (Data Manipulation Language)
- How to create or alter a table
- How to select data from a table
- How to insert, update, or delete data
- What subqueries are
- How to use MySQL functions

## Project Tasks

### Mandatory Tasks

1. **List databases**
   - Write a script that lists all databases of your MySQL server.
   - File: `0-list_databases.sql`

2. **Create a database**
   - Write a script that creates the database `hbtn_0c_0` if it does not already exist.
   - File: `1-create_database_if_missing.sql`

3. **Delete a database**
   - Write a script that deletes the database `hbtn_0c_0` if it exists.
   - File: `2-remove_database.sql`

4. **List tables**
   - Write a script that lists all tables of a given database.
   - File: `3-list_tables.sql`

5. **Create a table**
   - Write a script that creates a table called `first_table` with `id` and `name` fields.
   - File: `4-first_table.sql`

6. **Full description**
   - Write a script that prints the full description of the table `first_table`.
   - File: `5-full_table.sql`

7. **List all in table**
   - Write a script that lists all rows of the table `first_table`.
   - File: `6-list_values.sql`

8. **First add**
   - Write a script that inserts a new row in the table `first_table`.
   - File: `7-insert_value.sql`

9. **Count 89**
   - Write a script that displays the number of records with `id = 89` in the table `first_table`.
   - File: `8-count_89.sql`

10. **Full creation**
    - Write a script that creates a table `second_table` and adds multiple rows.
    - File: `9-full_creation.sql`

11. **List by best**
    - Write a script that lists all records of `second_table` ordered by score.
    - File: `10-top_score.sql`

12. **Select the best**
    - Write a script that lists all records with a score >= 10 in `second_table`.
    - File: `11-best_score.sql`

13. **Cheating is bad**
    - Write a script that updates the score of Bob to 10 in `second_table`.
    - File: `12-no_cheating.sql`

14. **Score too low**
    - Write a script that removes all records with a score <= 5 in `second_table`.
    - File: `13-change_class.sql`

15. **Average**
    - Write a script that computes the average score of `second_table`.
    - File: `14-average.sql`

16. **Number by score**
    - Write a script that lists the number of records with the same score in `second_table`.
    - File: `15-groups.sql`

17. **Say my name**
    - Write a script that lists all records of `second_table` where the name is not NULL.
    - File: `16-no_link.sql`

### Advanced Tasks

18. **Go to UTF8**
    - Write a script that converts the database `hbtn_0c_0` to UTF8.
    - File: `100-move_to_utf8.sql`

19. **Temperatures #0**
    - Write a script that displays the average temperature by city.
    - File: `101-avg_temperatures.sql`

20. **Temperatures #1**
    - Write a script that displays the top 3 cities' temperatures during July and August.
    - File: `102-top_city.sql`

21. **Temperatures #2**
    - Write a script that displays the max temperature of each state.
    - File: `103-max_state.sql`

## Usage

To execute the SQL scripts, use the following command:

```sh
$ cat FILENAME.sql | mysql -hlocalhost -uroot -p DATABASENAME
```

Ensure MySQL is running and properly installed on your system.

## Repository

- GitHub repository: [alx-higher_level_programming](https://github.com/username/alx-higher_level_programming)
- Directory: `0x0D-SQL_introduction`

This README provides an overview of the project tasks, requirements, and usage instructions for the SQL - Introduction project. Follow the tasks sequentially to achieve the project objectives and gain a solid understanding of SQL with MySQL.
