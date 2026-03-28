import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("❌ Error: File not found.")
        return None


def main():
    file_path = input("Enter file path: ").strip()

    # Check if file exists
    if not os.path.exists(file_path):
        print("❌ File does not exist!")
        return

    print("\nCalculating original hash...")
    original_hash = calculate_hash(file_path)

    if original_hash is None:
        return

    print("Original Hash:", original_hash)

    input("\n👉 Modify the file if you want, then press ENTER...\n")

    print("Re-checking file...")
    new_hash = calculate_hash(file_path)

    print("New Hash:", new_hash)

    if original_hash == new_hash:
        print("\n✅ File NOT modified")
    else:
        print("\n⚠️ File has been MODIFIED!")


if __name__ == "__main__":
    main()