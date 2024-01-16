from models.base_model import BaseModel


class Review(BaseModel):
    """Place class represents a place in a city. It has an id, name and actions
    associated with it."""

    place_id = ""
    user_id = ""
    text = ""
