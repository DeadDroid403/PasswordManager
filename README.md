
# PasswordManager

This Is a Password Manager Written in Python.
We Are Using MySQL Database For Storing Our Passwords.


## Documentation

Introduction:

This documentation outlines the usage and implementation details of a Python Password Manager project. The Password Manager securely stores passwords in a MySQL database in encrypted format. The passwords are encrypted using strong cryptographic techniques and cannot be decrypted without accessing the script it.

Features:

1. Secure storage of passwords: Passwords are stored in a MySQL database in encrypted format, ensuring the security of sensitive information.

2.  User-friendly interface: The Password Manager provides a simple and intuitive interface for users to manage their passwords efficiently.

3. Strong encryption: Passwords are encrypted using robust cryptographic algorithms, making it virtually impossible for unauthorized users to access the passwords without accessing the script itself.

Requirements:

   1. Python 3.x
   2. MySQL database
   3. mysql.connector library for Python (to interact with MySQL)

## Usage

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DeadDroid401/PasswordManager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd PasswordManager
    ```

3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Modify the `base.py` script to include your MySQL database credentials (host, username, password).
2. Run the `base.py` script to create the necessary database and table.
3. Modify the `pass.py` script to include your MySQL database credentials (host, username, password) in two places.

### Usage

1. Run the `pass.py` script using Python3:
    ```bash
    python3 pass.py
    ```

2. Follow the on-screen instructions to add, retrieve, update, or delete passwords.

### Security Considerations

1. **Encryption**: Passwords are stored in encrypted format using strong cryptographic algorithms. Even if the database is compromised, the passwords cannot be decrypted without accessing the script itself.
  
2. **Database Security**: Ensure proper access control and permissions are set up for the MySQL database to prevent unauthorized access.

3. **Secure Script Handling**: Keep the `pass.py` script secure and limit access to authorized users only.

4. **Regular Backups**: Perform regular backups of the MySQL database to prevent data loss.

### Example

Here's a brief example of using the Password Manager:

1. Run the `pass.py` script.
2. Choose an option from the menu (e.g., add a new password, list all passwords).
3. Follow the prompts to perform the desired operation.

### Limitations

1. **Dependence on Python and MySQL**: The Password Manager relies on Python and MySQL, so ensure compatibility and availability of these dependencies.

2. **Single User**: The current implementation is suitable for a single-user environment. For multi-user support, additional authentication and access control mechanisms would need to be implemented.

3. **No Password Recovery Mechanism**: Since passwords are encrypted and cannot be decrypted without accessing the script, there is no password recovery mechanism. Users must ensure they remember their master password.

