import uuid

from tinydb import TinyDB

from models import playermodel


class Match:
    def __init__(self, player_1, results_player_1, player_2,
                 results_player_2, id_round, id_player_1=None, id_player_2=None, id_match=None):
        if player_1 is not None:
            self.player_1 = player_1
        else:
            self.player_1 = playermodel.Player.load_player(id_player_1)
        if player_2 is not None:
            self.player_2 = player_2
        else:
            self.player_2 = playermodel.Player.load_player(id_player_2)
        self.results_player_1 = results_player_1
        self.results_player_2 = results_player_2
        if id_player_1 is None:
            self.id_player_1 = player_1.id_player
        else:
            self.id_player_1 = id_player_1
        if id_player_2 is None:
            self.id_player_2 = player_2.id_player
        else:
            self.id_player_2 = id_player_2
        self.id_round = id_round
        if id_match is None:
            self.id_match = uuid.uuid4()
        else:
            self.id_match = uuid.UUID(id_match)

    def serialized_match(self):
        return {
            'results_player_1': self.results_player_1,
            'results_player_2': self.results_player_2,
            'id_player_1': self.id_player_1.hex,
            'id_player_2': self.id_player_2.hex,
            'id_round': self.id_round.hex,
            'id_match': self.id_match.hex
        }

    @staticmethod
    def deserialized_match(serialized_match):
        return Match(
            id_round=uuid.UUID(serialized_match["id_round"]),
            id_match=serialized_match["id_match"],
            id_player_1=uuid.UUID(serialized_match["id_player_1"]),
            id_player_2=uuid.UUID(serialized_match["id_player_2"]),
            player_1=None,
            results_player_1=serialized_match["results_player_1"],
            player_2=None,
            results_player_2=serialized_match["results_player_2"],
        )

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

    @staticmethod
    def load_match():
        db = TinyDB('db.json')
        matches_table = db.table('matches')
        serialized_matches = matches_table.all()
        matches = []
        for serialized_match in serialized_matches:
            matches.append(Match.deserialized_match(serialized_match))
        return matches
