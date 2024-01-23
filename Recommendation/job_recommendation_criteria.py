# job_recommendation_criteria.py

class JobRecommendationCriteria:
    def __init__(self, skills=None, experience_level=None, industry=None, other_criteria=None):
        self.skills = skills if skills is not None else []
        self.experience_level = experience_level
        self.industry = industry
        self.other_criteria = other_criteria if other_criteria is not None else {}

    def update_criteria(self, new_criteria):
        """
        Update the recommendation criteria with new values.

        Args:
            new_criteria (JobRecommendationCriteria): An instance of JobRecommendationCriteria containing the new criteria.
        """
        if new_criteria.skills is not None:
            self.skills = new_criteria.skills
        if new_criteria.experience_level is not None:
            self.experience_level = new_criteria.experience_level
        if new_criteria.industry is not None:
            self.industry = new_criteria.industry
        if new_criteria.other_criteria is not None:
            self.other_criteria = new_criteria.other_criteria

    def validate_criteria(self):
        """
        Validate the recommendation criteria to ensure they are in the correct format.
        """
        # Implement validation logic for criteria
        # For example, check if skills are in a list, experience_level is a valid string, etc.
        pass

    def to_query_params(self):
        """
        Convert the recommendation criteria into a format suitable for querying a database or API.

        Returns:
            dict: A dictionary of query parameters.
        """
        query_params = {}
        if self.skills:
            query_params['skills'] = self.skills
        if self.experience_level:
            query_params['experience_level'] = self.experience_level
        if self.industry:
            query_params['industry'] = self.industry
        query_params.update(self.other_criteria)
        return query_params

# Example usage
criteria = JobRecommendationCriteria(skills=['Python', 'Data Analysis'], experience_level='Mid-Level', industry='Tech')
updated_criteria = JobRecommendationCriteria(skills=['Python', 'Machine Learning'])
criteria.update_criteria(updated_criteria)
print(criteria.skills)  # ['Python', 'Machine Learning']

# Converting criteria to query parameters
query_params = criteria.to_query_params()
print(query_params)  # Dictionary of query parameters
