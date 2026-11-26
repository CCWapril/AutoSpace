---
title: 论文笔记-Scaling Up
category: Scaling Up
source: https://iwiki.woa.com/p/4017698622
generated: 2026-11-25
paper_count: 28
---

# Scaling Up论文笔记

> 字段说明：英文标题与 arXiv 日期由 arXiv API 核验；中文标题为整理译名；机构以原页面为主，补充检索时已标注。结构图沿用原 iWiki 附件，需要相应内网权限。

## MTFM

- **中文标题**：MTFM：美团可扩展、免对齐的工业推荐基础模型
- **English Title**：MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan
- **机构**：美团
- **时间**：2026-02-11
- **论文链接**：[arXiv:2602.11235](https://arxiv.org/abs/2602.11235)
- **分类**：推荐系统 / Scaling Up
- **说明笔记**：以 H/R/T/U/C 等异构 token 表示历史、实时、场景、用户和交叉特征；HAT 结合 full attention 与 target attention，target attention 使用 GQA 和时序动态 mask。
- **可参考性**：target attention 配合动态 mask 的时序感知可用于序列建模；训练/推理还包括动态 mask 算子、结构化剪枝、稀疏计算跳过和 BF16。

### 结构图

![MTFM结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=41630969)

![MTFM结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44060115)

---

## CADET

- **中文标题**：CADET：使用 Decoder-Only Transformer 进行上下文条件广告 CTR 预测
- **English Title**：CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **机构**：LinkedIn
- **时间**：2026-02-11
- **论文链接**：[arXiv:2602.11410](https://arxiv.org/abs/2602.11410)
- **分类**：推荐系统 / Scaling Up
- **说明笔记**：多塔上下文条件解码对应不同广告位；自门控 MHA 包含表示层自门控与 Q-K 交互门控，并结合时间戳 RoPE、会话延迟 mask、上下文/辅助/成对排序损失。
- **可参考性**：基于时间序列的 attention 优化，原页面判断暂无法直接借鉴。
- **发表信息（arXiv 元数据）**：Accepted at AdKDD 2026. 7 pages

### 结构图

![CADET结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=43040418)

![CADET结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=43040433)

![CADET结构图3](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44065034)

![CADET结构图4](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44065043)

---

## OneLive

- **中文标题**：OneLive：动态统一的直播推荐生成式框架
- **English Title**：OneLive: Dynamically Unified Generative Framework for Live-Streaming Recommendation
- **机构**：快手
- **时间**：2026-02-09
- **论文链接**：[arXiv:2602.08612](https://arxiv.org/abs/2602.08612)
- **分类**：推荐系统 / Scaling Up
- **说明笔记**：针对级联目标不一致和算力利用率低，以动态语义 SID/残差量化处理内容生命周期，Decoder-Only 结合时间序列与 QK 归一化，多目标通过奖励模型、DPO/GRPO 对齐。
- **可参考性**：动态 tokenization、decoder 时间建模和多目标奖励/优化是直播生成式推荐的三项核心挑战。
- **发表信息（arXiv 元数据）**：Work in progress

### 结构图

![OneLive结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=62127219)

![OneLive结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=62127116)

---

## EST

- **中文标题**：EST：通过统一建模实现 CTR 预测的高效 Scaling Law
- **English Title**：EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **机构**：阿里巴巴
- **时间**：2026-02-11
- **论文链接**：[arXiv:2602.10811](https://arxiv.org/abs/2602.10811)
- **分类**：Scaling Up
- **说明笔记**：核心观点是内容信号更适合作为关系先验指导 ID 空间交互，而非直接作为 token 嵌入。LCA 以非行为特征为 Q、行为为 K/V；CSA 根据序列内内容相似度选 Top-N 交互。
- **可参考性**：序列与 context 直接输入容易交互不足，可参考 CSA 的相似度 Top-N；但相似矩阵需与其他特征处理并行，并评估存储和维护成本。
- **发表信息（arXiv 元数据）**：Accepted by KDD2026

### 结构图

![EST结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=43974551)

---

## MLCC

- **中文标题**：压缩、交叉与扩展：推荐系统高效扩展的多层压缩交叉网络
- **English Title**：Compress, Cross and Scale: Multi-Level Compression Cross Networks for Efficient Scaling in Recommender Systems
- **机构**：哔哩哔哩广告
- **时间**：2026-02-12
- **论文链接**：[arXiv:2602.12041](https://arxiv.org/abs/2602.12041)
- **分类**：Scaling Up
- **说明笔记**：GC 全局压缩与 LC 局部压缩降低特征表示成本，PLC（Progressive Layered Crossing）以多层次乘加模拟高阶非线性，缓解复杂度和 embedding 维度扩展成本。
- **可参考性**：压缩思想可用于 tokenization，PLC 的多层次乘加非线性也可参考。
- **发表信息（arXiv 元数据）**：11 pages, 3 figures

### 结构图

![MLCC结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44065464)

![MLCC结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44065445)

---

## MixFormer

- **中文标题**：MixFormer：工业推荐中 Dense 与 Sequence 的协同扩展
- **English Title**：MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders
- **机构**：字节跳动
- **时间**：2026-02-15
- **论文链接**：[arXiv:2602.14110](https://arxiv.org/abs/2602.14110)
- **分类**：Scaling Up
- **说明笔记**：Query Mixer 以 HeadMixing + Per-head SwiGLU FFN 替代 self-attention；Cross Attention 聚合序列；Output Fusion 以 Per-head SwiGLU FFN 替代标准 FFN，统一序列与特征交互。
- **可参考性**：原页面记录：可尝试，视频号 pCVR 正在 5% 实验。
- **发表信息（arXiv 元数据）**：Accepted by KDD 2026

### 结构图

![MixFormer结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44066678)

---

## MDL

- **中文标题**：MDL：通过 Tokenization 实现大规模工业推荐的统一多分布学习器
- **English Title**：MDL: A Unified Multi-Distribution Learner in Large-scale Industrial Recommendation through Tokenization
- **机构**：字节跳动
- **时间**：2026-02-07
- **论文链接**：[arXiv:2602.07520](https://arxiv.org/abs/2602.07520)
- **分类**：Scaling Up
- **说明笔记**：将 RankMixer 扩展为多场景多任务：引入场景/任务 token，基础 token 经 RankMixer 后与场景 token 做 attention，再与 task token pooling 结合。
- **可参考性**：多场景多任务建模，可直接对照 scenario/global token 与 task pooling 设计。
- **发表信息（arXiv 元数据）**：9 pages, 4 figures

### 结构图

![MDL结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=79559626)

---

## SORT

- **中文标题**：SORT：系统化优化的工业规模推荐排序 Transformer
- **English Title**：SORT: A Systematically Optimized Ranking Transformer for Industrial-scale Recommenders
- **机构**：阿里巴巴（AliExpress）
- **时间**：2026-03-04
- **论文链接**：[arXiv:2603.03988](https://arxiv.org/abs/2603.03988)
- **分类**：Scaling Up
- **说明笔记**：针对稀疏特征与稀疏标签，特征侧 transfer&freeze 并加入 RoPE；Block 采用 MHA + Sparse MoE，MHA 使用 RoPE 和 OneTrans 式查询剪枝。
- **可参考性**：MHA + Sparse MoE 结构可借鉴，剪枝需进一步验证可行性。
- **发表信息（arXiv 元数据）**：CIKM'26

### 结构图

![SORT结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44085169)

---

## OCP

- **中文标题**：OCP：工业商品推荐稀疏扩展的正交约束投影
- **English Title**：OCP: Orthogonal Constrained Projection for Sparse Scaling in Industrial Commodity Recommendation
- **机构**：京东
- **时间**：2026-03-19
- **论文链接**：[arXiv:2603.18697](https://arxiv.org/abs/2603.18697)
- **分类**：Scaling Up
- **说明笔记**：正交约束投影层在前向中保持等距映射，反向传播保留奇异值谱特性与空间相关性，面向稀疏词表扩展和 embedding 维度坍塌。
- **可参考性**：可用于矩阵更新和防坍塌，但需配套更新机制，成本较高。
- **发表信息（arXiv 元数据）**：5 pages, 4 figures

### 结构图

![OCP结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44085246)

---

## UniScale

- **中文标题**：UniScale：搜索排序的全空间数据与模型协同扩展
- **English Title**：UniScale: Synergistic Entire Space Data and Model Scaling for Search Ranking
- **机构**：阿里巴巴
- **时间**：2026-03-25
- **论文链接**：[arXiv:2603.24226](https://arxiv.org/abs/2603.24226)
- **分类**：Scaling Up
- **说明笔记**：ES3 做全空间采样，HHSFT 融合搜索、推荐、购买异构数据；HHFI 包含 per-token HFA 与全局 GFA，ESUIF 通过 DREF 和 DAPGA 组合共享/特定专家、任务专家与 domain attention。
- **可参考性**：全空间建模暂难直接落地；先异构 per-token 再全局交互可参考，domain attention 可改造为 scene attention。
- **发表信息（arXiv 元数据）**：Accepted at CIKM 2026

### 结构图

![UniScale结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44067053)

---

## UniMixer

- **中文标题**：UniMixer：推荐系统 Scaling Law 的统一架构
- **English Title**：UniMixer: A Unified Architecture for Scaling Laws in Recommendation Systems
- **机构**：快手
- **时间**：2026-04-01
- **论文链接**：[arXiv:2604.00590](https://arxiv.org/abs/2604.00590)
- **分类**：Scaling Up
- **说明笔记**：UniMixing 学习对称、稀疏、随机且行列和为 1 的全局/局部混合矩阵，采用 Sinkhorn-Knopp；Lite 版低秩表示全局矩阵，并结合 Per-Token FFN 与 SiameseNorm。
- **可参考性**：在全局 transform 上增加少量可学习参数做交互，mixing 设计值得参考。

### 结构图

![UniMixer结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44067027)

---

## SSR

- **中文标题**：超越稠密连接：可扩展推荐的显式稀疏性
- **English Title**：Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation
- **机构**：阿里巴巴
- **时间**：2026-04-09
- **论文链接**：[arXiv:2604.08011](https://arxiv.org/abs/2604.08011)
- **分类**：Scaling Up
- **说明笔记**：Multi-View Sparse Filtering 包含静态 SSR-S 与动态 SSR-D，后者以 ICS 做输入相关动态筛选；Intra-View Dense Fusion 在视图内并行全连接融合。
- **可参考性**：稀疏过滤方法可借鉴。
- **发表信息（arXiv 元数据）**：Accepted as a full paper at SIGIR 2026. 11 pages, 6 figures

### 结构图

![SSR结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44085696)

![SSR结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=44095011)

---

## SparseCTR

- **中文标题**：释放稀疏注意力在 CTR 长期行为建模中的潜力
- **English Title**：Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction
- **机构**：美团
- **时间**：2026-01-25
- **论文链接**：[arXiv:2601.17836](https://arxiv.org/abs/2601.17836)
- **分类**：Scaling Up
- **说明笔记**：以 TimeChunking 做个性化时间感知切分，RelTemporal 编码相对时间，EvoAttention 稀疏化长期行为注意力，降低 Transformer 成本并减少随机采样信息损失。
- **发表信息（arXiv 元数据）**：WWW 2026: THE ACM WEB CONFERENCE

### 结构图

![SparseCTR结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=45780311)

---

## RankUp

- **中文标题**：RankUp：面向大规模广告推荐系统的高秩表示
- **English Title**：RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **机构**：腾讯
- **时间**：2026-04-20
- **论文链接**：[arXiv:2604.17878](https://arxiv.org/abs/2604.17878)
- **分类**：Scaling Up
- **说明笔记**：针对维度坍塌和有效秩不足，组合随机排列分割、多嵌入表示、全局 token、预训练嵌入与任务 token。
- **可参考性**：重点参考随机排列分割及其对有效秩的影响。
- **发表信息（arXiv 元数据）**：9 pages, 5 figures

### 结构图

![RankUp结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=45780302)

---

## RankElastor

- **中文标题**：更多扩展、更少收缩：塑造推荐 Dense Scaling 的有效秩动态
- **English Title**：Expand More, Shrink Less: Shaping Effective-Rank Dynamics for Dense Scaling in Recommendation
- **机构**：腾讯
- **时间**：2026-05-22
- **论文链接**：[arXiv:2605.23191](https://arxiv.org/abs/2605.23191)
- **分类**：Scaling Up
- **说明笔记**：分析 RankMixer 的阻尼振荡：块转置只带来有限秩扩展，PFFN 可能导致秩收缩；通过参数化 mixing 与 GLU-PFFN 增强扩展并减少收缩。
- **可参考性**：适合与 RankMixer/RankUp 的有效秩曲线联合分析。
- **发表信息（arXiv 元数据）**：Accepted at the 32st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (Research Track), KDD 2026 February Cycle

### 结构图

![RankElastor结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=45770001)

---

## HeMix

- **中文标题**：HeMix：通过异质 Token 混合扩展工业排序模型
- **English Title**：HeMix: Scaling Industrial Ranking Models with Heterogeneous Token Mixing
- **机构**：阿里巴巴
- **时间**：2026-02-10
- **论文链接**：[arXiv:2602.09387](https://arxiv.org/abs/2602.09387)
- **分类**：Scaling Up
- **说明笔记**：输入包含 user/item/cross/实时/历史序列，统一 MLP→split tokenization；Query-Mixed 对全局与实时序列采用 mixed heterogeneous attention。
- **可参考性**：Cross-attention 设计可参考。

### 结构图

![HeMix结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=46379062)

---

## LUM

- **中文标题**：基于三步范式大型用户模型释放工业推荐 Scaling Law
- **English Title**：Unlocking Scaling Law in Industrial Recommendation Systems with a Three-step Paradigm based Large User Model
- **机构**：阿里巴巴
- **时间**：2025-02-12
- **论文链接**：[arXiv:2502.08309](https://arxiv.org/abs/2502.08309)
- **分类**：Scaling Up
- **说明笔记**：围绕知识构建、查询与利用，tokenization 后由 token/user encoder 学习用户表示，以 InfoNCE 训练，输出特征服务于排序和召回。
- **可参考性**：InfoNCE 损失及用户表示向多任务复用的方式可参考。
- **发表信息（arXiv 元数据）**：WSDM 2026, 10 pages; The first three authors contributed equally to this work

### 结构图

![LUM结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=61161118)

---

## OneRank

- **中文标题**：OneRank：多任务推荐的统一 Transformer 原生排序架构
- **English Title**：OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation
- **机构**：中国人民大学
- **时间**：2026-06-15
- **论文链接**：[arXiv:2606.16838](https://arxiv.org/abs/2606.16838)
- **分类**：Scaling Up
- **说明笔记**：行为序列、检索偏好与任务统一 tokenization；task-specific encoding 用 mask 隔离任务 token，候选感知模块以任务上下文为 Q；多任务预测采用梯度分离，损失结合 InfoNCE 与 BCE。
- **可参考性**：重点关注注意力掩码与反向算子阻断的梯度分离。
- **发表信息（arXiv 元数据）**：KDD 2026 Accepted

### 结构图

![OneRank结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=62126897)

---

## CCFormer

- **中文标题**：CCFormer：腾讯工业推荐的高效跨字段交互与分层序列压缩
- **English Title**：CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent
- **机构**：腾讯
- **时间**：2026-07-30
- **论文链接**：[arXiv:2607.28070](https://arxiv.org/abs/2607.28070)
- **分类**：Scaling Up
- **说明笔记**：字段分离注意力分别处理序列—user 及序列/user—item 的 dual attention；长序列 token 重排再混合，并隔层使用 Conv1D 分层压缩，保留细粒度行为信号。
- **可参考性**：可参考 token mixer 的重排再混合及 Conv1D 序列压缩。

### 结构图

![CCFormer结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=75781508)

---

## UniCon

- **中文标题**：UniCon：统一的上下文中心 CTR 预测建模范式
- **English Title**：UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction
- **机构**：美团
- **时间**：2026-09-03
- **论文链接**：[arXiv:2609.03290](https://arxiv.org/abs/2609.03290)
- **分类**：Scaling Up
- **说明笔记**：以 Context Unit 组织 items、user、context 和曝光位置三头，避免简单序列/非序列二分丢失上下文边界；分层执行 intra/inter 上下文交互，预测侧使用 MMoE。
- **可参考性**：重点关注 intra 与 inter 的序列交互。
- **发表信息（arXiv 元数据）**：10 pages, 5 figures, 2 tables

### 结构图

![UniCon结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=75781538)

---

## OneModel

- **中文标题**：OneModel：平台级多场景排序的统一基础模型
- **English Title**：OneModel: A Unified Foundation for Platform-Scale Multi-Scenario Ranking
- **机构**：小红书
- **时间**：2026-08-19
- **论文链接**：[arXiv:2608.18606](https://arxiv.org/abs/2608.18606)
- **分类**：Scaling Up
- **说明笔记**：item 与 context 相加形成跨场景统一表示，分层长序列采用 attention + FFN；SAIM 通过 scene gate 做场景感知信息调制，并端到端优化多目标损失。
- **可参考性**：SAIM 场景门控可用于多场景建模对照。

### 结构图

![OneModel结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=76468727)

![OneModel结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=76468951)

---

## SetMIR

- **中文标题**：SetMIR：多兴趣检索即集合预测
- **English Title**：SetMIR: Multi-Interest Retrieval as Set Prediction
- **机构**：Snapchat
- **时间**：2026-08-31
- **论文链接**：[arXiv:2608.30251](https://arxiv.org/abs/2608.30251)
- **分类**：Scaling Up
- **说明笔记**：以集合预测缓解 argmax 分配导致的兴趣坍缩和固定 K 查询的静态分发；损失包括 InfoNCE、presence BCE 与 Margin Diversity，后者惩罚活跃 query 间余弦冗余。

### 结构图

![SetMIR结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=76473695)

---

## MI-DPG

- **中文标题**：MI-DPG：基于互信息的可分解参数生成网络用于多场景推荐
- **English Title**：MI-DPG: Decomposable Parameter Generation Network Based on Mutual Information for Multi-Scenario Recommendation
- **机构**：蚂蚁集团
- **时间**：2026-03-22
- **论文链接**：[arXiv:2603.21209](https://arxiv.org/abs/2603.21209)
- **分类**：Scaling Up
- **说明笔记**：DWM 对权重矩阵本身做分解而非直接低秩分解骨干层；MIR 通过 shuffle 构造跨场景负样本并加互信息正则，联合交叉熵优化。
- **可参考性**：需进一步验证 shuffle 构造负样本的语义合理性。
- **发表信息（arXiv 元数据）**：Proc. 32nd ACM Intl. Conf. on Information and Knowledge Management (CIKM 2023), pp. 3803-3807

### 结构图

![MI-DPG结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=76475830)

---

## UniFormer

- **中文标题**：UniFormer：高效统一的模型中心工业推荐扩展
- **English Title**：UniFormer: Efficient and Unified Model-Centric Scaling for Industrial Recommendation
- **机构**：快手
- **时间**：2026-06-25
- **论文链接**：[arXiv:2606.27058](https://arxiv.org/abs/2606.27058)
- **分类**：Scaling Up
- **说明笔记**：统一序列、非序列与任务 token；FIM 结合 cross-attn、s-FFN、self-attn、ns-FFN 完成序列/非序列交叉，TIM 结合 cross-attn、self-attn、FFN 建模表示与任务信号。
- **可参考性**：attention 与 FFN 的组合方式可参考。

### 结构图

![UniFormer结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=79638341)

---

## HiRank

- **中文标题**：通过有效秩扩展实现推荐系统的统一异构特征交互
- **English Title**：Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender Systems
- **机构**：阿里巴巴淘宝
- **时间**：2026-10-26
- **论文链接**：[arXiv:2610.35318](https://arxiv.org/abs/2610.35318)
- **分类**：Scaling Up
- **说明笔记**：门控序列建模在层间迭代执行特征交互→行为记忆检索→再交互；主序列用 SiLU attention，候选状态生成互补记忆查询；异构 token 采用 head-wise mixing，场景感知聚合在高秩注意力输出上完成。
- **可参考性**：序列状态保留与门控，以及场景调制压缩信息的 high-rank attention 值得参考。
- **发表信息（arXiv 元数据）**：10 pages, 4 figures

### 结构图

![HiRank结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=79661132)

---

## UGR

- **中文标题**：UGR：异构电商推荐的统一生成式排序
- **English Title**：UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation
- **机构**：阿里巴巴淘宝
- **时间**：2026-10-29
- **论文链接**：[arXiv:2610.39426](https://arxiv.org/abs/2610.39426)
- **分类**：Scaling Up
- **说明笔记**：Generator 包含 context encoder、分业务 candidate encoding 与 auto decoder；离线结合广告去偏塔、NTP、WSFT、PermPO，在线结合广告价值与多价值序列检索，并兼容 GSP 拍卖。
- **可参考性**：生成式推荐中的广告去偏塔可考虑。

### 结构图

![UGR结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=81357725)

![UGR结构图2](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=84933474)

---

## HubMixer

- **中文标题**：HubMixer：推荐中参数高效特征交互的渐进潜在枢纽混合
- **English Title**：HubMixer: Progressive Latent Hub Mixing for Parameter-Efficient Feature Interaction in Recommendation
- **机构**：快手
- **时间**：2026-08-28
- **论文链接**：[arXiv:2608.27991](https://arxiv.org/abs/2608.27991)
- **分类**：Scaling Up
- **说明笔记**：两层 MLP 生成可学习 hubs，hub induction 以 hubs 为 Q 读取原始 token，hub interaction 做 self-attn，readout 再以原始 token 为 Q 读回，降低异构 token 全交互成本。
- **可参考性**：Q/K/V 角色在 induction 与 readout 间转换的设计可参考。

### 结构图

![HubMixer结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=84933873)

---

## DNA

- **中文标题**：DNA：释放 CTR 模型的深度扩展能力
- **English Title**：DNA: Unlocking Depth Scaling in CTR Models
- **机构**：阿里巴巴
- **时间**：2026-11-19
- **论文链接**：[arXiv:2611.25659](https://arxiv.org/abs/2611.25659)
- **分类**：Scaling Up
- **说明笔记**：Dual-stream Nexus Attention 同时更新请求/候选流 F、U 与行为流 S：Read Block 让 F/U 读取 S，Update Block 再让 S 读取更新后的 U，避免多层 cross-attn 反复读取固定行为序列而收益饱和。
- **可参考性**：行为序列随层深度更新的机制可直接用于序列建模对照实验。
- **发表信息（arXiv 元数据）**：10 pages, 5 figures

### 结构图

![DNA结构图1](https://iwiki.woa.com/tencent/api/attachments/s3/url?attachmentid=84473017)

---
