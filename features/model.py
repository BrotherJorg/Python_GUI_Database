from dataclasses import dataclass
import re

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


@dataclass
class Student:
    name: str
    email: str
    id: int | None = None

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        self.email = self.email.strip().lower()

        if len(self.name) < 2:
            raise ValueError("Name must have at least 2 characters.")

        if not EMAIL_PATTERN.fullmatch(self.email):
            raise ValueError("Invalid email address.")
