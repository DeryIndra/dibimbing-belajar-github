import csv

def read_csv_table(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            data = []
            for row in reader:
                data.append(row)
            
            return header, data
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    csv_file = 'example.csv'  # Replace with your CSV file path
    
    header, data = read_csv_table(csv_file)
    
    if header and data:
        print("Header:")
        print(header)
        print("\nData:")
        for row in data:
            print(row)
