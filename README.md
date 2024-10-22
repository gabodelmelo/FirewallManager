# FirewallManager.py

### Overview
The "Firewall Manager for Linux" is a Python-based script designed to provide users with an intuitive interface to manage their Linux-based firewall (iptables). This project aims to simplify the management of iptables, which can be complex for users not comfortable with Linux command-line operations. It offers features such as listing, adding, and deleting firewall rules, along with saving and restoring them from files. The script also includes enhanced logging functionality to help users track firewall changes over time, providing better accountability and ease of use.

### Key Objectives
The main objectives of the project were:
1. **User-friendly Interface**: To provide a simplified command-line interface for managing firewall rules.
2. **Basic Firewall Operations**: To enable easy listing, addition, and deletion of firewall rules for both TCP and UDP protocols.
3. **Persistence**: To allow users to save current firewall rules to a file and restore them when needed.
4. **Logging**: To log actions performed on the firewall and offer the ability to view recent logs for auditing purposes.
5. **Error Handling**: To provide clear and informative error messages when operations fail.

### Steps Taken
1. **Planning Phase**: Identified common tasks that users perform with iptables and designed the script to cover these key functions—listing, adding, and deleting firewall rules.
2. **Command Execution Function**: Developed a Python function using `subprocess` to securely execute system commands and handle errors.
3. **Feature Implementation**:
   - **Listing Rules**: Added functionality to display current firewall rules with `iptables -L`.
   - **Adding/Deleting Rules**: Implemented the addition of new rules and deletion of existing ones using the `iptables -A` and `iptables -D` commands, respectively. Enhanced success and error messages were included to inform users of the operation outcomes.
4. **Persistence Features**: Created functionality to save and restore firewall rules using `iptables-save` and `iptables-restore`. Implemented checks to prevent accidental overwriting of existing rule files.
5. **Logging System**: Developed a logging mechanism to store a history of actions in a log file, including error handling and timestamped entries.
6. **Testing**: Extensively tested the script to ensure it correctly performs firewall management tasks, accurately logs actions, and responds appropriately to errors.

### Outcome
The project successfully created a fully functional firewall management script for Linux. The script met all key objectives, offering a user-friendly way to handle firewall rules. It supports basic operations like adding/deleting rules, viewing firewall status, saving rules to a file, and restoring them when needed. The enhanced logging functionality provides helpful auditing of user actions, and robust error handling ensures that the script responds gracefully to issues.
