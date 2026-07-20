class IDMixin:
    CURR_ID: int = 1

    @classmethod
    def get_next_id(cls):
        return cls.CURR_ID

    @classmethod
    def increment_id(cls):
        cls.CURR_ID += 1
