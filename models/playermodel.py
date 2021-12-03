class Player:
    """Modèle représentant un joueur."""

    def __init__(self, name, first_name, birth_date, gender, ranking):
        """Initialise les détails relatifs au joueur."""
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def serialized_player(self):
        return {
            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'ranking': self.ranking
            }
