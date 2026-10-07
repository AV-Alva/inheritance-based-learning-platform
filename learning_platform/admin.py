from .user import User
from .logger import logger


class Admin(User):
    """Admin class inherits from User."""

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

        self.managed_users = []

        logger.info(f"Admin created: {name}")

    def add_user(self, user):
        self.managed_users.append(user.name)

        logger.info(
            f"Admin {self.name} added user {user.name}"
        )

        print(
            f"Admin {self.name} added {user.name}."
        )

    def remove_user(self, user):
        if user.name in self.managed_users:
            self.managed_users.remove(user.name)

            logger.info(
                f"Admin {self.name} removed user {user.name}"
            )

            print(
                f"Admin {self.name} removed {user.name}."
            )

    def get_role(self):
        """Method overriding."""
        return "Admin"

    def display_info(self):
        """Override parent method."""
        super().display_info()

        print(f"Role          : {self.get_role()}")
        print(f"Managed Users : {self.managed_users}")