from collections import Counter
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def most_frequent_element(lst):
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]

def main():
    while True:
        print("\nChoose an option:")
        print("1. Check if Two Strings are Anagrams")
        print("2. Check if a Number is Prime")
        print("3. Find the Most Frequent Element in a List")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            str1 = input("Enter first string: ")
            str2 = input("Enter second string: ")
            result = are_anagrams(str1, str2)
            print("Anagrams" if result else "Not Anagrams")

        elif choice == "2":
            num = int(input("Enter a number: "))
            print("Prime" if is_prime(num) else "Not Prime")

        elif choice == "3":
            lst_input = input("Enter elements separated by spaces: ")
            lst = lst_input.split()
            try:
                lst = [int(item) for item in lst]
            except ValueError:
                pass 
            result = most_frequent_element(lst)
            print(f"Most Frequent Element: {result}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
