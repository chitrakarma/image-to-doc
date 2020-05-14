# IED - Images to Editable Documents [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
A simple project with a web interface for uploading image files, viewing the quivalent text output and downloading the same as a `.docx` file. This project is built with the aim to provide users with a handy easy-to-use tool which brings together the existing technologies to provide a solution to the problem of conversion of images to documents.


# Table of Contents
- [Languages](#languages)
- [Frameworks](#frameworks)
- [Project Management](#project-management)
- [Dependencies & Tools](#dependencies-and-tools)
- [Software](#software)
- [Environment Setup](#environment-setup)
- [Run IED Locally](#run-ied-locally)
- [Authors](#authors)
- [Licence](#license)
- [Acknowledgements](#acknowledgements)

## Languages
  - Python 3 - An Interpreted, High-level, General-Purpose Programming Language 
  - JS ES5 - High-level, Programming Language
  - HTML5 - Markup Language
  - CSS3 - Style Sheet Language 
 
## Frameworks
  - Flask - Micro Web Framework Written In Python
  - Bootstrap 4 - Open-Source CSS Front-End Framework
  - Slim - Fast & Lightweight Web-Components Microframework Written In JavaScript

## Project Management
  - `pip` CLI - Package-Management System Written In Python
  - Git - Distributed VCS
  - GitHub - For Collaboration, Bug-tracking, Feature-requests & Task-management
  
## Dependencies and Tools
  - Tesseract OCR - Open-Source OCR Engine
  - `pytesseract` - Python Wrapper For Tessract 
  - `python-docx` - Python Library to Create, Read & Write `docx` files
  - `virtualenv` - Tool to Create Isolated Python Environments
  - Popper - Positioning Engine Written In JavaScript
  - AJAX - Asynchronous JavaScript & XML
  - PIL - Python Image Library
  - OS - Python Library For Using OS Dependent Functionality
  - JSON - JavaScript Object Notation 
  
## Software
  - OS - Windows 10, Version 1903 (OS Build 18362.778)
  - Microsoft VS Code 1.44.2 - Text Editor
  - GitHub Desktop 2.4.2
  - Google Chrome Version 81.0.4044.138 - Web Browser
  
## Environment Setup
All instructions are only for users running Windows 10 OS

### Downloads
- [Python 3](https://www.python.org/downloads/)
- [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [GitHub Desktop](https://desktop.github.com/)
- [Google Chrome](https://www.google.com/chrome/)
- [Git Bash](https://git-scm.com/downloads)

Follow the installation steps and make sure you add python to your path, more of which can be found [here](https://geek-university.com/python/add-python-to-the-windows-path/)

### Installations

  > C:\Users\Username> pip install tesseract    
  > C:\Users\Username> pip install tesseract-ocr    
  > C:\Users\Username> pip install virtualenv    

This will install `virtualenv` `tesseract` & `tesseract-ocr` globally

## Run IED Locally
Clone or Download the repository in your local machine before proceeding
### Run Virtual Environment 
    > C:\Users\Username\Downloads> cd image-to-doc    
    > C:\Users\Username\Downloads\image-to-doc> activate.bat    
    > (venv) C:\Users\Username\Downloads\image-to-doc>    
### Installs 
    > (venv) C:\Users\Username> pip install Flask     
    > (venv) C:\Users\Username> pip install pytesseract    
    > (venv) C:\Users\Username> pip install python-docx      
### Run App
    > (venv) C:\Users\Username> start.bat  

Visit http://localhost:5000 on your local machine to see the Web App

## Authors
- **Chitransh S. Vishwakarma**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
