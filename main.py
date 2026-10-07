from learning_platform import Student, Mentor, Admin
from learning_platform.exceptions import InvalidUserError
from learning_platform.logger import logger


def validate_user(name, email):
    if not name.strip():
        raise InvalidUserError("User name cannot be empty.")

    if "@" not in email:
        raise InvalidUserError("Invalid email address.")


def main():

    try:
        print("=" * 50)
        print("       EVOLVE LEARNING PLATFORM")
        print("=" * 50)

        # Create Student
        validate_user(
            "Amrutha",
            "amrutha@example.com"
        )

        student1 = Student(
            101,
            "Amrutha",
            "amrutha@example.com",
            "Python"
        )

        # Create Mentor
        mentor1 = Mentor(
            201,
            "Arjun",
            "arjun@example.com",
            "Python & AI"
        )

        # Create Admin
        admin1 = Admin(
            301,
            "Meera",
            "meera@example.com"
        )

        print("\n--- Student Activity ---")

        student1.enroll_course(
            "Advanced Python"
        )

        student1.complete_course(
            "Python Fundamentals"
        )

        print("\n--- Mentor Activity ---")

        mentor1.assign_student(
            student1
        )

        print("\n--- Admin Activity ---")

        admin1.add_user(student1)
        admin1.add_user(mentor1)

        print("\n" + "=" * 50)
        print("USER DETAILS")
        print("=" * 50)

        users = [
            student1,
            mentor1,
            admin1
        ]

        for user in users:
            user.display_info()

        print("\n" + "=" * 50)
        print("METHOD OVERRIDING DEMONSTRATION")
        print("=" * 50)

        for user in users:
            print(
                f"{user.name} -> {user.get_role()}"
            )

    except InvalidUserError as error:

        logger.error(
            f"Invalid user: {error}"
        )

        print(
            f"User Error: {error}"
        )

    except Exception as error:

        logger.exception(
            f"Unexpected error: {error}"
        )

        print(
            f"Unexpected error: {error}"
        )

    finally:

        print(
            "\nLearning Platform execution completed."
        )


if __name__ == "__main__":
    main()