"""
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""
from pprint import pprint


class League:

    def __init__(self):
        self.team_league = {
            'spain': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'iran': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'portugal': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'morocco': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        }
        self.matches_list = []
        self.results_list = []
        self.matches_count = 0

    def __str__(self):
        ...

    def __repr__(self):
        ...

    def _get_matches_count(self) -> None:
        matches_count = int(input('Enter matches count: '))
        self.matches_count = matches_count

    def _get_matches(self) -> None:
        counter = 0
        for i in range(self.matches_count):
            counter += 1
            result = input(f'Enter match {counter}: ')
            self.matches_list.append(result)

    def _get_results_input(self) -> None:
        counter = 0
        for match in self.matches_list:
            counter += 1
            result = input(f'Enter result of {match}: ')
            self.results_list.append(result)

    def _process(self) -> dict:
        zipped_list = (list(zip(self.matches_list, self.results_list)))

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

    def _sort_league(self) -> None:
        sorted(
            self.team_league.items(),
            key=lambda k: (-k[1]['points'], -k[1]['win'], k[0])
        )

    def _get_data(self) -> None:
        self._get_matches_count()
        self._get_matches()
        self._get_results_input()

    def __call__(self, *args, **kwargs):
        self._get_data()
        self._process()
        self._sort_league()
        pprint(self.team_league)


if __name__ == '__main__':
    league = League()
    league()
