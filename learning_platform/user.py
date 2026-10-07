class User:
    """Parent class representing a user of the learning platform."""

    platform_name = "Evolve Learning Platform"

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_info(self):
        """Display common user information."""
        print("\n--- User Information ---")
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")

    def get_role(self):
        """Return the role of the user."""
        return "User"