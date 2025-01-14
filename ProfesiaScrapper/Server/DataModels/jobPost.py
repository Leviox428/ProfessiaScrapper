from dataclasses import dataclass

@dataclass
class JobPost:
    regionName: str
    wage: int
    employer: str
    jobLocation: str