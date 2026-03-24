# 六问法 Skill 设计分析

## 1. 任务目标

本文档用于回答 4 个问题：

1. Claude Code 最新 `skill-creator` skill 的关键点是什么
2. 社区里关于创建 skill 的最佳实践有哪些值得采用
3. “界定问题六问法”是否适合做成一个 skill
4. 如果适合，应该怎么设计、怎么制作、怎么验证

## 2. 已完成的研究动作

### 2.1 本地与下载的 skill-creator 对照

已完成：

- 阅读本地系统自带的 `skill-creator`
- 通过 `skill-installer` 从 `anthropics/skills` 下载最新 `skill-creator`
- 对照两者的 `SKILL.md` 和目录结构

下载位置：

- 本轮研究时下载到了本地 `research/skill-creator` 目录，但该研究目录未纳入当前仓库。

结论：

- 最新官方版明显比本地系统版更强调“评测驱动”
- 它不只是教你写 `SKILL.md`，还强调：
  - 先定义测试 prompt
  - 做 with-skill / baseline 对照
  - 同时评估 qualitative + quantitative 结果
  - 迭代 skill description 以改善触发率

这对设计“六问法教练”非常重要，因为这个 skill 的核心价值不只是“写出来”，而是“真的能稳定带用户把问题界定清楚”。

### 2.2 参考的官方与社区资料

官方资料：

- Anthropic PDF: The Complete Guide to Building Skills for Claude
- Claude Blog: How to create Skills: Key steps, limitations, and examples
- Claude Docs: Creating custom skills
- Claude Docs: Skill authoring best practices
- 官方 `anthropics/skills` 仓库中的最新 `skill-creator`

社区资料：

- `skills.sh` 上的 `skill-builder` 社区 skill 页面

说明：

- 官方资料适合拿来做“硬约束”和默认做法
- 社区资料适合拿来参考补充经验，但不应无条件照搬

## 3. 创建 Skill 的关键点

结合官方 `skill-creator`、官方文档和社区经验，做 skill 时最关键的是下面这些点。

### 3.1 先想清楚 use case，不要先写说明书

最重要的不是马上写 `SKILL.md`，而是先定义：

- 这个 skill 到底解决什么重复性问题
- 用户会怎么表达这类需求
- 成功输出长什么样
- 哪些边界不应该触发这个 skill

如果这一步没做好，后面的文档写得再漂亮，skill 也会：

- 触发不准
- 使用范围漂移
- 输出不稳定

### 3.2 description 是触发核心

官方资料对这一点非常一致：

- `name` 和 `description` 是决定触发的核心元数据
- 尤其是 `description`，必须同时写清：
  - skill 做什么
  - 什么时候应该使用

经验上要避免：

- 描述过短，触发不到
- 描述太抽象，边界模糊
- 只写能力，不写触发语境

### 3.3 skill 要解决真实工作流，而不是抽象概念

优秀的 skill 一般都满足：

- 是一个多步骤工作流
- 经常重复发生
- 有比较固定的流程骨架
- 需要领域知识或最佳实践支撑

“六问法教练”满足这几个条件，所以从类型上看是适合做 skill 的。

### 3.4 progressive disclosure 很重要

官方最佳实践反复强调：

- `SKILL.md` 保持精炼
- 细节拆到 `references/`
- 脚本放到 `scripts/`
- 模板放到 `assets/`

原因是：

- 触发时只加载必要内容
- 降低上下文占用
- 更容易维护

### 3.5 优先做 workflow，而不是堆概念

skill 最有价值的部分是：

- 顺序化步骤
- 判断分支
- 输出模板
- 校验机制

不是百科式知识堆积。

### 3.6 最好先用单一任务跑通，再扩展

官方 PDF 和最佳实践都强调：

- 先拿 1 个典型任务跑通
- 先看 skill 是否真能改善结果
- 然后再扩展更多 use case

这意味着“六问法教练”不应该一开始就试图覆盖所有人生问题、管理问题、战略问题，而应先聚焦：

- 差距不明确的行动类问题

### 3.7 要做真实评测，而不是只凭主观感觉

最新官方 `skill-creator` 的最大价值之一，就是把迭代流程变成：

1. 写 skill
2. 写测试 prompt
3. 跑 with-skill / baseline
4. 看 qualitative + quantitative 结果
5. 改 skill
6. 再跑

这对六问法 skill 也非常适用。

## 4. 社区最佳实践里值得吸收的部分

社区资料里有些观点是有用的，但要有选择地吸收。

### 4.1 值得采用的部分

- 文件名要意图清晰，不要叫 `reference.md`、`utils.md` 这种模糊名字
- skill 要明确自己的边界和默认工作流
- 要把常见错误和测试方式写进设计里
- 要优先考虑触发准确性，而不是只考虑内容完整性

### 4.2 不应机械照搬的部分

有些社区 skill 会给出比较强的偏好，例如：

- 强推 Node.js
- 强推 gerund 风格命名
- 强推某种固定文件结构

这些可以参考，但不属于必须遵守的官方硬约束。

对我们这个项目来说，更重要的是：

- skill 是否容易触发
- workflow 是否稳定
- 输出是否真的能帮用户把问题界定清楚

## 5. 六问法是否适合做成 Skill

结论：

**适合，而且很适合。**

原因如下。

### 5.1 它是标准的重复型工作流

六问法天然就是一个结构化流程：

1. 明确目标
2. 明确现状
3. 明确差距
4. 追问目标背后的目的
5. 分析导致现状的原因
6. 汇总并重新界定真正问题

这种流程非常适合写成 skill。

### 5.2 它需要稳定的思考顺序

普通用户最常见的问题不是“不会思考”，而是：

- 顺序乱
- 跳步
- 把方案当问题
- 把情绪当问题
- 第 4 问和第 5 问没有验证因果

skill 的价值就在于把顺序固定下来，并强制输出必要中间过程。

### 5.3 它特别适合“教练型 skill”

这个 skill 不是替用户直接下结论，而是像教练一样：

- 帮用户一步步澄清问题
- 在关键点上追问
- 发现问题失效时重开
- 最终产出一个高质量问题定义

这类“教练型 skill”通常比“百科型 skill”更适合技能化。

### 5.4 它也适合叠加专业框架

你前面已经明确了一个关键原则：

- 六问法是方法框架
- 专业框架是增强层

这意味着这个 skill 可以做成“通用骨架 + 领域增强”的结构，而不是死板模板。

## 6. 但它不应该被做成什么样

为了避免做废，这个 skill 不应该被设计成下面几种样子。

### 6.1 不要做成纯知识说明书

如果 skill 只是解释：

- 六问法是什么
- 每一问是什么意思
- 有哪些注意事项

那它更像一篇教程，不像一个 skill。

### 6.2 不要做成“万能人生导师”

如果 description 写得太泛，就会过度触发，最后变成：

- 什么问题都想接
- 但什么问题都分析不深

所以它的边界必须清楚：

- 优先处理差距不明确的行动类问题

### 6.3 不要忽略多轮重开机制

六问法 skill 最大的独特点之一，是：

- 第 3 问可能发现原问题不成立
- 第 4 问可能发现原目标只是初步解决方案
- 这时必须生成新问题并重开

如果没有这个机制，这个 skill 的价值会打很大折扣。

### 6.4 不要忽略专业支撑

如果 skill 只会机械问六问，而不会：

- 先识别领域
- 提醒补专业框架
- 在第 1、2、5 问引入领域视角

那它只能做“形式上的六问法”，做不到高质量界定。

## 7. 推荐的 Skill 定位

我建议把它定位成：

**一个面向“差距不明确的行动类问题”的结构化问题界定教练。**

它的核心任务不是给方案，而是产出：

- 原始问题
- 每一轮六问法记录
- 是否重开及原因
- 最终真正问题
- 限制因素
- 可改变因素
- 初步对策方向

## 8. 推荐的 Skill 设计

## 8.1 Skill 类型

它属于官方分类中的：

- Workflow Automation skill

而不是单纯的 document skill。

## 8.2 建议的 skill 名称

按官方命名规则，skill folder/name 需要 kebab-case。

候选名：

- `clarifying-problems`
- `running-six-questions`
- `defining-real-problems`

如果强调方法来源，我更建议：

- `running-six-questions`

理由：

- 直观表达“执行六问法”
- 不会太泛
- 便于和其他问题分析 skill 区分

## 8.3 建议的 skill description 方向

description 需要同时写：

- 它做什么
- 什么时候使用

建议方向：

“Uses the six-question problem-definition method to turn vague, emotionally framed, or solution-disguised user problems into a clearly defined actionable problem. Use when users say they are unclear about the real problem, want to analyze a problem step by step, need root-cause-oriented problem definition, or describe action problems with unclear goals, current state, or gap.”

注意：

- 要覆盖“分析问题”“问题不清楚”“真正问题是什么”“一步步梳理问题”“把问题分析清楚”这类触发语境
- 要避免把 skill 写成“任何问题都可用”的过泛 description

## 8.4 建议的技能结构

建议第一版目录如下：

```text
running-six-questions/
├── SKILL.md
├── references/
│   ├── method-core.md
│   ├── domain-support.md
│   ├── restart-rules.md
│   ├── output-template.md
│   ├── anti-patterns.md
│   └── examples.md
└── scripts/
    └── validate_output.py
```

说明：

- `SKILL.md` 只保留触发、主流程、导航
- `method-core.md` 放六问法骨架
- `domain-support.md` 放“专业框架是增强层”的规则
- `restart-rules.md` 专门放第 3/4 问触发重开的条件
- `output-template.md` 放标准输出格式
- `anti-patterns.md` 放常见误区
- `examples.md` 放 2-3 个典型例子
- `validate_output.py` 可选，用于检查输出是否缺少关键段落

## 8.5 主流程应怎么设计

这个 skill 的主流程建议写成严格 workflow，而不是松散建议。

### Step 1. 判断是否适合使用六问法

先判断：

- 这是不是差距不明确的行动类问题
- 用户是在求解问题，还是只是在查事实
- 当前表达的是问题、情绪、判断，还是初步解决方案

如果不适合，就退出 skill 或只给简短说明。

### Step 2. 补“专业支撑”

进入六问法前，先补以下内容：

- 问题所属领域
- 目标常用拆解维度
- 现状常用观察维度
- 原因常用分析框架

如果用户给不出来，就：

- 用通用框架先分析
- 同时标记专业支撑不足

### Step 3. 执行第 1 问到第 3 问

要求 skill：

- 不得跳过
- 不得合并
- 目标、现状、差距必须同维度

### Step 4. 在第 4 问强制使用 0.5Why

标准句式：

- 【回答】就一定要【当前目标】吗？

目标：

- 判断原目标是否只是初步解决方案
- 判断是否出现了新目标

### Step 5. 在第 5 问强制使用框架 + 0.5Why

标准句式：

- 【原因】一定会导致【当前现状/问题】吗？

要求：

- 先发散原因
- 再分组
- 再验证
- 再下钻
- 再汇总

### Step 6. 在第 3 问或第 4 问需要时重开

这是 skill 的关键设计点。

必须显式输出：

- 原轮问题
- 为什么失效
- 新问题是什么
- 是否开启新一轮六问法

### Step 7. 输出最终结果

必须固定输出：

1. 原始问题
2. 轮次过程
3. 最终真正问题
4. 限制因素
5. 可改变因素
6. 初步对策方向

## 8.6 脚本是否需要

第一版不一定必须有复杂脚本。

因为这个 skill 的核心价值在于：

- workflow
- 判断逻辑
- 输出结构

但我建议至少准备一个轻量脚本：

- `validate_output.py`

它可以检查：

- 是否包含原始问题
- 是否包含每轮六问法
- 第 4 问和第 5 问是否出现 0.5Why 记录
- 是否包含重开记录
- 是否包含最终真正问题、限制因素、可改变因素

这样能提升稳定性。

## 9. 制作过程建议

结合官方 `skill-creator` 的最佳实践，这个 skill 的制作过程建议如下。

### 阶段 1：定义 use case

先固定 3 个代表性用例：

1. 个人拖延类问题
2. 团队效率类问题
3. 职场选择类问题

### 阶段 2：定义成功标准

至少定义这些成功标准：

- skill 能在相关请求上稳定触发
- 不相关请求不会乱触发
- 输出一定包含轮次过程
- 第 4 问和第 5 问不会跳过 0.5Why
- 遇到新目标时会重开
- 最终输出的问题定义可直接用于下一步方案设计

### 阶段 3：先写最小版 skill

最小版只需要：

- `SKILL.md`
- `references/method-core.md`
- `references/output-template.md`
- `references/restart-rules.md`

先把骨架跑通，再补其他文件。

### 阶段 4：准备评测集

建议至少准备：

- 8-12 个应触发 prompt
- 8-12 个不应触发 prompt
- 5 个完整功能测试 prompt

### 阶段 5：做 with-skill / baseline 对照

比较：

- 没有 skill 时，LLM 是否容易跳步
- 有 skill 时，是否更容易保留中间过程
- 是否更容易识别“原问题不是问题”
- 是否更容易输出结构化结果

### 阶段 6：迭代 description

如果触发不稳定，先改 description，不要急着改 body。

### 阶段 7：再迭代 body 和 references

如果触发正常，但执行过程仍不稳定，再改：

- workflow
- restart 规则
- 输出模板
- 反例说明

## 10. 这个 skill 的主要风险

### 风险 1：触发过泛

如果 description 写得过宽，它会在很多不该触发的场景触发。

解决方式：

- 明确“差距不明确的行动类问题”是适用边界

### 风险 2：触发过窄

如果 description 太保守，用户明明想梳理问题，skill 却触发不到。

解决方式：

- description 中显式写入常见用户表达

### 风险 3：输出变成空泛教学

如果 workflow 太松，skill 容易变成在解释六问法，而不是执行六问法。

解决方式：

- 强制结构化输出
- 把“解释”和“执行”分开

### 风险 4：忽略专业支撑

如果不补领域框架，分析质量会很虚。

解决方式：

- 把“专业支撑检查”放在主流程前面

### 风险 5：忘记重开

这是最关键的失败模式之一。

解决方式：

- 把第 3/4 问后的分流判断写成显式步骤
- 输出中必须保留“是否重开”

## 11. 最终判断

综合判断如下：

### 11.1 是否值得做成 skill

值得。

### 11.2 适合做成什么类型的 skill

适合做成：

- 结构化问题界定教练
- workflow automation skill

### 11.3 第一版最重要的设计原则

第一版应坚持：

1. 聚焦差距不明确的行动类问题
2. 第 4 问和第 5 问强制使用 0.5Why
3. 第 3 问和第 4 问支持多轮重开
4. 明确加入专业支撑层
5. 固定结构化输出
6. 先跑评测，再扩展能力边界

### 11.4 推荐做法

推荐先做 MVP：

- 一个可触发的 skill
- 一个稳定 workflow
- 一个结构化输出模板
- 一个轻量校验脚本
- 一组基础评测用例

先验证它真的比“没有 skill 时直接问模型”更稳定，再继续扩展。

## 12. 下一步建议

如果继续推进，最合理的下一步是：

1. 先确定最终 skill 名称
2. 基于当前文档初始化 skill 目录
3. 写出第一版 `SKILL.md`
4. 写 8-12 个触发/不触发测试 prompt
5. 跑第一轮 with-skill / baseline
6. 迭代 description 和 workflow

## 13. 参考来源

本地材料：

- [界定问题六问法.md](../method/界定问题六问法.md)
- `skill-creator` 的本地参考稿来自临时研究目录，未随仓库提交；如需重新核对，请在新环境再次安装官方 `skill-creator`。

线上资料：

- https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
- https://claude.com/docs/skills/how-to
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills
- https://skills.sh/olafgeibig/skills/skill-builder
