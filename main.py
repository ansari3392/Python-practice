"""
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""


class League:

    def __str__(self):
        ...

    def __repr__(self):
        ...

    def __call__(self, *args, **kwargs):
        team_league = {
            'spain': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'iran': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'portugal': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
            'morocco': {'win': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
        }

        result_count = int(input('Enter result count: '))

        match_list = []
        for i in range(0, result_count):
            result = input('Enter match: ')
            match_list.append(result)

        result_list = []
        for i in range(0, result_count):
            result = input('Enter result: ')
            result_list.append(result)

        zipped_list = (list(zip(match_list, result_list)))

        for match, result in zipped_list:
            first_team = match.split('-')[0]
            first_team_result = result.split('-')[0]
            second_team = match.split('-')[1]
            second_team_result = result.split('-')[1]

            if first_team_result == second_team_result:
                team_league[first_team]['points'] += 1
                team_league[first_team]['draws'] += 1
                team_league[second_team]['points'] += 1
                team_league[second_team]['draws'] += 1

            elif first_team_result > second_team_result:
                goal_difference = int(first_team_result) - int(second_team_result)
                team_league[first_team]['win'] += 1
                team_league[first_team]['points'] += 3
                team_league[first_team]['goal difference'] += goal_difference

                team_league[second_team]['loses'] += 1
                team_league[second_team]['goal difference'] -= goal_difference

            elif second_team_result > first_team_result:
                goal_difference = int(second_team_result) - int(first_team_result)
                team_league[second_team]['win'] += 1
                team_league[second_team]['points'] += 3
                team_league[second_team]['goal difference'] += goal_difference

                team_league[first_team]['loses'] += 1
                team_league[first_team]['goal difference'] -= goal_difference

        # sorted takes three parameters(iterabale, key, reverse)
        # here as we have dict so we use dict.items that return a tuple
        # key is a function

        result = sorted(team_league.items(),
                        key=lambda k: (-k[1]['points'], -k[1]['win'], k[0]))
        print(result)


league = League()

if __name__ == '__main__':
    league()
