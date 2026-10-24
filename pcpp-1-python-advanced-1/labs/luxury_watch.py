class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1
        self._engraving_text = None

    @classmethod
    def with_engraving_text(cls, text):
        try:
            cls.validate_engraving_text(text)
        except ValueError as e:
            raise ValueError(f"Engraving text is not valid: {e}") from e

        self = cls()
        self._engraving_text = text

        return self

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @staticmethod
    def validate_engraving_text(text):
        max_text_length = 40

        if len(text) > max_text_length:
            raise ValueError(
                f"Engraving text should not be longer than {max_text_length}"
            )

        if not text.isalnum():
            raise ValueError(
                "Engraving text can only have alpha-numeric characters, spaces are not allowed!"
            )

        return text

    def __str__(self):
        return f"{self.__class__.__name__}({self._engraving_text=})"


if __name__ == "__main__":
    try:
        regular_watch = LuxuryWatch()
        print("Regular watch:", regular_watch)

        watch_with_engraving = LuxuryWatch.with_engraving_text("Paulo")
        print("Watch with engraving:", watch_with_engraving)

        watch_with_invalid_engraving = LuxuryWatch.with_engraving_text("foo@baz.com")
        print("Watch with invalid engraving", watch_with_invalid_engraving)
    except ValueError as e:
        print(e)

    print()
    print("Created watches:", LuxuryWatch.get_number_of_watches_created())
