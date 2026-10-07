from .user import User
from .logger import logger


class Student(User):
    """Student class inherits from User."""

    def __init__(self, user_id, name, email, course):
        super().__init__(user_id, name, email)
        self.course = course
        self.completed_courses = []

        logger.info(f"Student created: {name}")

    def enroll_course(self, course):
        self.course = course
        logger.info(f"{self.name} enrolled in {course}")

        print(f"{self.name} enrolled in {course}.")

    def complete_course(self, course):
        self.completed_courses.append(course)
        logger.info(f"{self.name} completed {course}")

        print(f"{self.name} completed {course}.")

    def get_role(self):
        """Method overriding."""
        return "Student"

    def display_info(self):
        """Override parent display_info method."""
        super().display_info()

        print(f"Role    : {self.get_role()}")
        print(f"Course  : {self.course}")
        print(f"Completed Courses: {self.completed_courses}")