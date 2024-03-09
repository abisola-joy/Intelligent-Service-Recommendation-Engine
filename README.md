# Intelligent Service Recommendation Engine

## Overview
This repository contains the source code for an Intelligent Service Recommendation Engine, which provides recommendations for users based on their preferences and interactions with the system. The recommendation engine employs various similarity measures and collaborative filtering techniques to generate personalized recommendations.
(this was an assessment that needed to be done without any libraries imported)

## Features
- **User Interface:** Provides an interactive interface for users to browse recommendations, view book details, and explore different similarity measures.
- **Data Loading:** Loads book and user data from CSV files, allowing users to analyze ratings and generate recommendations.
- **Similarity Measures:** Implements different similarity measures such as Pearson correlation coefficient, cosine similarity, and Minkowski distance to calculate similarities between users or books.
- **Recommendation Generation:** Generates personalized recommendations for users based on their preferences and interactions with the system.
- **Error Handling:** Includes robust error handling to gracefully handle missing or invalid data.

## Installation
To run the recommendation engine locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure that the CSV files containing book and user data (`Books.csv` and `Book-Ratings.csv`) are placed in the appropriate directory.
4. Run the main script `test_module` to start the recommendation engine.

## Usage
Once the recommendation engine is running, follow these steps to use it:

1. Navigate through the interactive interface to load book and user data.
2. Choose the option to generate recommendations based on similarity measures or collaborative filtering techniques.
3. Explore the recommended books and view their details, including title, author, rating, and publication year.
4. Experiment with different similarity measures to observe how they affect the generated recommendations.
5. Provide feedback or suggestions for improving the recommendation engine.

## Contributing
Contributions to this project are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull request. 

Please ensure that your contributions adhere to the project's coding standards and guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- This project was developed as part of Sheffield Hallam University's course on Big Data Analytics.
- Special thanks to the instructors for their valuable feedback and support.
