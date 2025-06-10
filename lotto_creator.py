import random
from enum import Enum
from typing import Literal


class MBTI(Enum):
    ISTJ = "ISTJ"
    ISFJ = "ISFJ"
    INFJ = "INFJ"
    INTJ = "INTJ"
    ISTP = "ISTP"
    ISFP = "ISFP"
    INFP = "INFP"
    INTP = "INTP"
    ESTP = "ESTP"
    ESFP = "ESFP"
    ENFP = "ENFP"
    ENTP = "ENTP"
    ESTJ = "ESTJ"
    ESFJ = "ESFJ"
    ENFJ = "ENFJ"
    ENTJ = "ENTJ"


class BLOOD_TYPE(Enum):
    A = "A"
    B = "B"
    AB = "AB"
    O = "O"


class Motto:
    def __init__(self, data: dict):
        self.seed = self.set_seed(**data)
        self.motto = self.create()

    def set_seed(
        self,
        name: str,
        birth: str,
        phone: str,
        email: str | None = None,
        mbti: MBTI | None = None,
        blood_type: BLOOD_TYPE | None = None,
        gender: Literal["M", "F"] | None = None,
        foot_size: int | None = None,
        height: int | None = None,
    ):
        return f"N:{name};B:{birth};P:{phone};E:{email};M:{mbti};BT:{blood_type};G:{gender};FS:{foot_size};H:{height}"

    def create(self):
        random.seed(self.seed)
        return sorted(random.sample(range(1, 46), 6))
