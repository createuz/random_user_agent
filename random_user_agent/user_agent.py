import json
import os
import random


class UserAgent:
    ATTRIBUTES_MAP = {
        'hardware_types': [],
        'software_types': [],
        'software_names': [],
        'software_engines': [],
        'operating_systems': [],
        'popularity': [],
    }

    def __init__(self, limit=None, *args, **kwargs):
        self.user_agents = []

        for attribute, values in self.ATTRIBUTES_MAP.items():
            setattr(self, attribute, set([v.lower() for v in values]))

        self.load_user_agents()

        if limit is not None:
            self.user_agents = random.sample(self.user_agents, min(limit, len(self.user_agents)))

    def load_user_agents(self):
        #   user_agents.jl   in    user_agents.zip
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user_agents.jl')

        with open(file_path) as user_agents_file:
            for line in user_agents_file:
                user_agent = json.loads(line)
                if self.check_user_agent(user_agent):
                    self.user_agents.append(user_agent)

    def check_user_agent(self, user_agent):
        for attribute, values in self.ATTRIBUTES_MAP.items():
            if values and user_agent[attribute].lower() not in values:
                return False
        return True

    def get_user_agents(self):
        return self.user_agents

    def get_random_user_agent(self):
        return random.choice(self.user_agents)['user_agent']


fake_agent = UserAgent()
print(fake_agent.get_random_user_agent())
