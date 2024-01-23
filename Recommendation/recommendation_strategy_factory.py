# recommendation_strategy_factory.py

from collaborative_filtering import CollaborativeFiltering
from content_based_filtering import ContentBasedFiltering
from hybrid_recommendation import HybridRecommendation

class RecommendationStrategyFactory:
    def __init__(self, user_behavior_data, job_listings):
        self.user_behavior_data = user_behavior_data
        self.job_listings = job_listings

    def get_recommendation_strategy(self, strategy_type: str):
        if strategy_type == 'collaborative':
            return CollaborativeFiltering(self.user_behavior_data)
        elif strategy_type == 'content-based':
            return ContentBasedFiltering(self.job_listings)
        elif strategy_type == 'hybrid':
            return HybridRecommendation(self.user_behavior_data, self.job_listings)
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")

# Example usage:
user_behavior_data = {
    'user1': ['job4', 'job5'],
    'user2': ['job2', 'job3'],
    'user3': ['job1', 'job3'],
    # ... additional user behavior data ...
}

job_listings = {
    'job234': {'industry': 'Tech', 'skills': ['Python', 'Data Analysis']},
    'job567': {'industry': 'Finance', 'skills': ['Excel', 'Accounting']},
    'job890': {'industry': 'Tech', 'skills': ['Python', 'Machine Learning']},
    # ... additional job listings data ...
}

factory = RecommendationStrategyFactory(user_behavior_data, job_listings)
strategy = factory.get_recommendation_strategy('collaborative')
recommendations = strategy.generate_recommendations('user1', {})
print(recommendations)
