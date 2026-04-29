from pydantic import BaseModel, Field, \
                        model_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=Rank.CADET)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: Optional[datetime] = None
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validator(self) -> "SpaceMission":
        command_count = 0
        experience_count = 0
        for member in self.crew:
            if member.rank.value == "captain" \
                    or member.rank.value == "commander":
                command_count += 1

        if self.mission_id[:1] != 'M':
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        if command_count < 1:
            raise ValueError("Crew must have at least 1 Commander or Captain")
        elif self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experience_count += 1
            if experience_count < (len(self.crew) / 2):
                raise ValueError("Long missions require at "
                                 "least 50% experienced crew")
        return self

    def format_crew_list(self) -> str:
        format = ''
        for member in self.crew:
            format += (f"- {member.name} ({member.rank.value}) "
                       f"- {member.specialization}\n")
        return format

    def display_info(self) -> str:
        return (f"Mission: {self.mission_name}\n"
                f"ID: {self.mission_id}\n"
                f"Destination: {self.destination}\n"
                f"Duration: {self.duration_days} days\n"
                f"Budget ${self.budget_millions}M\n"
                f"Crew size: {len(self.crew)}\n"
                f"Crew members:\n{self.format_crew_list()}")


def create_crew_member(name: str, rank: Rank, specialization: str,
                       years_experience: int, is_active: bool) -> dict:
    return {"name": name, "rank": rank, "specialization": specialization,
            "years_experience": years_experience, "is_active": is_active}


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("========================================")

    sarah_data = create_crew_member("Sarah Connor", Rank.COMMANDER,
                                    "Mission Command", 20, True)
    john_data = create_crew_member("John Smith", Rank.LIEUTENANT,
                                   "Navigation", 10, True)
    alice_data = create_crew_member("Alice Johnson", Rank.OFFICER,
                                    "Engineering", 5, True)
    sarah = CrewMember.model_validate(sarah_data)
    john = CrewMember.model_validate(john_data)
    alice = CrewMember.model_validate(alice_data)
    crew1 = [sarah, john, alice]
    crew2 = [john, alice]
    data1 = {"mission_id": "M2024_MARS",
             "mission_name": "Mars Colony Establishment",
             "destination": "Mars",
             "duration_days": "900",
             "budget_millions": "2500.0",
             "crew": crew1}
    data2 = {"mission_id": "M2024_MARS",
             "mission_name": "Mars Colony Establishment",
             "destination": "Mars",
             "duration_days": "900",
             "budget_millions": "2500.0",
             "crew": crew2}

    try:
        mission1 = SpaceMission.model_validate(data1)
        print("Valid mission created:")
        print(mission1.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")

    print("========================================")
    print("Expected validation error:")
    try:
        mission2 = SpaceMission.model_validate(data2)
        print("Valid mission created:")
        print(mission2.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")
