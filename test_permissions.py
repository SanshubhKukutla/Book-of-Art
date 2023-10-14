try:
    with open("pyscript.json", "r") as file:
        data = file.read()
        print("Successfully read the file:")
        print(data)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
