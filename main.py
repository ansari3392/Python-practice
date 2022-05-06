"""
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""
from typing import List, Any


class League:

    def __init__(self, team_league: dict):
        self.team_league = {
            'spain': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'iran': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'portugal': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'morocco': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        }

    def __str__(self):
        ...

    def __repr__(self):
        ...

    @classmethod
    def get_matches_count_input(cls) -> int:
        result_count = int(input('Enter result count: '))
        return result_count

    @classmethod
    def get_matches_input(cls, number: int) -> list[str]:
        matches = input('enter the matches: ')
        match_list = []
        for i in range(0, number):
            result = input()
            match_list.append(result)
        return match_list

    @classmethod
    def get_results_input(cls, number: int) -> list[str]:
        results = input('enter the results: ')
        result_list = []
        for i in range(0, number):
            result = input()
            result_list.append(result)
        return result_list

    def get_result(self, match_list, result_list) -> dict:
        zipped_list = (list(zip(match_list, result_list)))

        for match, result in zipped_list:
            first_team = match.split('-')[0]
            first_team_result = result.split('-')[0]
            second_team = match.split('-')[1]
            second_team_result = result.split('-')[1]

            if first_team_result == second_team_result:
                self.team_league[first_team]['points'] += 1
                self.team_league[first_team]['draws'] += 1
                self.team_league[second_team]['points'] += 1
                self.team_league[second_team]['draws'] += 1

            elif first_team_result > second_team_result:
                goal_difference = int(first_team_result) - int(second_team_result)
                self.team_league[first_team]['win'] += 1
                self.team_league[first_team]['points'] += 3
                self.team_league[first_team]['goal difference'] += goal_difference

                self.team_league[second_team]['loses'] += 1
                self.team_league[second_team]['goal difference'] -= goal_difference

            elif second_team_result > first_team_result:
                goal_difference = int(second_team_result) - int(first_team_result)
                self.team_league[second_team]['win'] += 1
                self.team_league[second_team]['points'] += 3
                self.team_league[second_team]['goal difference'] += goal_difference

                self.team_league[first_team]['loses'] += 1
                self.team_league[first_team]['goal difference'] -= goal_difference

            return self.team_league

    def sort_result(self, team_league: dict) -> list[Any]:
        result = sorted(team_league.items(),
                        key=lambda k: (-k[1]['points'], -k[1]['win'], k[0]))
        return result

    def __call__(self, *args, **kwargs):
        result_count = self.get_matches_count_input()
        match_list = self.get_matches_input(result_count)
        result_list = self.get_results_input(result_count)
        team_league = self.get_result(match_list, result_list)
        result = self.sort_result(team_league)
        print(result)


league = League(team_league={
            'spain': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'iran': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'portugal': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'morocco': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        })

if __name__ == '__main__':
    league()
