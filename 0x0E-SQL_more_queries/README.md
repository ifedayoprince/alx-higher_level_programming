# 0x0E. SQL - More Queries

## Description

This project focuses on advanced SQL queries, specifically within the MySQL database management system. It aims to enhance your understanding and skills in managing database users, constraints, subqueries, joins, unions, and more. By the end of this project, you will be able to create and manage MySQL users, apply various SQL constraints, and perform complex queries involving multiple tables.

## Project Details

- **Project Duration**: May 22, 2024 - May 24, 2024
- **Weight**: 1
- **Auto QA Review**: 0.0/96 mandatory & 0.0/24 optional
- **Overall Calculation**: 0.0%

## Learning Objectives

At the end of this project, you should be able to explain the following concepts without external help:

- Creating a new MySQL user
- Managing privileges for a user to a database or table
- Understanding PRIMARY KEY and FOREIGN KEY
- Using NOT NULL and UNIQUE constraints
- Retrieving data from multiple tables in one request
- Understanding subqueries
- Using JOIN and UNION


## Tasks

1. **My privileges!**
   - Script to list all privileges of `user_0d_1` and `user_0d_2` on your server.

2. **Root user**
   - Script to create MySQL user `user_0d_1` with all privileges.

3. **Read user**
   - Script to create database `hbtn_0d_2` and user `user_0d_2` with SELECT privilege.

4. **Always a name**
   - Script to create table `force_name` with `id INT` and `name VARCHAR(256)` that can’t be null.

5. **ID can't be null**
   - Script to create table `id_not_null` with `id INT` default 1 and `name VARCHAR(256)`.

6. **Unique ID**
   - Script to create table `unique_id` with `id INT` unique and `name VARCHAR(256)`.

7. **States table**
   - Script to create database `hbtn_0d_usa` and table `states` with `id INT` as primary key.

8. **Cities table**
   - Script to create table `cities` with `id INT` as primary key and `state_id INT` as foreign key.

9. **Cities of California**
   - Script to list all cities of California in the database `hbtn_0d_usa`.

10. **Cities by States**
    - Script to list all cities in the database `hbtn_0d_usa`.

11. **Genre ID by show**
    - Script to list all shows in `hbtn_0d_tvshows` with at least one genre.

12. **Genre ID for all shows**
    - Script to list all shows in `hbtn_0d_tvshows`.

13. **No genre**
    - Script to list all shows in `hbtn_0d_tvshows` without a genre.

## Repository

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x0E-SQL_more_queries`

Each task's corresponding SQL script should be placed within this directory and follow the naming conventions specified in the task descriptions.
