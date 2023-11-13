# (1) Create a dicitonary 'bookstore' where each key is a genre and value is a list of books.
# (2) Let each book be a dictionary with keys 'title', 'author', 'year', 'price'.

favorite_fiction = {
    "British Literature": [
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": "1813", "price": "$9.99"},
        {"title": "Ivanhoe", "author": "Sir Walter Scott", "year": "1820", "price": "$7.99"},
    ],
    "Historical Fiction": [
        {"title": "Shogun", "author": "James Clavell", "year": "1975", "price": "$11.99"},
        {"title": "King Rat", "author": "James Clavell", "year": "1962", "price": "$10.99"},
    ]
}

# (3) Update a book's price.

favorite_fiction["British Literature"][1]["price"] = "$8.99"
print(favorite_fiction)
'''
(4) Add a new book to a genre.

(5) Remove a book from a genre.
(6) Sort the books by price.
(7) Print them in the format: "Title": [Title], "Author": [Author], "Year": [Year], "Price": [Price]
'''

