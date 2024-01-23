# recommendation_engine_interface.py

from abc import ABC, abstractmethod
from typing import List

class RecommendationEngineInterface(ABC):
    @abstractmethod
    def generate_recommendations(self, user_id: str, criteria: dict) -> List[str]:
        """
        Generate a list of job recommendations based on the given user ID and criteria.

        Args:
            user_id (str): The ID of the user for whom recommendations are being generated.
            criteria (dict): A dictionary containing criteria used to generate recommendations.

        Returns:
            List[str]: A list of recommended job IDs.
        """
        pass

# Example implementation of a strategy
class CollaborativeFiltering(RecommendationEngineInterface):
    def generate_recommendations(self, user_id: str, criteria: dict) -> List[str]:
        # Implementation for collaborative filtering
        # For example purposes, return an empty list
        return []

# Example usage
# recommendation_strategy = CollaborativeFiltering()
# recommendations = recommendation_strategy.generate_recommendations('user123', {})
# print(recommendations)
