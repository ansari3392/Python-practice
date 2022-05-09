import unittest
from unittest.mock import patch

from practice1 import League


def get_inputs():
    return [
        '3',
        'iran-spain',
        'iran-portugal',
        'iran-morocco',
        '1-1',
        '2-1',
        '3-2'
    ]


def get_matches():
    return [
        'iran-spain',
        'iran-portugal',
        'iran-morocco'
    ]


def get_results():
    return [
        '1-1',
        '2-2',
        '1-2'
    ]


class TestLeague(unittest.TestCase):

    @patch('builtins.input')
    def test_get_matches_count(self, mock_input):
        mock_input.return_value = '6'
        league = League()
        self.assertEqual(league.matches_count, 0)
        league._get_matches_count()
        self.assertEqual(league.matches_count, 6)

    @patch('builtins.input', side_effect=get_matches())
    def test_get_matches(self, mock_input):
        league = League()
        league.matches_count = 3
        self.assertEqual(league.matches_list, [])
        league._get_matches()
        self.assertEqual(league.matches_list, ['iran-spain', 'iran-portugal', 'iran-morocco'])

    def test_get_team_name(self):
        league = League()
        league.matches_list = ['iran-spain', 'iran-portugal']
        self.assertEqual(len(league.team_name), 0)
        league._get_team_name()
        self.assertEqual(len(league.team_name), 3)

    def test_create_team_league(self):
        league = League()
        league.team_name = ['iran', 'portugal']
        self.assertEqual(len(league.team_league), 0)
        league._create_team_league()
        self.assertEqual(len(league.team_league), 2)

    @patch('builtins.input', side_effect=get_results())
    def test_get_results_input(self, mock_input):
        league = League()
        league.matches_list = ['iran-spain', 'iran-portugal', 'iran-morocco']
        self.assertEqual(league.results_list, [])
        league._get_results_input()
        self.assertEqual(league.results_list, ['1-1', '2-2', '1-2'])

    def test_process(self):
        league = League()
        league.matches_list = ['iran-spain', 'iran-portugal', 'iran-morocco']
        league.results_list = ['1-1', '2-2', '2-2']
        league.team_name = []
        league.team_league = {}
        league._process()

        self.assertEqual(league.team_league['spain']['win'], 0)
        self.assertEqual(league.team_league['spain']['loses'], 0)
        self.assertEqual(league.team_league['spain']['draws'], 1)
        self.assertEqual(league.team_league['spain']['goal difference'], 0)
        self.assertEqual(league.team_league['spain']['points'], 1)
        self.assertEqual(league.team_league['iran']['win'], 0)
        self.assertEqual(league.team_league['iran']['loses'], 0)
        self.assertEqual(league.team_league['iran']['draws'], 3)
        self.assertEqual(league.team_league['iran']['goal difference'], 0)
        self.assertEqual(league.team_league['iran']['points'], 3)
        self.assertEqual(league.team_league['portugal']['win'], 0)
        self.assertEqual(league.team_league['portugal']['loses'], 0)
        self.assertEqual(league.team_league['portugal']['draws'], 1)
        self.assertEqual(league.team_league['portugal']['goal difference'], 0)
        self.assertEqual(league.team_league['portugal']['points'], 1)
        self.assertEqual(league.team_league['morocco']['win'], 0)
        self.assertEqual(league.team_league['morocco']['loses'], 0)
        self.assertEqual(league.team_league['morocco']['draws'], 1)
        self.assertEqual(league.team_league['morocco']['goal difference'], 0)
        self.assertEqual(league.team_league['morocco']['points'], 1)

    def test_sort_league(self):
        league = League()
        league.team_league = {
            'spain': {'win': 2, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 3},
            'iran': {'win': 3, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 6},
            'portugal': {'win': 2, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 3},
            'morocco': {'win': 2, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 3},
        }
        my_league = list(league.team_league)
        self.assertEqual(my_league[0], 'spain')
        league._sort_league()
        my_league = list(league.team_league)
        self.assertEqual(my_league[0], 'iran')
        self.assertEqual(my_league[1], 'morocco')
        self.assertEqual(my_league[2], 'portugal')
        self.assertEqual(my_league[3], 'spain')

    @patch('builtins.input', side_effect=get_inputs())
    def test_get_data(self, mock_input):
        league = League()
        self.assertEqual(league.matches_count, 0)
        self.assertEqual(league.matches_list, [])
        self.assertEqual(league.results_list, [])
        league._get_matches_count()
        league._get_matches()
        league._get_results_input()
        self.assertEqual(league.matches_count, 3)
        self.assertEqual(league.matches_list, ['iran-spain', 'iran-portugal', 'iran-morocco'])
        self.assertEqual(league.results_list, ['1-1', '2-1', '3-2'])

    @patch('builtins.input', side_effect=get_inputs())
    def test_call(self, mock_input):
        league = League()
        league._get_team_name()
        league._create_team_league()
        self.assertEqual(league.matches_count, 0)
        self.assertEqual(league.matches_list, [])
        self.assertEqual(league.results_list, [])
        league._get_data()
        self.assertEqual(league.matches_count, 3)
        self.assertEqual(league.matches_list, ['iran-spain', 'iran-portugal', 'iran-morocco'])
        self.assertEqual(league.results_list, ['1-1', '2-1', '3-2'])
        league._process()
        self.assertEqual(league.team_league['spain']['win'], 0)
        self.assertEqual(league.team_league['spain']['loses'], 0)
        self.assertEqual(league.team_league['spain']['draws'], 1)
        self.assertEqual(league.team_league['spain']['goal difference'], 0)
        self.assertEqual(league.team_league['spain']['points'], 1)
        self.assertEqual(league.team_league['iran']['win'], 2)
        self.assertEqual(league.team_league['iran']['loses'], 0)
        self.assertEqual(league.team_league['iran']['draws'], 1)
        self.assertEqual(league.team_league['iran']['goal difference'], 2)
        self.assertEqual(league.team_league['iran']['points'], 7)
        self.assertEqual(league.team_league['portugal']['win'], 0)
        self.assertEqual(league.team_league['portugal']['loses'], 1)
        self.assertEqual(league.team_league['portugal']['draws'], 0)
        self.assertEqual(league.team_league['portugal']['goal difference'], -1)
        self.assertEqual(league.team_league['portugal']['points'], 0)
        self.assertEqual(league.team_league['morocco']['win'], 0)
        self.assertEqual(league.team_league['morocco']['loses'], 1)
        self.assertEqual(league.team_league['morocco']['draws'], 0)
        self.assertEqual(league.team_league['morocco']['goal difference'], -1)
        self.assertEqual(league.team_league['morocco']['points'], 0)
        league._sort_league()


if __name__ == '__main__':
    unittest.main()
