from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(gt=0.0, lt=100.0)
    last_maintenance: Optional[datetime] = None
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

    def display_info(self) -> str:
        status = "Operational" if self.is_operational else "Non operational"
        return (f"ID: {self.station_id}\n"
                f"Name: {self.name}\n"
                f"Crew: {self.crew_size} people\n"
                f"Power: {self.power_level}%\n"
                f"Oxygen: {self.oxygen_level}%\n"
                f"Status: {status}")


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")

    data1 = {"station_id": "ISS001",
             "name": "International Space Station",
             "crew_size": "6",
             "power_level": "85.5",
             "oxygen_level": "92.3",
             "is_operational": "True"}
    data2 = {"station_id": "ISS001",
             "name": "International Space Station",
             "crew_size": "21",
             "power_level": "85.5",
             "oxygen_level": "92.3",
             "is_operational": "True"}

    try:
        station1 = SpaceStation.model_validate(data1)
        print("Valid station created:")
        print(station1.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")

    print("\n========================================")
    print("Expected validation error:")
    try:
        station2 = SpaceStation.model_validate(data2)
        print("Valid station created:")
        print(station2.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")
