from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            if len(self.photos[page]) < self.MAX_PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return (f"{label} photo added successfully "
                        f"on page {page + 1} "
                        f"slot {len(self.photos[page])}")
        return "No more free slots"

    def display(self) -> str:
        result = [
            "-----------"
        ]

        for page in range(self.pages):
            curr_page = ['[]' for _ in self.photos[page]]
            result.append(' '.join(curr_page))
            result.append("-----------")

        return '\n'.join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())