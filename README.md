# PERSONAL_WEBSITE
- !/usr/bin/env python3
- -*- coding: utf-8 -*-
- Author: Russ T
- Created: September 2021

# description
This is my personal website which is built using Flask, HTML5, CSS, and some minor Javascript (for hamburger menu on mobile). The website displays my freelance information 
and several personal projects and publications. I built it using Flask on my local development server and deployed it on a PythonAnywhere server. The contact page form sends 
users requests to my personal email and also saves the data in an SQLite database which is kept on the deployed server. 

A custom domain was purchased from Google for this site.

https://www.russ-thorsteinsson.ca/

# version control (Git/GitHub)
All testing/ development is done on a local server. Code is then pushed to Github and then a pulled down into the PythonAnywhere servers.

# modules/ packages
- Flask
- sqlite3
- EmailMessage
- datetime
- smtplib

# website details
- built with Flask
- mobile responsive
- utilized HTML template inheritance in the application (for headers, footers, navbars, styles)
- utilized CSS grid architecture (makes mobile responsive transition simple)
- form submission page requires completeness from the user; the page reroutes back to the form, and flashes an error, if an incomplete submission is given (but saves partially completed info) 

# website scripts:
- portfolio_site.py: Flask application script, page routing, form handling.
- sql_database.py: supporting script to create database table for contact form (database created separately w/ GitBash)

# security
- website reads in personal email + password from a text file. This allows the form info to be submitted to me and also host scripts on GitHub public repository.

# example output of contact form
![db_img_for_GitHub](https://user-images.githubusercontent.com/87350911/137597399-d36dff5b-1c02-4943-9269-473fd592e9e6.png)
