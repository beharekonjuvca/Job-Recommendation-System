# recommendation_service.py

from recommendation_strategy_factory import RecommendationStrategyFactory
from user_behavior_tracking_service import UserBehaviorTrackingService

# Mock user behavior data and job listings data
user_behavior_data = {
    'user123': ['job1', 'job2'],
    'user234': ['job2', 'job3', 'job4'],
    'user345': ['job1', 'job4', 'job5'],
}

job_listings = {
    'job1': {'industry': 'Tech', 'skills': ['Python']},
    'job2': {'industry': 'Healthcare', 'skills': ['Biology']},
    'job3': {'industry': 'Tech', 'skills': ['Java']},
    'job4': {'industry': 'Finance', 'skills': ['Excel']},
    'job5': {'industry': 'Tech', 'skills': ['Python', 'Machine Learning']}
}

class RecommendationService:
    def __init__(self, user_behavior_data, job_listings):
        self.strategy_factory = RecommendationStrategyFactory(user_behavior_data, job_listings)
        self.user_behavior_service = UserBehaviorTrackingService.get_instance()

    def serve_recommendations(self, user_id: str):
        criteria = {'industry': 'Tech', 'skills': ['Python']}
        # Retrieve the user's behavior data
        behavior_data = self.user_behavior_service.get_behavior_data(user_id)

        # Determine the recommendation strategy based on user behavior
        strategy_type = 'hybrid' if behavior_data else 'content-based'

        # Get the appropriate recommendation strategy for the user
        recommendation_strategy = self.strategy_factory.get_recommendation_strategy(strategy_type)

        # Generate personalized recommendations
        
        recommendations = recommendation_strategy.generate_recommendations(user_id, criteria)

        return recommendations
        # Return the list of job recommendations

# Initialize the recommendation service with mock data
    # Track user behavior


recommendation_service = RecommendationService(user_behavior_data, job_listings)

# Generate and print recommendations for a user
user_recommendations = recommendation_service.serve_recommendations('user123')
recommendation_service = RecommendationService(user_behavior_data, job_listings)

# Initialize user behavior tracking service
user_behavior_service = UserBehaviorTrackingService.get_instance()

# Track some user behavior for a specific user (example)
user_behavior_service.track_user_behavior('user123', {'action': 'click', 'item': 'job1'})

# Generate and print recommendations for a user
user_recommendations = recommendation_service.serve_recommendations('user123')
print(user_recommendations)