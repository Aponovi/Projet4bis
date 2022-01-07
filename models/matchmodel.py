import uuid

from tinydb import TinyDB, where

from models import playermodel


class Match:
    def __init__(self, player_1, results_player_1, player_2,
                 results_player_2, id_round, id_match=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.results_player_1 = results_player_1
        self.results_player_2 = results_player_2
        self.id_player_1 = player_1.id_player
        self.id_player_2 = player_2.id_player
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
            player_1=playermodel.Player.load_player(uuid.UUID(serialized_match["id_player_1"])),
            results_player_1=serialized_match["results_player_1"],
            player_2=playermodel.Player.load_player(uuid.UUID(serialized_match["id_player_2"])),
            results_player_2=serialized_match["results_player_2"],
        )

    def maj_results(self):
        db = TinyDB("db.json")
        table = db.table("matches")
        table.update({"results_player_1": str(self.results_player_1)}, where("id_match") == self.id_match.hex)
        table.update({"results_player_2": str(self.results_player_2)}, where("id_match") == self.id_match.hex)

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
