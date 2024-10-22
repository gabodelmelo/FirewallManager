import subprocess
import os
import datetime

LOG_FILE = "firewall_manager.log"

# Function to execute system commands
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

# Function to list current firewall rules
def list_rules():
    print("Listing current firewall rules...")
    command = "sudo iptables -L"
    output = run_command(command)
    print(output)

# Function to add a firewall rule
def add_rule(protocol, port, action='ACCEPT'):
    print(f"Adding rule: {action} {protocol} traffic on port {port}")
    command = f"sudo iptables -A INPUT -p {protocol} --dport {port} -j {action}"
    output = run_command(command)
    if output == "":
        print("Firewall rule added successfully.")
        log_action("Add", f"Added rule: {action} {protocol} traffic on port {port}")
    else:
        print(f"Error adding firewall rule: {output}")
        log_action("Error", f"Failed to add rule: {action} {protocol} traffic on port {port}. Error: {output}")

# Function to delete a firewall rule
def delete_rule(protocol, port):
    print(f"Deleting rule: {protocol} traffic on port {port}")
    command = f"sudo iptables -D INPUT -p {protocol} --dport {port} -j ACCEPT"
    output = run_command(command)
    if output == "":
        print("Firewall rule deleted successfully.")
        log_action("Delete", f"Deleted rule: {protocol} traffic on port {port}")
    else:
        print(f"Error deleting firewall rule: {output}")
        log_action("Error", f"Failed to delete rule: {protocol} traffic on port {port}. Error: {output}")

#Function to save firewall rules
def save_rules():
    filename = input("Enter the name for saving the firewall rules (without extension): ")
    filepath = f"{filename}.rules"

    if os.path.exists(filepath):
        overwrite = input(f"The file '{filepath}' already exists. Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("Aborting save operation.")
            return
    
    print(f"Saving firewall rules to {filepath}...")
    command = f"sudo iptables-save > {filepath}"
    output = run_command(command)

    if output == "":
        print("Firewall rules saved.")
        log_action("Save", f"Firewall rules saved to {filepath}")
    else:
        print(output)
        log_action("Error", f"Failed to save firewall rules to {filepath}. Error: {output}")

#Function to restore firewall rules
def restore_rules():
    print("Listing all saved firewall rules (.rules files):")
    
    # List all files with .rules extension in the current directory
    rules_files = [f for f in os.listdir() if f.endswith('.rules')]
    
    if not rules_files:
        print("No saved firewall rules found.")
        return

    # Display the list of saved rule files
    for idx, file in enumerate(rules_files, 1):
        print(f"{idx}. {file}")

    # Ask the user to choose a file by number
    try:
        choice = int(input(f"Enter the number of the file to restore (1-{len(rules_files)}): ")) - 1
        if choice < 0 or choice >= len(rules_files):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input, please enter a number.")
        return

    # Get the selected file
    selected_file = rules_files[choice]
    print(f"Restoring firewall rules from {selected_file}...")

    # Restore the selected file using iptables-restore
    command = f"sudo iptables-restore < {selected_file}"
    output = run_command(command)

    if output == "":
        print("Firewall rules restored.")
        log_action("Restore", f"Firewall rules restored from {selected_file}")
    else:
        print(f"Error restoring firewall rules: {output}")
        log_action("Error", f"Failed to restore firewall rules from {selected_file}. Error: {output}")



# Function to log actions
def log_action(action, details=""):
    # Check if the log file exists; if not, create it
    if not os.path.exists(LOG_FILE):
        # Create the log file
        with open(LOG_FILE, "w") as log_file:
            log_file.write("Firewall Manager Log Created\n")
    
    # Append the new log entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {action}: {details}\n"
    
    # Write the log entry to the log file
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

# Function to view the last 20 log entries
def view_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs available.")
        return

    with open(LOG_FILE, "r") as log_file:
        logs = log_file.readlines()

    # Show the latest 20 log entries (or fewer if there aren't that many)
    print("Last 20 log entries:")
    for line in logs[-20:]:
        print(line.strip())

# Main function
if __name__ == "__main__":
    while True:
        print("\nFirewall Manager")
        print("1. List firewall rules")
        print("2. Add firewall rule")
        print("3. Delete firewall rule")
        print("4. Save actual firewall rules")
        print("5. Restore firewall rules")
        print("6. View latest 20 logs")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_rules()
        elif choice == '2':
            protocol = input("Enter protocol (tcp/udp): ")
            port = input("Enter port number: ")
            add_rule(protocol, port)
        elif choice == '3':
            protocol = input("Enter protocol (tcp/udp): ")
            port = input("Enter port number: ")
            delete_rule(protocol, port)
        elif choice == '4':
            save_rules()
        elif choice == '5':
            restore_rules()
        elif choice == '6':
            view_logs()
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")
