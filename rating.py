"""
Module responsible for the marks of places
"""
from dataclasses import dataclass


@dataclass
class Rating:
    """
    Holds information about the marks of the place
    """
    rating_id: int
    place_id: int
    one_stars: int
    two_stars: int
    three_stars: int
    four_stars: int
    five_stars: int

    def calculate_rating(self):
        """
        Calculates place's rating
        """
        return (self.one_stars + self.two_stars * 2 + self.three_stars * 3 + self.four_stars * 4 +
                self.five_stars * 5) / (self.one_stars + self.two_stars + self.three_stars +
                                        self.four_stars + self.five_stars)
