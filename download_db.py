"""Download the SQLite Chinook sample database from its source repository."""

from pathlib import Path
from shutil import copyfileobj
from urllib.request import Request, urlopen

DATABASE_URL = (
    "https://raw.githubusercontent.com/lerocha/chinook-database/"
    "master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
)
OUTPUT_PATH = Path(__file__).parent / "data" / "Chinook_Sqlite.sqlite"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = OUTPUT_PATH.with_suffix(".sqlite.tmp")
    request = Request(DATABASE_URL, headers={"User-Agent": "querying-sql-python/1.0"})

    try:
        with urlopen(request, timeout=30) as response, temporary_path.open("wb") as target:
            copyfileobj(response, target)
        if temporary_path.stat().st_size == 0:
            raise OSError("The downloaded database is empty.")
        temporary_path.replace(OUTPUT_PATH)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise

    print(f"Downloaded Chinook SQLite database to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

