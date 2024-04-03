
import load_dataset_module
import similarity_module

def get_details_menu(book_profile, user_profile):
    """
    Display menu options for getting book and user details.
    """
    while True:
        print("\nGet Book and User Details:")
        print("1. Load Books")
        print("2. Load Users ID")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            try:
                number = int(input("\nEnter the number of books you want to print: "))
                load_dataset_module.n_top_books(number, book_profile)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            
        elif choice == "2":
            try:
                number = int(input("\nEnter the number of user ID you want to print: "))
                load_dataset_module.n_top_users(number, user_profile)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            
        elif choice == "3":
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def find_similar_users_menu(user_profile):
    """
    Display menu options for finding similar users.
    """
    while True:
        print("\nChoose a method to calculate similarity:")
        print("1. Pearson Correlation Coefficient")
        print("2. Manhattan Distance")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            user1 = input("\nEnter the first user: ")
            user2 = input("\nEnter the second user: ")
            
            similarity, explanation = similarity_module.pearson_correlation_coefficient(user1, user2, user_profile)
            print("\nSimilarity:", similarity)
            print("Explanation:", explanation)
            
        elif choice == "2":
            user1 = input("\nEnter the first user: ")
            user2 = input("\nEnter the second user: ")
            
            similarity, explanation = similarity_module.manhattan_distance(user1, user2, user_profile)
            print("\nSimilarity:", similarity)
            print("Explanation:", explanation)
            
        elif choice == "3":
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def find_similar_books_menu(book_profile):    
    """
    Display menu options for finding similar books.
    """
    while True:
        print("\nChoose a method to calculate similarity:")
        print("1. Euclidean Distance")
        print("2. Cosine similarity")
        print("3. Minkowski Distance")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            book1 = input("\nEnter the first book: ")
            book2 = input("\nEnter the second book: ")
            
            similarity, explanation = similarity_module.euclidean_distance(book1, book2, book_profile)
            print("\nSimilarity:", similarity)
            print("Explanation:", explanation)
            
        elif choice == "2":
            book1 = input("\nEnter the first book: ")
            book2 = input("\nEnter the second book: ")
            
            similarity, explanation = similarity_module.cosine_similarity(book1, book2, book_profile)
            print("\nSimilarity:", similarity)
            print("Explanation:", explanation)

        elif choice == "3":
            book1 = input("\nEnter the first book: ")
            book2 = input("\nEnter the second book: ")
            
            similarity, explanation = similarity_module.minkowski_distance(book1, book2, book_profile)
            print("\nSimilarity:", similarity)
            print("Explanation:", explanation)
            
        elif choice == "4":
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")