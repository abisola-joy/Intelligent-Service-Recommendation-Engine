import math

import math

def euclidean_distance(book1, book2, data):
    """
    Calculate the Euclidean distance between two books based on their ratings.
    
    Euclidean distance is a measure of the straight-line distance between two points in a multidimensional space. 
    In the context of recommendation systems, it is used to measure the dissimilarity between two items or users based on their ratings or features.
    
    Interpretation: 
        A lower Euclidean distance implies that two items or users are more similar to each other, while a higher distance indicates greater dissimilarity.

    Parameters:
    - book1 (str): The ID of the first book.
    - book2 (str): The ID of the second book.
    - data (dict): A dictionary containing user ratings for books.

    Returns:
    - tuple: A tuple containing the Euclidean distance between the two books and an explanation string.
    
    """

    common_ratings = {}
    
    # Check if both books exist in the data
    if book1 in data and book2 in data:
        ratings1 = data[book1]['ratings']
        ratings2 = data[book2]['ratings']
        
        # Remove double quotes from keys and values
        ratings1 = {key.strip('"'): float(value.strip('"')) for key, value in ratings1.items()}
        ratings2 = {key.strip('"'): float(value.strip('"')) for key, value in ratings2.items()}
        
        # print(f"Ratings 1: {ratings1}\nRatings 2: {ratings2}")
        
        common_ratings = {key: (ratings1.get(key, 0), ratings2.get(key, 0)) for key in set(ratings1) & set(ratings2)}
        # print(f"\nCommon Ratings:{common_ratings}\n")
        
        
        if not common_ratings:
            return 0, "No common ratings found."

        squared_diff = sum((rating1 - rating2) ** 2 for rating1, rating2 in common_ratings.values())
        euclidean_dist = math.sqrt(squared_diff)

        explanation = f"Euclidean Distance: {euclidean_dist:.2f}\nA lower Euclidean distance implies greater similarity."
        
        return euclidean_dist, explanation
    else:
        return 0, "One or both books not found in data."


def pearson_correlation_coefficient(user1, user2, data):
    """
    Calculate the Pearson correlation coefficient between two users based on their ratings.

    Pearson correlation coefficient measures the linear correlation between two variables. 
    In the context of recommendation systems, it is used to measure the similarity between two items or users based on their ratings.
    
    Interpretation: 
        The coefficient ranges from -1 to 1, where:
            1 indicates a perfect positive correlation (both items tend to increase or decrease together).
            -1 indicates a perfect negative correlation (one item tends to increase as the other decreases).
            0 indicates no linear correlation between the items.
    
    Parameters:
    - user1 (str): The ID of the first user.
    - user2 (str): The ID of the second user.
    - data (dict): A dictionary containing user ratings for items.

    Returns:
    - tuple: A tuple containing the Pearson correlation coefficient between the two users and an explanation string.
    
    """

    if user1 in data and user2 in data:
        
        common_ratings = {}
    
        # Extract ratings for user1 and user2
        ratings1 = data[user1]
        ratings2 = data[user2]
    
        # print(f"Ratings 1: {ratings1}\nRatings 2: {ratings2}")
    
        # Find common ratings
        common_users = set(ratings1.keys()) & set(ratings2.keys())
        common_ratings = {user: (float(ratings1[user].strip('"')), float(ratings2[user].strip('"'))) for user in common_users}
        # print(f"\nCommon Ratings:{common_ratings}\n")
    
        if not common_ratings:
            return 0, "No common ratings found."
    
        n = len(common_ratings)
        sum1 = sum(rating1 for rating1, _ in common_ratings.values())
        sum2 = sum(rating2 for _, rating2 in common_ratings.values())
        sum1_sq = sum(rating1 ** 2 for rating1, _ in common_ratings.values())
        sum2_sq = sum(rating2 ** 2 for _, rating2 in common_ratings.values())
        product_sum = sum(rating1 * rating2 for rating1, rating2 in common_ratings.values())
    
        num = product_sum - (sum1 * sum2 / n)
        den = math.sqrt((sum1_sq - sum1 ** 2 / n) * (sum2_sq - sum2 ** 2 / n))
    
        if den == 0:
            return 0, "Denominator is zero."
    
        pearson_coefficient = num / den
        explanation = f"Pearson Correlation Coefficient: {pearson_coefficient:.2f}\nA coefficient close to 1 indicates a strong positive correlation, while a coefficient close to -1 indicates a strong negative correlation."

        return pearson_coefficient, explanation
    else:
        return 0, "One or both users not found in data."


def cosine_similarity(book1, book2, data):
    """
    Calculate the cosine similarity between two items books based on their ratings.

    Cosine similarity measures the cosine of the angle between two vectors in a multidimensional space. 
    In recommendation systems, itis used to measure the similarity between two items or users based on their ratings or features.
    
    Interpretation: 
        Cosine similarity ranges from -1 to 1, where:
            1 indicates that the two items are perfectly similar (point in the same direction).
            0 indicates that the items are orthogonal (no correlation).
            -1 indicates that the items are perfectly dissimilar (point in opposite directions).
            
    Parameters:
    - book1 (str): The ID of the first book.
    - book2 (str): The ID of the second book.
    - data (dict): A dictionary containing user ratings for books.

    Returns:
    - tuple: A tuple containing the cosine similarity between the two books and an explanation string.
    
    """

    common_ratings = {}
    
    # Check if both books exist in the data
    if book1 in data and book2 in data:
        ratings1 = data[book1]['ratings']
        ratings2 = data[book2]['ratings']
        
        # Remove double quotes from keys and values
        ratings1 = {key.strip('"'): float(value.strip('"')) for key, value in ratings1.items()}
        ratings2 = {key.strip('"'): float(value.strip('"')) for key, value in ratings2.items()}
        
        # print(f"Ratings 1: {ratings1}\nRatings 2: {ratings2}")
        
        common_ratings = {key: (ratings1.get(key, 0), ratings2.get(key, 0)) for key in set(ratings1) & set(ratings2)}
        # print(f"\nCommon Ratings:{common_ratings}\n")
        
        if not common_ratings:
            return 0, "No common ratings found."

        dot_product = sum(rating1 * rating2 for rating1, rating2 in common_ratings.values())
        magnitude_item1 = math.sqrt(sum(rating ** 2 for rating, _ in common_ratings.values()))
        magnitude_item2 = math.sqrt(sum(rating ** 2 for _, rating in common_ratings.values()))

        if magnitude_item1 == 0 or magnitude_item2 == 0:
            return 0, "Magnitude of one or both items is zero."

        cosine_sim = dot_product / (magnitude_item1 * magnitude_item2)
        explanation = f"Cosine Similarity: {cosine_sim:.2f}\nA similarity of 1 indicates perfect similarity, while a similarity of 0 indicates no similarity."

        return cosine_sim, explanation
    else:
        return 0, "One or both books not found in data."


def manhattan_distance(user1, user2, data):
    """
    Calculate the Manhattan distance between two items (users or books) based on their ratings.

    Manhattan distance (also known as taxicab or city block distance) is the sum of the absolute differences between the coordinates of two points in a multidimensional space. 
    In recommendation systems, it is used to measure the distance between two items or users based on their ratings or features.
    
    Interpretation: 
    Manhattan distance represents the total distance one would travel to move from one point to another along the grid of a city block. 
    In this context, a lower Manhattan distance implies greater similarity between two items or users.
    
    Parameters:
    - user1 (str): The ID of the first user.
    - user2 (str): The ID of the second user.
    - data (dict): A dictionary containing user ratings for items.

    Returns:
     - tuple: A tuple containing the Manhattan distance between the two users and an explanation string.
    
    """

    common_ratings = {}
    
    if user1 in data and user2 in data:
        # Extract ratings for user1 and user2
        ratings1 = data[user1]
        ratings2 = data[user2]
    
        # print(f"Ratings 1: {ratings1}\nRatings 2: {ratings2}")
        
        # Find common ratings
        common_users = set(ratings1.keys()) & set(ratings2.keys())
        common_ratings = {user: (float(ratings1[user].strip('"')), float(ratings2[user].strip('"'))) for user in common_users}
    
        # print(f"\nCommon Ratings:{common_ratings}\n")
        
        if not common_ratings:
            return 0, "No common ratings found."
    
        manhattan_dist = sum(abs(rating1 - rating2) for rating1, rating2 in common_ratings.values())
        explanation = f"Manhattan Distance: {manhattan_dist:.2f}\nA lower Manhattan distance implies greater similarity."
        return manhattan_dist, explanation
    else:
        return 0, "One or both users not found in data."


def minkowski_distance(book1, book2, data, p=1):
    """
    Calculate the Minkowski distance between two books based on their ratings.

    Minkowski distance is a generalization of Euclidean distance and Manhattan distance. 
    It is defined as the p-th root of the sum of the absolute values raised to the power of p.

    Interpretation: 
        Minkowski distance generalizes both Euclidean and Manhattan distances and is controlled by the parameter p. 
        When p=1, it reduces to Manhattan distance, and when p=2, it reduces to Euclidean distance.
        Smaller values imply greater similarity, while larger values imply greater dissimilarity.
        
    Parameters:
    - book1 (str): The ID of the first book.
    - book2 (str): The ID of the second book.
    - data (dict): A dictionary containing user ratings for books.

    Returns:
    - tuple: A tuple containing the Minkowski distance between the two books and an explanation string.
    
    """
    common_ratings = {}
    
    # Check if both books exist in the data
    if book1 in data and book2 in data:
        ratings1 = data[book1]['ratings']
        ratings2 = data[book2]['ratings']
        
        # Remove double quotes from keys and values
        ratings1 = {key.strip('"'): float(value.strip('"')) for key, value in ratings1.items()}
        ratings2 = {key.strip('"'): float(value.strip('"')) for key, value in ratings2.items()}
        
        # print(f"Ratings 1: {ratings1}\nRatings 2: {ratings2}")
        
        common_ratings = {key: (ratings1.get(key, 0), ratings2.get(key, 0)) for key in set(ratings1) & set(ratings2)}
        # print(f"\nCommon Ratings:{common_ratings}\n")
        
        if not common_ratings:
            return 0, "No common ratings found."

    minkowski_dist = sum(abs(rating1 - rating2) ** p for rating1, rating2 in common_ratings.values()) ** (1 / p)
    explanation = f"Minkowski Distance (p={p}): {minkowski_dist:.2f}\nSmaller values imply greater similarity."

    return minkowski_dist, explanation


def find_n_similar_books(book_id, num_books, data):
    """
    Find similar books to a given book based on Euclidean distance.

    Parameters:
    - book_id (str): The ID of the book for which to find similar books.
    - data (dict): A dictionary containing book data.

    Returns:
    - list: A list of tuples containing (book_id, euclidean_distance) for the similar books.
    """

    # Print book details
    print("BOOK DETAILS:")
    print("--------------")
    print("Book ID:", book_id)
    print("Title:", data[book_id]['title'])
    print("Author:", data[book_id]['author'])
    print("Year:", data[book_id]['year'])
    print()

    def euclidean_distance(book1, book2, data):
        """
        Calculate the Euclidean distance between two books based on their ratings.

        Parameters:
        - book1 (str): The ID of the first book.
        - book2 (str): The ID of the second book.
        - data (dict): A dictionary containing user ratings for books.

        Returns:
        - float: The Euclidean distance between the two books.
        """

        common_ratings = {}

        # Check if both books exist in the data
        if book1 in data and book2 in data:
            ratings1 = data[book1]['ratings']
            ratings2 = data[book2]['ratings']

            # Remove double quotes from keys and values
            ratings1 = {key.strip('"'): float(value.strip('"')) for key, value in ratings1.items()}
            ratings2 = {key.strip('"'): float(value.strip('"')) for key, value in ratings2.items()}

            common_ratings = {key: (ratings1.get(key, 0), ratings2.get(key, 0)) for key in set(ratings1) & set(ratings2)}

            if not common_ratings:
                return 0

            squared_diff = sum((rating1 - rating2) ** 2 for rating1, rating2 in common_ratings.values())
            return math.sqrt(squared_diff)
        else:
            return 0

    valid_books = {}
    for book_id, book_data in data.items():
        if 'ratings' in book_data:
            # Check if all ratings are valid numerical values
            ratings = book_data['ratings']
            if all(isinstance(rating, int) or isinstance(rating, float) for rating in ratings.values()):
                valid_books[book_id] = book_data

    # Compute Euclidean distance between the given book and all other valid books
    distances = [(other_book_id, euclidean_distance(book_id, other_book_id, data)) for other_book_id in valid_books.keys() if other_book_id != book_id]

    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[1])

    # Return the n most similar books
    similar_books = distances[:num_books]

    # Print details of the similar books
    print("SIMILAR BOOKS:")
    print("--------------")
    for similar_book_id, euclidean_distance in similar_books:
        print("Book ID:", similar_book_id)
        print("Title:", data[similar_book_id]['title'])
        print("Author:", data[similar_book_id]['author'])
        print("Year:", data[similar_book_id]['year'])
        print("Euclidean Distance:", euclidean_distance)
        print()