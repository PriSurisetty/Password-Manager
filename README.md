Password Manager with Tkinter:

Overview:

This project is a Password Manager built using Tkinter for the graphical user interface. It allows users to generate strong, random passwords and securely store them alongside associated website and email information; It also allows them to store their pre-existing passwords. The passwords are stored in a JSON file, which can be searched later to retrieve saved credentials.

Features:
- Password Generation: Generates strong and random passwords using a combination of letters, numbers, 
  and symbols.
- Secure Storage: Saves website credentials (website, email, password) to a JSON file (data.json).
- Search Functionality: Allows users to search for existing credentials by website name.
- User-Friendly Interface: Built using Tkinter, providing an intuitive and easy-to-use graphical 
  interface.
- Clipboard Functionality: Copies the generated password to the clipboard for easy pasting.

Requests:
- Python 3.x
- tkinter (usually included with Python)
- pyperclip (for copying to clipboard)

Installation:
1. Clone the repository: git clone https://github.com/your-username/password-manager.git
2. Navigate to the project directory: cd password-manager
3. Install required dependencies: pip install pyperclip
4. Run the application: python main.py

How to Use:

Generating a Password:

1. Click the "Generate Password" button to create a new strong password.
The password will be copied to your clipboard automatically.
Save the Password:

Entering login details:

2. Enter the website name, email/username, and the generated password.
Click the "Add" button to save the credentials to data.json.

Searching for Saved Credentials:

3. Enter the website name in the "Website" field. Click the "Search" button to retrieve the saved email and password for that website.

