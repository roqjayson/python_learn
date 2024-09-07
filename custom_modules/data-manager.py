# data_manager.py

class DataManager:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        try:
            number = float(value)
            self.data.append(number)
            print("Data added successfully!")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def view_data(self):
        if not self.data:
            print("No data available.")
        else:
            print("Logged Data:")
            for i, value in enumerate(self.data, 1):
                print(f"Entry {i}: {value}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for number in self.data:
                file.write(f"{number}\n")
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.data = [float(line.strip()) for line in file]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("File not found. Starting with an empty data list.")
        except ValueError:
            print("File contains non-numeric data. Please check the file.")

    def calculate_statistics(self):
        if not self.data:
            print("No data available for analysis.")
            return
        mean_value = sum(self.data) / len(self.data)
        max_value = max(self.data)
        print(f"Mean: {mean_value:.2f}")
        print(f"Max: {max_value}")
