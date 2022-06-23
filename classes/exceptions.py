# Exceptions for Storage, Store, Shop


class StorageFull(Exception):
    """In case item is added when no capacity left"""
    def __init__(self, message=None):
        super().__init__(message)


class ShopFull(Exception):
    """In case title is added in excess of titles limit"""
    def __init__(self, message=None):
        super().__init__(message)


class NotFound(Exception):
    """In case not stored title passed"""
    def __init__(self, message=None):
        super().__init__(message)

class MessageError(Exception):
    """In case not stored title passed"""
    def __init__(self, message=None):
        super().__init__(message)


class NotEnough(Exception):
    """In case quantity requested in excess of stored quantity"""
    def __init__(self, message=None):
        super().__init__(message)
