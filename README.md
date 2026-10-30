# 招聘信息采集与职业技能需求分析系统

<p align="center">
  基于 Python 的招聘信息采集、数据处理与可视化分析项目
</p>

## 1. 项目简介

本项目是一个基于 Python 开发的招聘信息采集与职业技能需求分析系统，主要围绕网络招聘信息展开，实现了从数据采集、数据清洗、数据存储到数据分析与可视化的完整实践流程。

项目通过调用招聘网站 API 接口获取招聘信息，利用 Python 对采集的数据进行清洗和整理，并将处理后的数据存储至 Ubuntu 虚拟机中 Docker 部署的 MySQL 数据库。

在数据分析阶段，使用 Python 编写职业技能相关的数据处理程序，并在 Ubuntu 虚拟机环境中开展 Hadoop MapReduce Mapper/Reducer 编程实践。最后，通过部署在 Docker 环境中的 Redash 连接 MySQL 数据库，对招聘岗位数量、地区分布及职业技能需求等多个维度进行查询与可视化分析。

本项目主要用于实践 Python 网络数据采集、数据清洗、数据库管理、MapReduce 编程及数据可视化等技术。

## 2. 项目技术栈

| 技术类别 | 使用技术 |
|---|---|
| 开发语言 | Python |
| 数据采集 | Requests、HTTP API |
| 数据处理 | Pandas、Python |
| 数据库 | MySQL、PyMySQL |
| 数据处理实践 | Hadoop MapReduce（Mapper/Reducer） |
| 数据可视化 | Redash |
| 运行环境 | Windows、Ubuntu |
| 容器部署 | Docker |

## 3. 项目整体流程

项目主要分为以下几个阶段：

1. **数据采集：** 通过 Python 调用招聘网站 API 接口，根据职业类别及关键词获取招聘信息。
2. **数据清洗：** 对采集到的招聘信息进行初步清洗，处理无效数据和重复数据，整理后续分析所需的数据。
3. **数据存储：** 使用 PyMySQL 建立数据库连接，将清洗后的招聘信息写入 MySQL 数据库。
4. **技能数据处理：** 对招聘信息中的职业技能进行提取与整理，使用 Python 编写 Mapper 和 Reducer 程序，在 Ubuntu 虚拟机环境中进行 MapReduce 编程实践。
5. **数据可视化：** 使用 Redash 连接 MySQL 数据库，通过 SQL 查询和图表展示招聘岗位及职业技能需求情况。

## 4. 项目运行架构

项目采用 Windows 宿主机与 Ubuntu 虚拟机相结合的运行方式。

- **Windows 宿主机：** 主要用于 Python 项目开发、代码编写及调试。
- **Ubuntu 虚拟机：** 提供后端数据处理及相关服务的运行环境。
- **Docker：** 在 Ubuntu 虚拟机中部署 MySQL、Redash 等服务。
- **MySQL：** 负责存储清洗后的招聘信息，为后续数据查询与分析提供数据支持。
- **Hadoop MapReduce：** 在 Ubuntu 环境中进行 Mapper/Reducer 编程及相关数据处理实践。
- **Redash：** 连接 MySQL 数据库，通过 SQL 查询构建数据分析图表与仪表盘。

## 5. 核心模块介绍

| 文件或模块 | 主要功能 |
|---|---|
| jobs_types.py | 使用字典维护职业名称及对应代码，为招聘信息采集提供职业分类参数 |
| spider_for_data.py | 项目主程序，负责调用相关模块，完成招聘信息采集及流程调度 |
| data_clean.py | 数据清洗模块，对采集到的招聘信息进行初步清洗和整理 |
| data_save.py | 数据存储模块，将处理后的招聘信息写入 MySQL 数据库 |
| mysql_connect.py | 数据库连接模块，建立 Python 程序与 MySQL 数据库之间的连接 |
| skill_mapper.py | Mapper 程序，对输入的职业技能数据进行映射处理 |
| skill_reducer.py | Reducer 程序，对映射结果进行汇总与统计 |

## 6. 数据可视化展示

项目使用 Redash 对招聘信息进行多维度分析，通过 SQL 查询与图表展示招聘市场中的岗位需求及职业技能分布情况。

主要分析内容包括：

- **岗位数量分析：** 统计不同职业类别的招聘岗位数量，观察不同岗位的招聘需求。
- **地区分布分析：** 对招聘岗位的地区分布进行统计，分析不同地区的招聘需求差异。
- **职业技能分析：** 统计招聘信息中出现的职业技能，了解不同岗位对专业技能的需求情况。

### 可视化效果展示

![Redash数据分析仪表盘](/images/dashboard.png)

## 7. 项目目录结构

```text
PythonProject/
│
├── data_process/
│   ├── data_clean.py
│   ├── data_save.py
│   ├── mysql_connect.py
│   │
│   └── mapreduce/
│       ├── skill_mapper.py
│       └── skill_reducer.py
│
├── spider/
│   ├── jobs_types.py
│   ├── spider_for_data.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

注：完整招聘数据及职业技能关联数据集保留在本地，不随公开仓库上传。

## 8. 环境配置与运行说明

### 8.1 环境要求

- Python 3.x
- MySQL 8.0
- Ubuntu
- Docker
- Redash
- 相关 Python 第三方依赖

### 8.2 安装依赖

克隆项目后，在项目根目录执行：

```bash
pip install -r requirements.txt
```

### 8.3 配置环境变量

复制 `.env.example` 文件，并创建本地 `.env` 文件，根据实际运行环境填写数据库连接信息及必要的爬虫配置。

注意：`.env` 文件包含本地敏感配置，不应上传至 GitHub。

### 8.4 数据库配置

根据项目实际运行环境准备 MySQL 数据库，并配置对应的数据库连接信息。

### 8.5 数据运行

完成依赖安装、环境变量及数据库配置后，根据项目主程序和相关模块执行数据采集、清洗及存储流程。

## 9. 数据说明

本项目涉及第三方招聘平台的招聘信息，公开仓库不提供完整招聘数据集及职业技能关联数据文件。

相关数据主要用于个人学习与项目实践，使用者需要根据自身情况配置数据来源，并通过项目程序自行采集和处理数据。

## 10. 项目说明

本项目为个人独立实践项目，记录了从招聘信息采集到数据存储、处理及可视化分析的完整开发过程。

通过本项目，对 Python 网络数据采集、数据清洗、MySQL 数据库操作、Linux 环境配置、Docker 服务部署及数据可视化等技术进行了综合实践。

[def]: docs/images/dashboard.png