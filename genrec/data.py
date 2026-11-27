from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "ml-1m"

def load_ratings(
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """加载用户评分数据。"""
    return pd.read_csv(
        Path(data_dir) / "ratings.dat",
        sep="::",
        engine="python",
        header=None,
        names=["user_id", "movie_id", "rating", "timestamp"],
        encoding="latin-1",
        dtype={
            "user_id": int,
            "movie_id": int,
            "rating": int,
            "timestamp": int,
        },
    )


def load_movies(
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """加载电影信息。"""
    return pd.read_csv(
        Path(data_dir) / "movies.dat",
        sep="::",
        engine="python",
        header=None,
        names=["movie_id", "title", "genres"],
        encoding="latin-1",
        dtype={"movie_id": int},
    )


def load_users(
    data_dir: Path = DEFAULT_DATA_DIR,
) -> pd.DataFrame:
    """加载用户信息。"""
    return pd.read_csv(
        Path(data_dir) / "users.dat",
        sep="::",
        engine="python",
        header=None,
        names=[
            "user_id",
            "gender",
            "age",
            "occupation",
            "zip_code",
        ],
        encoding="latin-1",
        dtype={
            "user_id": int,
            "age": int,
            "occupation": int,
            "zip_code": str,
        },
    )


def load_movielens(
    data_dir: Path = DEFAULT_DATA_DIR,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """加载完整的 MovieLens 1M 数据集。"""
    ratings = load_ratings(data_dir)
    movies = load_movies(data_dir)
    users = load_users(data_dir)

    return ratings, movies, users
