import datetime


class Round:
    """Modèle représentant un tour."""
    def __init__(self, name, start_date, end_date, matches):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches

    def __init__(self, tournament):
        nb_round_past = len(tournament.round_instances)
        self.name = "Round " + str(nb_round_past)
        self.start_date = datetime.datetime.now()
        self.end_date = None
        self.matches = None

    def generate_first_pair(self, players, round_row):
        """Premières paires générées selon le système de tournoi suisse"""
        nb_players = len(players)
        # tri des joueurs par classement
        players = sorted(players, key=lambda player: player.ranking, reverse=True)
        middle_list = int(nb_players / 2)
        players_sup = players[0: middle_list]
        players_inf = players[middle_list:nb_players]
        nb_matches = len(players_sup)
        for index in range(nb_matches):
            competitors = ([players_sup[index], 0], [players_inf[index], 0])
            round_row.append(competitors)

    def sorting_players(self, round_instance):
        """Cumule les scores des joueurs"""
        players_scores = {}
        for tour in round_instance:
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
        players = []
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
            players.append(joueur_max_score)
            del players_scores[joueur_max_score]

    def pair_player(self, players, round_instance, round_row):
        nb_players = len(players)
        self.sorting_players(round_instance)
        nb_matches = int(nb_players / 2)
        index_player_1 = 0
        index_player_2 = 1
        index_player_2_tmp = 1
        previous_matches = []
        for m in range(nb_matches):
            # recherche dans round_instance les matches précédents pour savoir si les joueurs se sont déjà rencontrés
            while self.historic_match(index_player_1, index_player_2_tmp):
                index_player_2_tmp += 1
                if index_player_2_tmp > nb_players - 1:
                    index_player_2_tmp = index_player_2
                    break
            index_player_2 = index_player_2_tmp
            competitors = ([players[index_player_1], 0], [players[index_player_2], 0])
            round_row.append(competitors)
            previous_matches.append(index_player_1)
            previous_matches.append(index_player_2)

            # joueur in self.players avec plus petit indice n'ayant pas encore de match
            for ind in range(len(players)):
                if ind not in previous_matches:
                    index_player_1 = ind
            for ind in range(index_player_1 + 1, len(players)):
                if ind not in previous_matches:
                    index_player_2 = ind
                    index_player_2_tmp = ind

    def generate_pair(self, players, round_instance):
        nb_players = len(players)
        if nb_players % 2 == 0 and nb_players > 0:
            round_row = []
            if len(round_instance) == 0:
                self.generate_first_pair(players, round_row)
            else:
                self.pair_player(players, round_instance, round_row)
            self.matches = round_row
            round_instance.append(round_row)

    # TODO
    def historic_match(self, index_player_1, index_player_2):
        return False

    # TODO
    def finished_match(self):
        pass
