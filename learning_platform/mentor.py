from .user import User
from .logger import logger


class Mentor(User):
    """Mentor class inherits from User."""

    def __init__(self, user_id, name, email, expertise):
        super().__init__(user_id, name, email)
        self.expertise = expertise
        self.students = []

        logger.info(f"Mentor created: {name}")

    def assign_student(self, student):
        self.students.append(student.name)

        logger.info(
            f"Student {student.name} assigned to mentor {self.name}"
        )

        print(
            f"{student.name} assigned to mentor {self.name}."
        )

    def get_role(self):
        """Method overriding."""
        return "Mentor"

    def display_info(self):
        """Override parent method."""
        super().display_info()

        print(f"Role      : {self.get_role()}")
        print(f"Expertise : {self.expertise}")
        print(f"Students  : {self.students}")