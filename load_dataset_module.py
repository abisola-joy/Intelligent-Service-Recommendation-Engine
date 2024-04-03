# Returns a nested dictionary of books (ISBN, title, author, year, and ratings)
def load_books_dataset():
    """
    Load the book dataset from the CSV file and return a dictionary containing book information.
    """
    try:
        books_data = {}
    
        # Load Books.csv file and extract information for each book
        with open('Books.csv', encoding='ISO-8859-1') as file:
            for line in file:
                # Split the line into parts and strip whitespace from each part
                parts = line.strip().split(';')
                isbn, title, author, year = map(str.strip, parts[:4])
                isbn = isbn.strip('""')
                
                # Initialize the ratings sub-dictionary for each book
                books_data[isbn] = {
                    'title': title,
                    'author': author,
                    'year': year,
                    'ratings': {}
                }

        # Load Book-Ratings.csv file and append ratings to corresponding books
        with open('Book-Ratings.csv', encoding='ISO-8859-1') as file:
            for line in file:
                # Split the line into parts and strip whitespace from each part
                parts = line.strip().split(';')
                user_id, isbn, rating = map(str.strip, parts)
                isbn = isbn.strip('""')
                user_id = user_id.strip('""')
                
                if isbn in books_data:
                    # Add the rating to the ratings sub-dictionary of the corresponding book
                    books_data[isbn]['ratings'][user_id] = rating
                else:
                    # If the book doesn't exist in the dataset, create a new entry
                    books_data[isbn] = {
                        'title': 'N/A',
                        'author': 'N/A',
                        'year': 'N/A',
                        'ratings': {user_id: rating}
                    }

    except IOError as e:
        print(f'Error loading dataset: {e}')

    return books_data


# Returns a nested dictionary of users (UserID, ISBN, Book-Rating)
def load_users_dataset():
    """
    Load the user dataset from the CSV file and return a dictionary containing user ratings.
    """
    try:
        users_data = {}

        # Load Book-Ratings.csv file and organize ratings by user ID
        with open('Book-Ratings.csv', encoding='ISO-8859-1') as file:
            for line in file:
                # Split the line into parts and strip whitespace from each part
                user_id, isbn, rating = map(str.strip, line.split(';'))
                user_id = user_id.strip('""')
                isbn = isbn.strip('""')
                
                if user_id in users_data:
                    # Add the rating to the user's ratings dictionary
                    users_data[user_id][isbn] = rating
                else:
                    # If the user doesn't exist in the dataset, create a new entry
                    users_data[user_id] = {isbn: rating}

    except IOError as e:
        print(f'Error loading dataset: {e}')

    return users_data


def n_top_books(number, books):
    # Sort the dictionary items by the 'title' key in the inner dictionary values in ascending order
    sorted_books = sorted(books.items(), key=lambda x: x[1]['title'], reverse=False)
    
    # Get the items
    n_books = sorted_books[:number]
    
    # Print the top 10 items with formatted details
    print(f"\nTop {number} books and their details:")
    for item in n_books:
        book_id, book_details = item
        print("Book ID:", book_id)
        print("Title:", book_details['title'])
        print("Author:", book_details['author'])
        print("Year:", book_details['year'])
        print()


def n_top_users(number, users):
    # Sort the dictionary items by the number of ratings in descending order
    sorted_users = sorted(users.items(), key=lambda x: len(x[1]), reverse=True)
    
    # Get the top users
    top_users = sorted_users[:number]
    
    # Print the top users with formatted details
    print(f"\nTop {number} users:")
    for user_id, user_data in top_users:
        print("User ID:", user_id)
