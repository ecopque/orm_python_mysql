# Exploring the Power of ORM with Python and MySQL

This project demonstrates the implementation of a full data manipulation system using **Python**, **MySQL**, and the powerful technique of **ORM** (Object-Relational Mapping).

## What is ORM?

**ORM** is a technique that allows interaction between object-oriented applications and relational databases without manually writing SQL queries. Instead, we define classes and objects to represent tables and rows in the database. This abstraction layer enhances code maintainability and readability, simplifying database operations.

## Tools Used

- **Python**: The main programming language used in the project.
- **MySQL**: The relational database system used for storing data.
- **SQLAlchemy ORM**: A library that allows mapping Python classes to MySQL tables and performing CRUD operations efficiently.

## What I Learned and Implemented

- **Table Creation**: Defined Python classes to represent tables in the database, with columns of types like `String`, `Integer`, and relationships such as foreign keys.
- **Table Relationships**: Used foreign keys to associate products with categories, demonstrating one-to-many relationships.
- **CRUD Operations**: Implemented create, read, update, and delete operations through Python, eliminating the need for direct SQL queries. 
    - Examples include adding new records, querying data with filters, and updating records with a single command.
- **Database Integration**: Configured the connection to the MySQL database, managing data with Python and SQLAlchemy.

## Objective

This project is designed to optimize data handling processes in real-world applications, providing a more efficient and modular approach to working with databases. By using ORM, database interactions become more intuitive and maintainable, which is essential for scalable projects.
