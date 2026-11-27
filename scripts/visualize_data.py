
import matplotlib.pyplot as plt

from genrec.data import load_movielens, PROJECT_ROOT


def main():
    ratings, movies, users = load_movielens()

    output_dir = PROJECT_ROOT / "outputs" / "eda"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 评分分布
    ratings["rating"].value_counts().sort_index().plot(
        kind="bar",
        title="Rating Distribution",
        xlabel="Rating",
        ylabel="Count",
    )
    plt.tight_layout()
    plt.savefig(output_dir / "rating_distribution.png")
    plt.close()

    # 2. 用户活跃度分布
    user_activity = ratings.groupby("user_id").size()

    user_activity.plot(
        kind="hist",
        bins=50,
        title="User Activity Distribution",
        xlabel="Number of Ratings",
    )
    plt.tight_layout()
    plt.savefig(output_dir / "user_activity.png")
    plt.close()

    # 3. 电影热度长尾分布
    movie_popularity = (
        ratings.groupby("movie_id")
        .size()
        .sort_values(ascending=False)
    )

    plt.plot(movie_popularity.to_numpy())
    plt.title("Movie Popularity Long Tail")
    plt.xlabel("Movie Popularity Rank")
    plt.ylabel("Number of Ratings")
    plt.tight_layout()
    plt.savefig(output_dir / "movie_popularity.png")
    plt.close()

    print(f"图表已保存至: {output_dir}")


if __name__ == "__main__":
    main()
