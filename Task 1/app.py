import os
import sys
from datetime import datetime

def get_top_files(path, top_n=10):
    """Получает топ N самых больших файлов в указанной директории."""
    files = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            try:
                filesize = os.path.getsize(filepath) / 1024 
                files.append((filepath, filesize))
            except OSError:
                pass  
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:top_n]

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "User"
        
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}!")
    print(f"Current time: {current_time}")
    path = input("Enter the path to analyze (default is '/'): ").strip() or "/"

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return

    total_files = sum(len(files) for _, _, files in os.walk(path))
    print(f"Total number of files: {total_files}")

    top_files = get_top_files(path)
    print("Top 10 largest files (in KB):")
    for filepath, filesize in top_files:
        print(f"{filepath}: {filesize:.2f} KB")

if __name__ == "__main__":
    main()
