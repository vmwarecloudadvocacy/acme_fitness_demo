from locust import LoadTestShape
from locustfile import WebSiteUser

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
    total_runtime = 1200
    stages = [
        {"duration": 10, "users": 20, "spawn_rate": 5},
        {"duration": 150, "users": 50, "spawn_rate": 2},
        {"duration": 300, "users": 100, "spawn_rate": 5},
        {"duration": 450, "users": 150, "spawn_rate": 5},
        {"duration": 600, "users": 600, "spawn_rate": 50},
        {"duration": 750, "users": 400, "spawn_rate": 5},
        {"duration": 900, "users": 300, "spawn_rate": 1},
        {"duration": 1050, "users": 100, "spawn_rate": 5},
        {"duration": 1201, "users": 50, "spawn_rate": 1},
    ]
    def tick(self):
        run_time = self.get_run_time() % self.total_runtime
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
