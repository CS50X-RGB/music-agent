class MusicSearchError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        error_type: str = "music_search_error"
    ):
        self.message = message
        self.status_code = status_code
        self.error_type = error_type
        super().__init__(message)

    def to_dict(self):
        return {
            "success": False,
            "error": {
                "type": self.error_type,
                "status_code": self.status_code,
                "message": self.message
            }
        }