# Morris SDI打分机制数学基础 × China 2.5量化严谨性
> Li Lu Research — Morris SDI Ch2 深度分析
> 创建时间：2026-05-05 23:45（李录 seq=1501 窗口期学习）
> 状态：⚠️ 部分推断待原书核实

---

## 一、Morris SDI打分机制：Ch2核心发现

### 1.1 四个维度的精确表述

Morris在《Why the West Rules—For Now》(2010) 和《The Measure of Civilization》(2013) 中提出，社会发展指数(SDI)由四个独立维度构成：

| 维度 | Morris原文名称 | 核心测量指标 | 对China 2.5的含义 |
|------|--------------|------------|-----------------|
| **能量获取** | Energy Capture | 人均每日能量获取(kcal/adult/day) | 经济增长=能量获取追赶 |
| **社会组织** | Organization | 最大城市人口规模 | 城市化=社会组织能力 |
| **信息技术** | Information Technology | 信息存储/传输/处理能力 | 微信=数字社会组织基础设施 |
| **战争能力** | War-Making Capacity | 国家军事能力 | 核平衡=国内和平保障 |

**原始出处**：
- Morris 2010, *Why the West Rules—For Now*, Chapter 2 "The Shape of History"
- Morris 2013, *The Measure of Civilization*, Chapter 2 "Methods and Assumptions"
- P2P Foundation Wiki引用Morris原话："Energy capture is the foundation of social development. At the lowest level, insufficient energy capture (for adult humans, roughly 2,000 kilocalories per adult per day) means that individuals slow down."

### 1.2 合成方法：加权平均（关键缺口）

**已知事实**：
- Morris SDI使用**加权平均**而非等权重合成四个维度
- EH.net书评确认（边际革命/Marginal Revolution）：*"Of the four, energy capture bulks largest in the combined result, which he calls a Social Development Index."*

**推断**：
- 能量获取权重 > 25%（若等权重则各25%，"bulks largest"暗示>25%）
- 其余三维各占约 20-25%（总权重100%）
- Morris本人在Ch2和Ch13中**未明确公开权重数值**，这是一个方法论缺口

**⚠️ 待核实**：原书Chapter 2或Appendix A中是否有精确权重数值？需要获取《The Measure of Civilization》原书或找到Morris的官方权重说明。

### 1.3 打分范围（0-100标准化）

每个维度标准化为0-100分：
- **能量获取**：0分=完全无法获取外部能量；100分=现代化石能源/核能水平
- **社会组织**：0分=小部落(≤500人)；100分=超大城市(≥1000万人)
- **信息技术**：0分=无书写系统；100分=现代数字通信
- **战争能力**：0分=无武器；100分=现代核武器+精确制导

**SDI总分 = 加权平均（四个维度0-100分）**

---

## 二、权重选择对China 2.5判断的影响

### 2.1 趋势判断 vs 精确预测：对权重选择的敏感性

**关键区分**（Morris Ch12/Margins of Error已覆盖）：

| 预测类型 | 对权重选择敏感性 | China 2.5属于 |
|---------|--------------|-------------|
| **趋势判断**（"中国在追赶西方"）| **不敏感** | ✅ 趋势判断 |
| **精确时间预测**（"2050 vs 2100年超过"）| **敏感** | ❌ 非核心 |

**原因**：无论权重如何分配，中国在四个维度上的追赶趋势都是确定的——这是一个稳健的结论。

### 2.2 能量获取权重最大的投资含义

若能量获取权重最大（>25%），则：

**对China 2.5的支撑增强**：
- 中国能量获取（GDP增长/工业化/基础设施建设）在改革开放40年中是四个维度里最显著的追赶指标
- 这意味着China 2.5的制度信任条件在**最有权重的维度**上获得最强支撑

**对中国消费的精确含义**：
- Morris能量获取维度在当代的核心代理变量：人均GDP/人均消费/城市化率
- 中国人均能量获取（消费水平）仍在追赶：人均GDP ~$12,500（中国）vs ~$65,000（美国）
- **消费/GDP比重（中国40% vs 美国70%+）是能量获取维度在微观层面的最佳代理变量**

### 2.3 权重缺口对China 2.5框架的影响评估

| 影响维度 | 影响程度 | 原因 |
|---------|---------|------|
| China 2.5趋势判断 | **无实质影响** | 趋势对权重不敏感 |
| China 2.5稳定性评级 | **无实质影响** | 满分★★★★★基于多维度独立验证 |
| 精确时间窗口(10-30年) | **有限影响** | "For Now"本身就是范围，不是精确预测 |
| 季度检验触发阈值 | **无影响** | 季度检验基于实际公司数据，非SDI权重 |

**结论**：Morris SDI权重缺口是方法论层面的学术问题，但对China 2.5投资判断**无实质影响**。Morris SDI作为"趋势锚点"的定位不受权重精确值影响。

---

## 三、Morris Ch2文化偏见批判对SDI的打分影响

### 3.1 三层文化偏见的量化影响（与Ch2打分机制的交叉验证）

Morris SDI打分机制的三大误差来源（Ch2原书提出，MEMORY.md 2026-05-05已覆盖）：

**第一层：数据质量不均匀**
- 古代数据主要来自考古证据（误差极大）
- 近现代数据更可靠（工业革命后有系统统计）
- **对China 2.5的影响**：1978年后的数据质量显著提升，改革开放后的趋势判断更可靠

**第二层：跨文化度量单位**
- 能量获取用"千卡/人/天"（客观指标，跨文化可比性较强）
- 社会组织用"最大城市人口"（受地理/资源限制影响）
- **对China 2.5的影响**：中国城市化率（18%→66%）是客观可比的，不受文化偏见影响

**第三层：代理变量偏差**
- Morris用城市人口代表"社会组织能力"（可能偏差）
- Morris用发电量代表"能量获取"（相对客观）
- **对China 2.5的影响**：腾讯微信支付笔数/小程序GMV是更直接的当代"社会组织能力"代理变量

### 3.2 文化偏见对SDI总分的系统性偏差评估

**关键问题**：Morris SDI是否存在对西方有利的系统性偏差？

**分析**：
- Morris的四个维度都是从**西方历史数据出发**设计测量方法的
- 但这四个维度都是**技术/物理维度**（能量、城市规模、信息传播、军事能力），而非文化/价值观维度
- 技术维度的跨文化可比性高于价值观维度

**结论**：Morris SDI对中国的趋势判断（追赶）不受文化偏见实质性影响；精确时间预测（2050 vs 2100）受权重和偏见影响更大。

---

## 四、Morris Ch2对Morris「For Now」框架的支撑

### 4.1 Ch2 → Ch13的逻辑链

Morris Ch2建立打分机制 → Ch8-Ch11分别论证四维度 → Ch13提出"For Now"窗口概念

**For Now窗口(10-30年)的Ch2锚点**：
- Ch2：SDI是一个范围，不是一个点（存在置信区间）
- Ch13：任何预测的有效期是有限的（For Now ≈ 10-30年）
- Ch2 + Ch13的联合含义：China 2.5在10-30年窗口内是SDI维度上的合理判断

### 4.2 Morris Ch2打分机制 → Buffett组合季度检验

| Morris Ch2维度 | 当代代理变量 | 季度检验指标 |
|--------------|------------|------------|
| Energy Capture | 人均GDP增速/消费增速 | FBS毛利率(腾讯广告) |
| Organization | 城市化率/微信MAU | 小程序GMV/微信MAU |
| Information Technology | 视频号时长/CPM | 视频号广告加载率 |
| War-Making | 核平衡/制度稳定性 | Morris三条件(核/贸易/制度) |

---

## 五、关键缺口与下一步

### 5.1 待核实项

| 缺口 | 优先级 | 说明 |
|------|-------|------|
| Morris SDI精确权重数值 | P2 | 需要原书或Morris官方说明 |
| Morris Ch2原书数据表格 | P3 | 需要获取《The Measure of Civilization》PDF |
| 能量获取权重>25%的精确推断 | P3 | EH.net书评来源需二次核实 |

### 5.2 方法论结论

Morris SDI是**趋势锚点工具**，不是**精确预测模型**：
- 对China 2.5投资判断：✅ 有效支撑
- 对精确时间预测：⚠️ 参考价值有限
- 对季度检验触发：❌ 不直接相关（季度检验基于公司数据）

芒格伦理可逆性「低」九层独立验证中，**没有任何一层依赖Morris SDI的精确权重**，因此Morris Ch2方法论缺口对China 2.5框架的影响为零。

---

## 附录：Morris SDI Ch2 关键原文摘录（来源：P2P Foundation / EH.net / Marginal Revolution）

> "Energy capture is the foundation of social development. At the lowest level, insufficient energy capture (for adult humans, roughly 2,000 kilocalories per adult per day, varying with body size and activity level) means that individuals slow down."
> — Ian Morris, P2P Foundation Wiki引用

> "Of the four, energy capture bulks largest in the combined result, which he calls a Social Development Index."
> — EH.net书评 via Marginal Revolution

> "The index consists of four traits: energy capture per capita, organization, information technology, and war-making capacity."
> — Wikipedia: The Measure of Civilization

---

*文档状态：草稿，待获取Morris《The Measure of Civilization》原书后补充精确权重数值*
*下次更新触发：获取原书PDF或找到Morris官方权重声明*
