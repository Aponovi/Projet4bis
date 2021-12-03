class TournamentModel:
    """Modèle représentant un tournoi."""

    def __init__(self, name, place, start_date, end_date, round_instances, time, description, turn_number=4):
        """Initialise les détails relatifs au tournoi."""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_instances = round_instances
        self.time = time
        self.description = description
        self.turn_number = turn_number
        self.players = []

    def serialized_tournament(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'round_instances': self.round_instances,
            'time': self.time,
            'description': self.description,
            'turn_number': self.turn_number,
            'players': self.players,
            }

    def add_player(self, player):
        self.players.append(player)

    def tournament_results(self):
        """Cumule les scores des joueurs"""
        players_scores = {}
        for tour in self.round_instances:
            for match in tour:
                first_element = match[0]
                second_element = match[1]
                premier_joueur = first_element[0]
                deuxieme_joueur = second_element[0]
                if premier_joueur in players_scores:
                    players_scores[premier_joueur] += first_element[1]
                else:
                    players_scores[premier_joueur] = first_element[1]
                if deuxieme_joueur in players_scores:
                    players_scores[deuxieme_joueur] += second_element[1]
                else:
                    players_scores[deuxieme_joueur] = second_element[1]
        """Tri les joueurs selon leur score et leur classement"""
        players_scores_trie = []
        while len(players_scores) > 0:
            max_score = 0
            joueur_max_score = None
            for joueur in players_scores:
                if joueur_max_score is None:
                    max_score = players_scores[joueur]
                    joueur_max_score = joueur
                else:
                    if players_scores[joueur] > max_score:
                        max_score = players_scores[joueur]
                        joueur_max_score = joueur
                    elif players_scores[joueur] == max_score:
                        if joueur.ranking > joueur_max_score.ranking:
                            joueur_max_score = joueur
            players_scores_trie.append((joueur_max_score, players_scores[joueur_max_score]))
            del players_scores[joueur_max_score]
        return players_scores_trie
