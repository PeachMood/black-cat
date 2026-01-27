from enum import StrEnum
from base_model import BaseModel
from email_validator import validate_email
import bcrypt


class UserRole(StrEnum):
    USER = "user"
    ADMIN = "admin"


class User(BaseModel):
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        role: UserRole = UserRole.USER,
        balance: int = 0,
    ) -> None:
        super().__init__()
        self._name = name
        self._email = email
        self._hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )
        self._role = role
        self._balance = balance

    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name
        self._update_timestamp()

    @property
    def email(self) -> str:
        return self._email

    def set_email(self, email: str) -> bool:
        if not validate_email(email):
            return False

        self._email = email
        self._update_timestamp()
        return True

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self._hashed_password)

    def set_password(self, password: str) -> None:
        self._update_timestamp()
        self._hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )

    @property
    def role(self) -> UserRole:
        return self._role

    def update_role(self, role: UserRole) -> None:
        self._role = role
        self._update_timestamp()

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> bool:
        if amount <= 0:
            return False

        self._balance += amount
        self._update_timestamp()
        return True

    def can_withdraw(self, amount: int) -> bool:
        return amount > 0 and self._balance >= amount

    def withdraw(self, amount: int) -> bool:
        if not self.can_withdraw(amount):
            return False

        self._balance -= amount
        self._update_timestamp()
        return True

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "username": self._name,
            "email": self._email,
            "role": self._role.value,
            "balance": self._balance,
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat(),
        }
