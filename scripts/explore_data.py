
import pandas as pd

from genrec.data import load_movielens


def main():
    ratings, movies, users = load_movielens()

    # 1. 数据基本规模
    print("\n========== 数据基本信息 ==========")

    n_users = ratings["user_id"].nunique()
    n_movies = ratings["movie_id"].nunique()
    n_interactions = len(ratings)

    print(f"用户数量: {n_users}")
    print(f"电影库数量: {len(movies)}")
    print(f"有评分的电影数量: {n_movies}")
    print(f"评分数量: {n_interactions}")

    # 2. 数据质量检查
    print("\n========== 数据质量 ==========")

    for name, df in [
        ("ratings", ratings),
        ("movies", movies),
        ("users", users),
    ]:
        print(f"{name} 缺失值: {df.isna().sum().sum()}")
        print(f"{name} 重复行: {df.duplicated().sum()}")

    print(
        "重复用户-电影交互:",
        ratings.duplicated(["user_id", "movie_id"]).sum(),
    )

    print(
        "无效评分:",
        (~ratings["rating"].between(1, 5)).sum(),
    )

    print(
        "无法匹配的用户:",
        (~ratings["user_id"].isin(users["user_id"])).sum(),
    )

    print(
        "无法匹配的电影:",
        (~ratings["movie_id"].isin(movies["movie_id"])).sum(),
    )

    # 3. 评分分布
    print("\n========== 评分分布 ==========")
    print(ratings["rating"].value_counts().sort_index())
    print(f"平均评分: {ratings['rating'].mean():.4f}")

    # 4. 用户活跃度
    print("\n========== 用户活跃度 ==========")
    user_activity = ratings.groupby("user_id").size()
    print(user_activity.describe())

    # 5. 电影热度
    print("\n========== 最热门的10部电影 ==========")
    movie_popularity = (
        ratings.groupby("movie_id")
        .size()
        .reset_index(name="interaction_count")
        .merge(
            movies[["movie_id", "title"]],
            on="movie_id",
            how="left",
        )
        .sort_values("interaction_count", ascending=False)
    )

    print(movie_popularity.head(10).to_string(index=False))

    # 6. 电影类型分布
    print("\n========== 电影类型分布 ==========")
    genre_counts = (
        movies["genres"]
        .str.split("|", regex=False)
        .explode()
        .value_counts()
    )
    print(genre_counts)

    # 7. 交互矩阵稀疏度
    print("\n========== 数据稀疏度 ==========")

    n_unique_pairs = len(
        ratings.drop_duplicates(["user_id", "movie_id"])
    )

    density = n_unique_pairs / (n_users * n_movies)
    sparsity = 1 - density

    print(f"矩阵密度: {density:.4%}")
    print(f"矩阵稀疏度: {sparsity:.4%}")

    # 8. 时间范围
    print("\n========== 交互时间范围 ==========")
    timestamps = pd.to_datetime(
        ratings["timestamp"],
        unit="s",
        utc=True,
    )

    print(f"最早评分时间: {timestamps.min()}")
    print(f"最晚评分时间: {timestamps.max()}")


if __name__ == "__main__":
    main()
