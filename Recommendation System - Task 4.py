data = {
    'Movies': {
        'The Mummy': ['Action', 'Adventure', 'Thriller'],
        'Titanic': ['Comedy', 'Romance'],
        'The Avatar': ['Action', 'Adventure', 'Fantasy'],
        'Senior Year': ['Drama', 'Romance'],
        'Home Alone': ['Comedy', 'Drama'],
        'RRR':['Drama','Action'],
        'King Kong':['Adventure'],
        'The Adventures of Robin Hood':['Adventure','Drama','Action'],
        'The Treasure of the Sierra Madre':['Adventure'],
        'Raiders of the Lost Ark':['Adventure'],
        'Jurassic Park':['Adventure']
    },
    'Books': {
        'Jack Reacher': ['Mystery', 'Thriller'],
        'Her Keeper': ['Romance', 'Drama'],
        'Harry Potter': ['Science Fiction', 'Adventure'],
        'Around the Globe': ['Fantasy', 'Young Adult'],
        'Emily': ['Non-Fiction', 'Self-Help']
    },
    'Items': {
        'Vision Pro': ['Electronics', 'Gadgets'],
        'Sombrero': ['Clothing', 'Fashion'],
        'Birch table': ['Home Decor', 'Furniture'],
        'Football': ['Sports', 'Outdoor'],
        'RC Zoom': ['Toys', 'Kids'],
        'CCTV Camera':['Electronics', 'Gadgets']
    }
}

# Function to recommend items based on user preferences
def recommend_items(category, user_preferences):
    recommended_items = []

    for item, attributes in data[category].items():
        if all(attribute in attributes for attribute in user_preferences):
            recommended_items.append(item)

    return recommended_items

# Function to take user preferences as input
def get_user_preferences():
    print("Enter your preferences (comma-separated) for the selected category:")
    user_input = input().strip().split(',')
    return [preference.strip() for preference in user_input]

# Function to recommend items for a given category based on user preferences
def recommend_category(category):
    print(f"Recommendations for {category}:")
    user_preferences = get_user_preferences()
    recommended_items = recommend_items(category, user_preferences)

    if recommended_items:
        print(f"Recommended {category} for preferences: {', '.join(user_preferences)}")
        for item in recommended_items:
            print(f"{category}: {item}")
    else:
        print(f"No {category} found for the given preferences.")

# Ask the user to select a category (Movies, Books, or Items)
while True:
    print("Select a category: Movies, Books, Items (or 'exit' to quit)")
    selected_category = input().strip().capitalize()

    if selected_category == 'Exit':
        break

    if selected_category in data:
        recommend_category(selected_category)
    else:
        print("Invalid category. Please select Movies, Books, or Items.")
