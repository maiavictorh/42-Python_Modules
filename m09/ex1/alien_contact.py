from pydantic import BaseModel, Field, \
                        model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    TELEPATHIC = "telepathic"
    PHYSICAL = "physical"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: Optional[datetime] = None
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(default=None)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contact_validator(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC'")
        elif self.contact_type.value == "physical" and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        elif self.contact_type.value == "telepathic" \
                and self.witness_count < 3:
            raise ValueError("Telepathic contact "
                             "requires at least 3 witnesses")
        elif self.signal_strength <= 7.0:
            raise ValueError("Signal strength is too weak")
        return self

    def display_info(self) -> str:
        return (f"ID: {self.contact_id}\n"
                f"Type: {self.contact_type.value}\n"
                f"Location: {self.location}\n"
                f"Signal: {self.signal_strength}\n"
                f"Duration: {self.duration_minutes}\n"
                f"Witnesses: {self.witness_count}\n"
                f"Message: '{self.message_received}'")


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("========================================")

    data1 = {"contact_id": "AC_2024_001",
             "contact_type": "radio",
             "location": "Area 51, Nevada",
             "signal_strength": "8.5",
             "duration_minutes": "45",
             "witness_count": "5",
             "message_received": "Greetings from Zeta Reticuli"}
    data2 = {"contact_id": "AC_2024_001",
             "contact_type": "telepathic",
             "location": "Area 51, Nevada",
             "signal_strength": "8.5",
             "duration_minutes": "45",
             "witness_count": "2",
             "message_received": "Greetings from Zeta Reticuli"}

    try:
        contact1 = AlienContact.model_validate(data1)
        print("Valid contact report:")
        print(contact1.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")

    print("\n========================================")
    print("Expected validation error:")
    try:
        contact2 = AlienContact.model_validate(data2)
        print("Valid contact report:")
        print(contact2.display_info())
    except ValidationError as err:
        print(f"\33[31m{err}\33[0m")
