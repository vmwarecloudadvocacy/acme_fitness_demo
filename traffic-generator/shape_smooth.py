from locust import LoadTestShape
from locustfile import WebSiteUser
import os

class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """
    shape_runtime = 1800
    if (os.environ.get('SHAPE_RUNTIME_SECONDS')):
        shape_runtime = int(os.environ.get('SHAPE_RUNTIME_SECONDS'))

    max_users = 600
    if (os.environ.get('MAX_USERS')):
        max_users = int(os.environ.get('MAX_USERS'))


    stages = [
            {"duration": shape_runtime * 1/10, "users": max_users * 1/6, "spawn_rate": 1},
            {"duration": shape_runtime * 1/5, "users": max_users *1/3, "spawn_rate": 1},
            {"duration": shape_runtime * 3/10, "users": max_users *1/2, "spawn_rate": 1},
            {"duration": shape_runtime * 2/5, "users": max_users *2/3, "spawn_rate": 1},
            {"duration": shape_runtime * 1/2, "users": max_users *1, "spawn_rate": 1},
            {"duration": shape_runtime * 3/5, "users": max_users *2/3, "spawn_rate": 1},
            {"duration": shape_runtime * 3/4, "users": max_users *1/2, "spawn_rate": 1},
            {"duration": shape_runtime * 4/5, "users": max_users *1/3, "spawn_rate": 1},
            {"duration": shape_runtime * 9/10, "users": max_users *1/6, "spawn_rate": 1},
            {"duration": shape_runtime + 1, "users": max_users *1/12, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time() % self.shape_runtime
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
