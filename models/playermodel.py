import uuid


class Player:
    """Modèle représentant un joueur."""

    def __init__(self, name, first_name, birth_date, gender, ranking, id_tournament):
        """Initialise les détails relatifs au joueur."""
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.id_player = uuid.uuid4()
        self.id_tournament = id_tournament

    def serialized_player(self):
        return {
            'name': self.name,
            'first_name': self.first_name,
            'birth_date': str(self.birth_date),
            'gender': self.gender,
            'ranking': self.ranking,
            'id_player': self.id_player.hex,
            'id_tournament': self.id_tournament.hex
            }

    def update_ranking(self, new_ranking):
        self.ranking = new_ranking
