class TournamentModel:
    """Modèle représentant un tournoi."""

    def __init__(self, name, place, start_date, end_date, round_instances, time, description,  turn_number=4):
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

    def add_player(self, player):
        self.players.append(player)
