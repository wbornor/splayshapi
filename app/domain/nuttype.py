from enum import Enum


class NutType(Enum):
    TALKNUT = 'TALKNUT'  # 1
    FAVNUT = 'FAVNUT'  # 2
    PHOTONUT = 'PHOTONUT'  # 3
    WISHNUT = 'WISHNUT'  # 4
    MEDIANUT = 'MEDIANUT'  # 6
    PROJECTNUT = 'PROJECTNUT'  # 7
    ANALNUT = 'ANALNUT'  # 8
    VIDINUT = 'VIDINUT'  # 9
    AUDINUT = 'AUDINUT'  # 10
    BUDNUT = 'BUDNUT'  # 12
    MAPNUT = 'MAPNUT'  # 13

    @classmethod
    def get_enum_by_name(cls, name):
        try:
            return cls.__members__[name]
        except KeyError:
            raise ValueError(f"No enum member with name '{name}'")
