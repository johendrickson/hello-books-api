class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Circe", "Circe is a 2018 mythic fantasy novel by American writer Madeline Miller. Set during the Greek Heroic Age, it is an adaptation of various Greek myths, most notably the Odyssey, as told from the perspective of the witch Circe."),
    Book(2, "Pride and Prejudice", "A classic novel by Jane Austen that tells the story of Elizabeth Bennet and her relationship with Mr. Darcy. It's a tale of love, social expectations, and personal growth."),
    Book(3, "The Name of the Wind", "The Name of the Wind, also referred to as The Kingkiller Chronicle: Day One, is a heroic fantasy novel written by American author Patrick Rothfuss.")
]