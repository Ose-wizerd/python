
# this is the perfect program whithout gui
def sequential_search(names, target, search_type):
    # Perform sequential search based on search type.
    for i, name in enumerate(names):
        first_name, last_name = name.split()
        if (
            (search_type == "full" and name == target) or
            (search_type == "first" and first_name == target) or
            (search_type == "last" and last_name == target)
        ):
            return i
    return -1

def binary_search(names, target, search_type):
    # Perform binary search based on search type.
    low, high = 0, len(names) - 1
    while low <= high:
        mid = (low + high) // 2
        first_name, last_name = names[mid].split()
        if (
            (search_type == "full" and names[mid] == target) or
            (search_type == "first" and first_name == target) or
            (search_type == "last" and last_name == target)
        ):
            return mid
        elif names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def simple_sort(names):
    return sorted(names)

def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

def selection_sort(names):
    n = len(names)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if names[j] < names[min_idx]:
                min_idx = j
        names[i], names[min_idx] = names[min_idx], names[i]
    return names

def insertion_sort(names):
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        while j >= 0 and key < names[j]:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key
    return names

def display_menu():
    print("\nMenu:")
    print("1. Add names")
    print("2. Sequential Search")
    print("3. Binary Search (requires sorted list)")
    print("4. Sort (Simple, Bubble, Selection, Insertion)")
    print("5. Display names")
    print("6. Exit")

def main():
    names = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Enter full names (first and last name), separated by commas.Example: John Doe, Jane Smith, ...")
            new_names = input("Enter names: ").split(",")
            
            invalid_input=False
            for name in new_names:
                if name.isdigit():
                    invalid_input=True
                    break
            if invalid_input:
                print("Error: Names should not contain numbers. Try again.")
            else:
                names.extend([name.strip() for name in new_names])
                print("Names added successfully!")
        elif choice == "2":
            if not names:
                print("The list is empty. Add names first.")
                continue
            print("Search Options:")
            print("1. By First Name")
            print("2. By Last Name")
            print("3. By Full Name")
            search_choice = input("Choose a search option: ")
            target = input("Enter the search term: ")
            search_type = (
                "first" if search_choice == "1" else
                "last" if search_choice == "2" else
                "full"
            )
            index = sequential_search(names, target, search_type)
            print(f"Name {'found at index ' + str(index) if index != -1 else 'not found'}")
        elif choice == "3":
            if not names:
                print("The list is empty. Add names first.")
                continue
            print("Search Options:")
            print("1. By First Name")
            print("2. By Last Name")
            print("3. By Full Name")
            search_choice = input("Choose a search option: ")
            target = input("Enter the search term: ")
            search_type = (
                "first" if search_choice == "1" else
                "last" if search_choice == "2" else
                "full"
            )
            sorted_names = simple_sort(names)
            index = binary_search(sorted_names, target, search_type)
            print(f"Name {'found at index ' + str(index) if index != -1 else 'not found'} in sorted list")
        elif choice == "4":
            print("Sort Options:")
            print("1. Simple Sort")
            print("2. Bubble Sort")
            print("3. Selection Sort")
            print("4. Insertion Sort")
            sort_choice = input("Choose a sort option: ")
            if sort_choice == "1":
                names = simple_sort(names)
                print("Sorted using Simple Sort.")
            elif sort_choice == "2":
                names = bubble_sort(names)
                print("Sorted using Bubble Sort.")
            elif sort_choice == "3":
                names = selection_sort(names)
                print("Sorted using Selection Sort.")
            elif sort_choice == "4":
                names = insertion_sort(names)
                print("Sorted using Insertion Sort.")
            else:
                print("Invalid choice!")
        elif choice == "5":
            print("Current Names List:")
            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()


