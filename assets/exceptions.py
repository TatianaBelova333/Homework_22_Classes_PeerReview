# Exceptions for Storage, Store, Shop


class StorageFull(Exception):
    """In case item is added when no capacity left"""
    def __init__(self, message='Capacity exceeded'):
        self.message = message
        super().__init__(message)


class ItemsNotFound(Exception):
    """In case not stored title passed or quantity requested greater than stored"""
    def __init__(self, message='Items not found'):
        self.message = message
        super().__init__(message)


class MessageError(Exception):
    """If wrong message passed"""
    def __init__(self, message='Incorrect message'):
        self.message = message
        super().__init__(message)
