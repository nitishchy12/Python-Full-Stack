with open("logs.txt", "r") as file_:
    for line in file_:
        print(line.strip())

with open("file2.txt", "w")as file_:
    file_.write("Hello World3")

with open("file2.txt", "a")as file_:
     file_.write("Hello world4\n")


## using try catch
# Reading from logs.txt
try:
    with open("logs.txt", "r") as file_:
        for line in file_:
            print(line.strip())
except FileNotFoundError:
    print("logs.txt not found.")
except Exception as e:
    print(f"An error occurred while reading: {e}")

# Writing to file2.txt
try:
    with open("file2.txt", "w") as file_:
        file_.write("Hello World3\n")
except Exception as e:
    print(f"An error occurred while writing: {e}")

# Appending to file2.txt
try:
    with open("file2.txt", "a") as file_:
        file_.write("Hello world4\n")
except Exception as e:
    print(f"An error occurred while appending: {e}")



