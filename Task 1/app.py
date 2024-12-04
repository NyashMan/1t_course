import os
import sys
from datetime import datetime

# Путь к директории (по умолчанию корневой каталог файловой системы)
path = "/"
path = os.getcwd()  

def get_top_files(directory, top_n=10):
    file_sizes = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                file_sizes.append((file_path, size))
            except FileNotFoundError:
                pass
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    return file_sizes[:top_n]

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "User"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_files = sum(len(files) for _, _, files in os.walk(path))
    top_files = get_top_files(path)

    print(f"Hello, {name}!")
    print(f"Current time: {current_time}")
    print(f"Total number of files: {total_files}")
    print("Top 10 largest files (in KB):")
    for file_path, size in top_files:
        print(f"{file_path}: {size / 1024:.2f} KB")

if __name__ == "__main__":
    main()
