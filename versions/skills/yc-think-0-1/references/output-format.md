# Output Format

Use two formats:

1. turn format for normal interactive mode
2. final format when enough information exists

## Turn format

Use this in normal interactive execution.

### 1. 适配判断

- 是否适合六问法：
- 问题类型：
- 判断理由：
- 下一步：

If the answer is not fit, stop here after giving the simpler handling path.

### 2. 当前步骤

- 当前在第几步：
- 这一步为什么要做：

### 3. 暂定理解

- 我目前的理解：

If details are uncertain, clearly say this is provisional.

### 4. 回答方向

Give 2-4 directions when helpful.

Use concrete Chinese.

### 5. 请你回答

Ask one concrete next question.

Then stop and wait.

## Final format

Only use the full final format when:

- the user asked for a draft
- or enough interaction has happened to ground the result

### 1. 适配判断

- 是否适合六问法：
- 问题类型：
- 判断理由：
- 下一步：

### 2. 原始问题

- 原始表述：

### 3. 支撑层

- 可能领域：
- 使用框架：
- 为什么用这个框架：

### 4. 轮次过程

For each round, include:

#### 第 N 轮

- 第1问 目标是什么：
- 第2问 现状是什么：
- 第3问 差距是什么：
- 第4问 目标背后的目的是什么：
- 第4问 0.5Why 验证：
- 第5问 导致现状的原因是什么：
- 第5问 0.5Why 验证：
- 第6问 差距真正的原因是什么：

#### 是否重开

- 是否需要重开：
- 如果需要，为什么：
- 新问题是什么：

### 5. 最终结果

- 真正的问题：
- 限制因素：
- 可改变因素：
- 初步行动方向：

### 6. 教练说明

Keep this short.

Include:

- 为什么这次关键判断重要
- 用户下次可以复用什么
- 还有什么不确定

## Style notes

- 默认中文
- 默认互动
- 不要在信息很少时直接写出完整终局分析
- 不要把暂定推断写成既定事实
