class Band:
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @property
    def concerts(self):
        return self._concerts

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise ValueError("Concert must be an instance of Concert class")
        self._concerts.append(concert)

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band.add_concert(self)
        venue.add_concert(self)
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Date must be a non-empty string")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise ValueError("Band must be of type Band")
        self._band = value

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def hometown_show(self):
        return self.venue.city == self.band.hometown


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("City must be a non-empty string")
        self._city = value

    @property
    def concerts(self):
        return self._concerts

    def add_concert(self, concert):
        if isinstance(concert, Concert) and concert not in self._concerts:
            self._concerts.append(concert)

    def bands(self):
        return list(set(concert.band for concert in self._concerts))