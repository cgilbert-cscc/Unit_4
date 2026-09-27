class Restaurant:
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

restaurant = Restaurant('The Mario Bros ', 'Pizza!')
print(restaurant.name)
print(restaurant.cuisine_type)