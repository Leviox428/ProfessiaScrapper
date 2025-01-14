from dataclasses import dataclass

@dataclass
class Region:
    regionName: str
    numOfJobPostings: int
    averageWage: float