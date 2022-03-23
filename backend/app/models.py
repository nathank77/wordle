from datetime import datetime, timedelta

class Movie:

    class MovieCompare:
        def __init__(self, title_eq, director_eq, time_diff, runtime_diff, rating_diff, box_office_diff):
            self.title_eq = title_eq
            self.director_eq = director_eq
            self.time_diff = time_diff
            self.runtime_diff = runtime_diff
            self.rating_diff = rating_diff
            self.box_office_diff = box_office_diff

        def jsonify(self):
            return {"TitleEquality": self.title_eq,
                    "DirectorEquality": self.director_eq,
                    "ReleaseDateDifference": self.time_diff,
                    "RuntimeDifference": self.runtime_diff,
                    "imdbRatingDifference": self.rating_diff,
                    "BoxOfficeDifference": self.box_office_diff
                    }

    def __init__(self, title, director, release_date, runtime, imdb_rating, box_office):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.runtime = runtime
        self.imdb_rating = imdb_rating
        self.box_office = box_office

    def jsonify(self):
        return {"Title": self.title,
                "Director": self.director,
                "ReleaseDate": self.release_date,
                "Runtime": self.runtime,
                "imdbRating": self.imdb_rating,
                "BoxOfficeGross": self.box_office }

    def __eq__(self, other):
        self.compared = self.MovieCompare(
            self.title == other.title,
            self.director == other.director,
            (self.release_date - other.release_date).total_seconds()/86400,
            self.runtime - other.runtime,
            self.imdb_rating - other.imdb_rating,
            self.box_office - other.box_office
        )
        return self.compared
