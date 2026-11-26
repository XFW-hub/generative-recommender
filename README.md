# GenRec-Qwen：基于大语言模型的生成式推荐系统

## 项目简介

本项目旨在从零构建一个基于 Qwen 大语言模型的生成式电影推荐系统，以 MovieLens 1M 为实验数据集，探索传统推荐算法与大语言模型相结合的推荐方案，并进一步实现基于 Semantic ID 的生成式推荐架构。

项目覆盖数据处理、用户兴趣建模、多路召回、排序、重排、离线评估、模型微调及在线推荐服务等完整流程。

## 项目目标

- 实现热门召回、TF-IDF 召回与 ItemCF 协同过滤召回。
- 利用 Qwen 大模型实现基于用户历史行为的生成式召回。
- 构建多路召回融合与 LightGBM 排序模型。
- 实现基于 RQ-VAE 的物品语义编码。
- 通过 LoRA 微调实现基于 Semantic ID 的生成式推荐。
- 构建完整的推荐效果评估体系。
- 实现推荐系统的在线服务与容器化部署。

## 技术栈

| 模块 | 技术选型 |
|---|---|
| 开发语言 | Python |
| 实验数据 | MovieLens 1M |
| 数据处理 | Pandas、NumPy |
| 推荐算法 | ItemCF、TF-IDF、LightGBM、SASRec |
| 大语言模型 | Qwen、Ollama |
| 生成式推荐 | RQ-VAE、Semantic ID、LoRA |
| 服务框架 | FastAPI |
| 数据存储与缓存 | PostgreSQL、Redis |
| 工程化 | Docker、GitHub Actions、pytest |

## 快速开始

创建虚拟环境：

```bash
conda create -n genrec python=3.11 -y
conda activate genrec
```

安装项目依赖：

```bash
pip install -r requirements.txt
```

## 开发进度

- [x] 项目初始化与环境配置
- [ ] 数据加载与预处理
- [ ] 用户画像与特征工程
- [ ] 传统推荐算法
- [ ] Qwen 生成式召回
- [ ] 多路召回融合
- [ ] LightGBM 排序
- [ ] 推荐系统离线评估
- [ ] Semantic ID 构建
- [ ] 大语言模型微调
- [ ] 在线推荐服务
- [ ] Docker 容器化部署
- [ ] CI/CD 自动化测试

## 数据集

本项目使用 GroupLens 发布的 MovieLens 1M 数据集。

下载地址：https://grouplens.org/datasets/movielens/1m/

原始数据集不包含在本仓库中，请遵循数据集使用许可自行下载。

## 参考项目

- GenRecWithQwen：https://github.com/ZHAOoops/GenRecWithQwen
- Qwen：https://github.com/QwenLM/Qwen
- MovieLens：https://grouplens.org/datasets/movielens/

本项目参考上述开源项目的技术思路，并进行独立实现与功能扩展。

## 当前状态

项目正在持续开发中，目前处于初始化阶段。