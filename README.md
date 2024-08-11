# Password Manager with Tkinter

## Overview

This project is a Password Manager built using Tkinter for the graphical user interface. It allows users to generate strong, random passwords and securely store them alongside associated website and email information. It also allows users to store pre-existing passwords. The passwords are stored in a JSON file, which can be searched later to retrieve saved credentials.


[Watch the video](https://github.com/user-attachments/assets/96d6fd59-19ed-41ff-8293-012d9735c310)



## Features

- **Password Generation**: Generates strong and random passwords using a combination of letters, numbers, and symbols.
- **Secure Storage**: Saves website credentials (website, email, password) to a JSON file (`data.json`).
- **Search Functionality**: Allows users to search for existing credentials by website name.
- **User-Friendly Interface**: Built using Tkinter, providing an intuitive and easy-to-use graphical interface.
- **Clipboard Functionality**: Copies the generated password to the clipboard for easy pasting.

## Requests

- Python 3.x
- Tkinter (usually included with Python)
- Pyperclip (for copying to clipboard)

## Installation

To run the Password Manager on your machine:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/password-manager.git

2. Navigate to the project directory: 
   ```bash
   cd password-manager

3. Install required dependencies:
   ```bash
   pip install pyperclip
   
4. Run the application: python main.py
   ```bash
   python main.py

## How to Use:

**Generating a Password**:

1. Click the "Generate Password" button to create a new strong password.
The password will be copied to your clipboard automatically.
Save the Password:

**Entering login details**:

2. Enter the website name, email/username, and the generated password.
Click the "Add" button to save the credentials to data.json.

**Searching for Saved Credentials**:

3. Enter the website name in the "Website" field. Click the "Search" button to retrieve the saved email and password for that website.


