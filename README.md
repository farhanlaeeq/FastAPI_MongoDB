# FastAPI_MongoDB

## Overview

This project is a Python-based backend API for an ERP (Enterprise Resource Planning) portal, built using FastAPI and MongoDB as the database. The project follows best code practices and utilizes MongoDB aggregation pipelines for complex queries and reports.

## Architecture

The code architecture is modular and follows a controller-based structure. Separate controllers have been created for each module, including:

* **EmployeeManagement**: Handles employee-related operations
* **Departments**: Manages department-related data and operations
* **Salary**: Handles salary-related operations and calculations
* **Roles**: Manages user roles and access control
* **Authentication**: Handles user authentication and authorization

This modular structure allows for easy maintenance, scalability, and reusability of code.

## Technology Stack

* **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
* **MongoDB**: A NoSQL database used for storing and retrieving data.
* **MongoDB Aggregation Pipelines**: Used for complex queries and report generation.

## Features

* Modular code structure with separate controllers for each module
* Utilizes MongoDB aggregation pipelines for complex queries and reports
* Follows best code practices for maintainability and scalability

## Getting Started

To run this project, you'll need to have Python and MongoDB installed on your system. Follow these steps:

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Start the FastAPI server using `uvicorn main:app --host 0.0.0.0 --port 8000`
4. Access the API documentation at `http://localhost:8000/docs`
