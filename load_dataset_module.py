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
                
                # Check if the line contains at least four parts
                # if len(parts) < 4:
                #     print(f"Invalid line: {line}")
                #     continue
                
                isbn, title, author, year = map(str.strip, parts[:4])
                
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
                
                # Check if the line contains the expected number of parts
                # if len(parts) != 3:
                #     print(f"Invalid line: {line}")
                #     continue
                
                user_id, isbn, rating = map(str.strip, parts)
                
                if isbn in books_data:
                    # Add the rating to the ratings sub-dictionary of the corresponding book
                    books_data[isbn]['ratings'][user_id] = rating
                else:
                    # If the book doesn't exist in the dataset, create a new entry
                    books_data[isbn] = {
                        'title': '',
                        'author': '',
                        'year': '',
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
                if user_id in users_data:
                    # Add the rating to the user's ratings dictionary
                    users_data[user_id][isbn] = rating
                else:
                    # If the user doesn't exist in the dataset, create a new entry
                    users_data[user_id] = {isbn: rating}

    except IOError as e:
        print(f'Error loading dataset: {e}')

    return users_data
