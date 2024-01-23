# user_behavior_tracking_service.py

import json

class UserBehaviorTrackingService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserBehaviorTrackingService, cls).__new__(cls)
            cls._instance.behavior_data_store = {}
        return cls._instance

    @staticmethod
    def get_instance():
        if UserBehaviorTrackingService._instance is None:
            UserBehaviorTrackingService()
        return UserBehaviorTrackingService._instance

    def track_user_behavior(self, user_id: str, behavior_data: dict) -> None:
        if user_id not in self._instance.behavior_data_store:
            self._instance.behavior_data_store[user_id] = []
        self._instance.behavior_data_store[user_id].append(behavior_data)

    def get_behavior_data(self, user_id: str):
        return self._instance.behavior_data_store.get(user_id, [])

    def store_user_behavior(self, user_id: str, behavior_data: dict) -> None:
        self.track_user_behavior(user_id, behavior_data)

    def clear_behavior_data(self):
        self._instance.behavior_data_store.clear()

    def save_behavior_data_to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            json.dump(self._instance.behavior_data_store, file, indent=4)

# Example usage:
user_behavior_service = UserBehaviorTrackingService.get_instance()
user_behavior_service.track_user_behavior('user123', {'action': 'click', 'item': 'job123'})
user_data = user_behavior_service.get_behavior_data('user123')
print(user_data)

# Saving behavior data to a file
user_behavior_service.save_behavior_data_to_file('behavior_data.json')
