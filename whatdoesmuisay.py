import os
import winreg
import csv

def read_mui_cache():
    # Define the registry paths
    registry_paths = [
        r'Local Settings\Software\Microsoft\Windows\Shell\MuiCache',
        r'Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache'
    ]

    # Dictionary to store the results
    mui_cache_data = {}

    # Read the MUI Cache from each registry path
    for path in registry_paths:
        try:
            # Choose the appropriate registry root
            root_key = winreg.HKEY_CURRENT_USER if 'Classes' in path else winreg.HKEY_CLASSES_ROOT
            key = winreg.OpenKey(root_key, path, 0, winreg.KEY_READ)
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                value = winreg.EnumValue(key, i)
                mui_cache_data[value[0]] = value[1]
            winreg.CloseKey(key)
        except FileNotFoundError:
            print(f"Registry path {path} not found.")
        except Exception as e:
            print(f"Error reading registry path {path}: {str(e)}")

    return mui_cache_data

def save_to_csv(data, filename='mui_cache.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Path', 'MUI Cache Entry'])
        for key, value in data.items():
            writer.writerow([key, value])
    print(f"Data saved to {filename}")

def main():
    print("Reading MUI Cache...")
    mui_cache_data = read_mui_cache()
    if mui_cache_data:
        print(f"Found {len(mui_cache_data)} entries.")
        save_to_csv(mui_cache_data)
    else:
        print("No entries found.")

if __name__ == "__main__":
    main()
