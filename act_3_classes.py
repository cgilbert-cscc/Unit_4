class Restaurant:
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"The {self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
        msg = f"The {self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('Mario Bros', 'Pizza!')
print(restaurant.name, restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()