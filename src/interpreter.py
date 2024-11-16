import csv
from bs4 import BeautifulSoup

# Storage for HTML content and data tables
tables = {}

# A class for handling the TabloLang commands
class TabloLangInterpreter:
    def __init__(self):
        self.current_html = None
        self.last_selection = None

    def execute_command(self, command):
        global tables
        parts = command.strip().split()
        command_type = parts[0]

        if command_type == "LOAD_HTML":
            # Command: LOAD_HTML "file.html"
            filename = parts[1].strip('"')
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    html_content = file.read()
                    self.current_html = BeautifulSoup(html_content, 'html.parser')
                print(f"HTML loaded from {filename}")
            except FileNotFoundError:
                print(f"File not found: {filename}")

        elif command_type == "SELECT":
            # Command: SELECT "tag_name"
            selector = parts[1].strip('"')
            if self.current_html:
                self.last_selection = self.current_html.select(selector)
                print(f"Selected elements with selector: {selector}")
            else:
                print("No HTML loaded. Use LOAD_HTML first.")

        elif command_type == "EXTRACT":
            # Command: EXTRACT "attribute" TO table_name
            if not self.last_selection:
                print("No elements selected. Use SELECT first.")
                return

            attribute = parts[1].strip('"')
            table_name = parts[3]
            if table_name not in tables:
                tables[table_name] = []

            # Extracting the specified attribute from selected elements
            for element in self.last_selection:
                if attribute == "text":
                    data = element.get_text().strip()
                else:
                    data = element.get(attribute, "").strip()

                if data:
                    tables[table_name].append([data])

            print(f"Data extracted to table: {table_name}")

        elif command_type == "SAVE_TABLE":
            # Command: SAVE_TABLE table_name TO "file.csv"
            table_name = parts[1]
            filename = parts[3].strip('"')
            if table_name in tables:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    for row in tables[table_name]:
                        writer.writerow(row)
                print(f"Table {table_name} saved to {filename}")
            else:
                print(f"Table {table_name} does not exist")

        elif command_type == "DISPLAY_TABLE":
            # Command: DISPLAY_TABLE table_name
            table_name = parts[1]
            if table_name in tables:
                print(f"Displaying table {table_name}:")
                for row in tables[table_name]:
                    print(row)
            else:
                print(f"Table {table_name} does not exist")

        else:
            print(f"Unknown command: {command_type}")

# Example usage of the interpreter
def main():
    # Initialize the TabloLang Interpreter
    interpreter = TabloLangInterpreter()

    # Sample commands to demonstrate functionality
    commands = [
        'LOAD_HTML "form.html"',
        'SELECT "input"',
        'EXTRACT "name" TO user_data',
        'EXTRACT "value" TO user_data',
        'SAVE_TABLE user_data TO "user_data.csv"',
        'DISPLAY_TABLE user_data'
    ]

    # Execute each command
    for cmd in commands:
        interpreter.execute_command(cmd)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
