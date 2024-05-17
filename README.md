# MEDIA MANAGER
#### Video Demo:  https://youtu.be/-lMwoklfonc
## Description:
Media Manager is a web application written with flask framework, designed to help users organize their favorite books, movies, and TV shows. The application allows users to create lists of their favorite media and plan for future consumption.
## Files Overview
### requirements.txt

This file specifies the Python packages required for the project. It includes cs50, Flask, and Flask-Session.
### books.html

This HTML file represents the template for managing favorite books. Users can add their favorite books and future reads, as well as remove items from these lists. The page has a clean and user-friendly interface with two input forms for adding books.
### contact.html

This HTML file serves as the template for the contact page. Users can send messages by providing their email address and a brief message. The page includes a form with fields for email and message, making it easy for users to reach out.
### index.html

The index page introduces users to Media Manager. It provides a brief description of the application and highlights its main features—organizing books, movies, and TV shows. Users can navigate to specific sections by clicking on corresponding buttons.
### layout.html

This HTML file defines the overall structure and layout of the web pages. It includes navigation links, a header, main content, and a footer. The navigation bar adjusts based on whether a user is logged in or not.
### login.html

This file presents the login form where users can log in to their accounts. It includes fields for entering a username and password. Upon successful login, users are redirected to the home page.
### message_sent.html

This HTML file is a confirmation page displayed after a user successfully sends a message through the contact form. It thanks the user and assures them that their message has been sent.
### movies.html

Similar to books.html, this HTML file provides a template for managing favorite movies and future watches. Users can add, remove, and view their lists of favorite movies and planned future watches.
### register.html

This file contains the registration form where users can create a new account. It includes fields for choosing a username and password. Upon successful registration, users are automatically logged in.
### app.py

The main Python script contains the application logic. It uses the Flask framework and interacts with a SQLite database (final.db). The script includes routes for managing books, movies, contact messages, user registration, login, and logout.
### helpers.py

This module contains helper functions used by app.py. The apology function renders error messages in a standardized format. The login_required decorator ensures that certain routes require user authentication.
## Usage

    Install the required packages using pip install -r requirements.txt.
    Run the application by executing python app.py or flask run.
    Open your web browser and navigate to http://localhost:5000 to access Media Manager.

## Features

    Organize Books, Movies, and TV Shows: Users can create lists of their favorite books, movies, and TV shows.
    Plan for Future Consumption: The application allows users to plan for future reads and watches by adding items to respective lists.
    User Authentication: Users can register, log in, and log out to personalize their experience.
    Contact Form: Users can send messages and inquiries through the contact form.
    Responsive Design: The web pages are designed to be responsive and accessible on different devices.

Media Manager offers a user-friendly interface and a set of features to enhance the organization of media preferences.
