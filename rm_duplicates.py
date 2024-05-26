import hashlib
import os
import sys

# Function to get the hash of a file
def get_file_hash(file_path, hash_algorithm="md5"):
    """
    Returns the hash of a file using the specified hash algorithm.
    """
    hash_func = getattr(hashlib, hash_algorithm)
    with open(file_path, "rb") as f:
        file_hash = hash_func(f.read()).hexdigest()
    return file_hash

# Function to find all duplicate files in a directory
def find_duplicate_files(directory, hash_algorithm="md5"):
    """
    Finds all duplicate files in a directory using the specified hash algorithm.
    """
    hashes = {}
    duplicate_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path):
                try:
                    file_hash = get_file_hash(file_path, hash_algorithm)

                    if file_hash in hashes:
                        duplicate_files.append((file_path, hashes[file_hash]))
                    else:
                        hashes[file_hash] = file_path
                except Exception as e:
                    if not quiet_mode:
                        print(f"Error hashing file {file_path}: {e}")

    return duplicate_files

# Function to replace the duplicate files with symbolic links
def replace_duplicate_files(duplicate_files):
    """
    Replaces the duplicate files with symbolic links.
    """
    for duplicate, original in duplicate_files:
        try:
            os.remove(duplicate)
            os.symlink(original, duplicate)
            if not quiet_mode:
                print(f"Replaced file: {duplicate} with link to {original}")
        except Exception as e:
            if not quiet_mode:
                print(f"Error replacing file {duplicate}: {e}")

# Menu
def main():
    global quiet_mode
    global hash_algorithm

    quiet_mode = False
    hash_algorithm = "md5"

    while True:
        print("\nDuplicate File Remover")
        print("----------------------")
        print("1. Select Directory")
        print("2. Quiet Mode")
        print("3. Change Hash Algorithm")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = input("Enter the directory to search: ")
            duplicate_files = find_duplicate_files(directory, hash_algorithm)
            if not quiet_mode:
                for duplicate, original in duplicate_files:
                    print(f"Duplicate: {duplicate}, Original: {original}")
            replace_duplicate_files(duplicate_files)
        elif choice == "2":
            quiet_mode = not quiet_mode
            print(f"Quiet Mode {'enabled' if quiet_mode else 'disabled'}")
        elif choice == "3":
            hash_algorithm = input("Enter the hash algorithm (md5, sha1, sha256): ").lower()
            if hash_algorithm not in ["md5", "sha1", "sha256"]:
                print("Invalid hash algorithm. Please enter 'md5', 'sha1', or 'sha256'.")
                hash_algorithm = "md5"
        elif choice == "4":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
