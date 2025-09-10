studentList={}
def main():
    try: 
        fileInput = open("students.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
    except FileNotFoundError:
        print("File not found")
main()
def menu():
    while True:
        print("1: Search by last name" \
        "2: Search by major" \
        "q: Exit")
        choice=input("")
        if choice =="1":
            search_last_name()
        elif choice=="2":
            search_major()
        elif choice=="q":
            break 
        else:
            print("Invalid option ")
def search_last_name():
    key_lastname=input("Plese enter a last name:")
    for k in studentList:
        print(key_lastname)
def search_major():
    major_key=input("plese enter a major")
    for v in studentList:
        print(major_key)
