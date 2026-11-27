
import pytest

from genrec.data import (
    load_ratings,
    load_movies,
    load_users,
    load_movielens,
)


@pytest.fixture
def sample_data(tmp_path):
    """创建测试用的微型 MovieLens 数据集。"""

    (tmp_path / "ratings.dat").write_text(
        "1::1::5::978300760\n"
        "2::2::4::978302109\n",
        encoding="latin-1",
    )

    (tmp_path / "movies.dat").write_text(
        "1::Toy Story (1995)::Animation|Comedy\n"
        "2::Amélie (2001)::Comedy|Romance\n",
        encoding="latin-1",
    )

    (tmp_path / "users.dat").write_text(
        "1::F::25::10::02138\n"
        "2::M::35::16::70072\n",
        encoding="latin-1",
    )

    return tmp_path


def test_load_ratings(sample_data):
    ratings = load_ratings(sample_data)

    assert ratings.shape == (2, 4)
    assert ratings.iloc[0]["rating"] == 5
    assert ratings.columns.tolist() == [
        "user_id", "movie_id", "rating", "timestamp"
    ]


def test_load_movies(sample_data):
    movies = load_movies(sample_data)

    assert movies.shape == (2, 3)
    assert movies.iloc[0]["title"] == "Toy Story (1995)"
    assert movies.iloc[1]["title"] == "Amélie (2001)"


def test_load_users(sample_data):
    users = load_users(sample_data)

    assert users.shape == (2, 5)
    assert users.iloc[0]["zip_code"] == "02138"


def test_load_movielens(sample_data):
    ratings, movies, users = load_movielens(sample_data)

    assert len(ratings) == 2
    assert len(movies) == 2
    assert len(users) == 2

    assert ratings["user_id"].isin(users["user_id"]).all()
    assert ratings["movie_id"].isin(movies["movie_id"]).all()


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_ratings(tmp_path)
