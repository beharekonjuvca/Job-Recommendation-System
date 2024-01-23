class UserProfile:
    def __init__(self, preferred_industries=None, preferred_job_types=None, preferred_skills=None):
        self.preferred_industries = preferred_industries if preferred_industries else []
        self.preferred_job_types = preferred_job_types if preferred_job_types else []
        self.preferred_skills = preferred_skills if preferred_skills else []

class Job:
    def __init__(self, industry=None, job_type=None, required_skills=None):
        self.industry = industry
        self.job_type = job_type
        self.required_skills = required_skills if required_skills else []

class PreferenceMatcher:
    def match_preferences(self, user_profile: UserProfile, job_listing: Job) -> bool:
        if user_profile.preferred_industries and job_listing.industry not in user_profile.preferred_industries:
            return False
        if user_profile.preferred_job_types and job_listing.job_type not in user_profile.preferred_job_types:
            return False
        if user_profile.preferred_skills and not all(skill in job_listing.required_skills for skill in user_profile.preferred_skills):
            return False
        return True

# Example usage
user_profile = UserProfile(preferred_industries=['Tech'], preferred_job_types=['Full-time'], preferred_skills=['Python'])
job_listing = Job(industry='Tech', job_type='Full-time', required_skills=['Python', 'Machine Learning'])
preference_matcher = PreferenceMatcher()
is_match = preference_matcher.match_preferences(user_profile, job_listing)
print(is_match)  # Output: True or False depending on the matching criteria
