# eligibility_checker.py

class UserProfile:
    def __init__(self, skills=None, experience_level=None):
        self.skills = skills if skills else []
        self.experience_level = experience_level

class Job:
    def __init__(self, required_skills=None, required_experience_level=None):
        self.required_skills = required_skills if required_skills else []
        self.required_experience_level = required_experience_level

class EligibilityChecker:
    def check_eligibility(self, user_profile: UserProfile, job_listing: Job) -> bool:
        """
        Check if a user's profile matches the requirements of a job listing.

        Args:
            user_profile (UserProfile): The user's profile.
            job_listing (Job): The job listing.

        Returns:
            bool: True if the user is eligible for the job, False otherwise.
        """
        # Check experience level
        if job_listing.required_experience_level and user_profile.experience_level != job_listing.required_experience_level:
            return False
        
        # Check for skills match
        if not self.has_required_skills(user_profile.skills, job_listing.required_skills):
            return False

        # Additional checks can be added here (e.g., education level, certifications)

        return True

    def has_required_skills(self, user_skills, job_skills):
        """
        Check if the user has all the required skills for the job.

        Args:
            user_skills (list): List of skills the user has.
            job_skills (list): List of skills required for the job.

        Returns:
            bool: True if the user has all required skills, False otherwise.
        """
        return set(job_skills).issubset(set(user_skills))

# Example usage
user_profile = UserProfile(skills=['Python', 'Data Analysis'], experience_level='Mid-Level')
job_listing = Job(required_skills=['Python', 'Machine Learning'], required_experience_level='Mid-Level')
eligibility_checker = EligibilityChecker()
is_eligible = eligibility_checker.check_eligibility(user_profile, job_listing)
print(is_eligible)  # Output: False (user lacks 'Machine Learning' skill)
