import requests

BASE_URL = "http://127.0.0.1:8000"

def create_issue():
    title = input("Enter title: ")
    description = input("Enter description: ")
    issue = {"title": title, "description": description}
    response = requests.post(f"{BASE_URL}/issues/", json=issue)
    
    if response.status_code == 200:  # Check if status code indicates success
        print(response.json())
    else:
        print(f"Error with status code {response.status_code}: {response.text}")


def read_issues():
    response = requests.get(f"{BASE_URL}/issues/")
    issues = response.json()
    for issue in issues:
        print(issue)

def update_issue():
    issue_id = int(input("Enter issue id to update: "))
    title = input("Enter new title: ")
    description = input("Enter new description: ")
    issue_data = {"title": title, "description": description}
    response = requests.put(f"{BASE_URL}/issues/{issue_id}", json=issue_data)
    print(response.json())

def delete_issue():
    issue_id = int(input("Enter issue id to delete: "))
    response = requests.delete(f"{BASE_URL}/issues/{issue_id}")
    print(response.json())

def main():
    while True:
        print("\nChoose operation:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_issue()
        elif choice == "2":
            read_issues()
        elif choice == "3":
            update_issue()
        elif choice == "4":
            delete_issue()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
