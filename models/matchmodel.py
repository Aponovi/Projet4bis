class Match:
    def __init__(self, player_1, results_player_1, player_2, results_player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.results_player_1 = results_player_1
        self.results_player_2 = results_player_2

    def match_tuple(self):
        return [self.player_1, self.results_player_1], [self.player_2, self.results_player_2]

    @staticmethod
    def historic_match(round_instance, index_player_1, index_player_2, players):
        for i in range(len(round_instance)):
            tour = round_instance[i]
            for k in range(len(tour)):
                match = tour[k]
                if (match[0][0] == players[index_player_1] and match[1][0] == players[index_player_2]) \
                        or (match[0][0] == players[index_player_2] and match[1][0] == players[index_player_1]):
                    return True
        return False
