# 下一台 Codex 接班说明

这份文档的目标不是介绍项目，而是让另一台电脑上的 Codex 尽快进入正确工作状态，继续协助迭代 `yc_think`。

## 1. 这台新的 Codex 需要知道什么

请把下面几点当成项目事实：

- 项目名称：`yc_think`
- 项目目标：把“界定问题六问法”做成一个教练型元 skill
- 当前活跃版本：`v0.2`
- 当前活跃 skill：`skills/yc-think/SKILL.md`
- 历史版本保留在：`versions/skills/`
- 当前主要测试平台顺序：
  1. Codex
  2. Claude Code
  3. OpenClaw

## 2. 这个 skill 的核心定位

`yc_think` 不是普通问答 skill，而是一个教练型元 skill。

它的职责是：

- 先判断用户输入是否适合用“界定问题六问法”
- 只有在“差距不明确的行动类问题”上，才进入完整六问法
- 如果不适合，就先识别问题类型，并给出更适合的处理建议
- 在执行六问法时，不只是帮用户完成分析，还要帮助用户逐步内化这种思考方式

## 3. 当前已经明确的设计约束

下一台 Codex 不要偏离这些约束：

- 用户通常会显式说 `Use yc_think`
- 默认中文
- 默认互动，不要一口气把整套六问法直接答完
- 第 1-3 问默认先问用户，再决定是否给提示
- 只有用户明确要提示、明显卡住、或回答过于模糊无法继续时，才给回答方向
- `0.5Why` 主要用于第 4 问和第 5 问
- 第 3 问不要写成 `0.5Why`，也不要太像验证式逼问
- 如果第 3 问或第 4 问发现原问题不是真问题，需要重开新一轮六问法

## 4. 当前最重要的测试结论

`v0.0` 的主要问题：

- 模型自己把整套流程答完了
- 不够互动

`v0.1` 的主要改进：

- 开始互动
- 默认中文

`v0.2` 的主要改进：

- 第 1-3 问默认先问，不先给方向
- 把 `0.5Why` 的显式边界收回到第 4、5 问

`v0.2` 当前仍然需要继续验证的重点：

1. 第 1-3 问是否真正做到了“先问后导”
2. 第 3 问是否不再让用户感觉提前用了 `0.5Why`
3. 用户请求提示时，提示是否足够具体但不过度干扰

## 5. 下一台 Codex 先看哪些文件

建议按这个顺序读取：

1. `README.md`
2. `docs/HANDOFF_2026-03-25.md`
3. `docs/PROJECT_OVERVIEW.md`
4. `docs/design/yc_think_v0_2升级分析.md`
5. `skills/yc-think/SKILL.md`
6. `skills/yc-think/references/six-questions-workflow.md`
7. `skills/yc-think/references/coaching-guidelines.md`
8. `skills/yc-think/references/output-format.md`

如果需要方法背景，再看：

- `docs/method/界定问题六问法.md`

如果需要历史上下文，再看：

- `evals/sessions/parsed/019d1fd0-2e90-7f90-92b4-8658a9adde4d.md`
- `evals/sessions/parsed/019d2086-9364-7370-bacd-9cea6da0c510.md`

## 6. 明天开工建议

不要直接改 skill。

先做这三步：

1. 复测 `v0.2`
2. 记录真实体验
3. 只围绕真实问题设计 `v0.3`

推荐先复测这两个 prompt：

`Use yc_think. 我总是拖延本月学习任务，但我也说不清真正的问题是什么。请按这个方法帮我分析。`

`Use yc_think. 我总是拖延本月学习任务，但我不知道第1问该怎么答。你给我几个思路。`

## 7. 给下一台 Codex 的开场提示词

明天可以直接把下面这段发给新的 Codex：

```text
请接手这个仓库里的 yc_think 项目，并继续协助我迭代。

先不要直接改代码或 skill。先完成这几件事：
1. 阅读 README.md
2. 阅读 docs/HANDOFF_2026-03-25.md
3. 阅读 docs/PROJECT_OVERVIEW.md
4. 阅读 docs/design/yc_think_v0_2升级分析.md
5. 阅读 skills/yc-think/SKILL.md
6. 阅读 skills/yc-think/references/six-questions-workflow.md
7. 阅读 skills/yc-think/references/coaching-guidelines.md
8. 阅读 skills/yc-think/references/output-format.md

然后用你自己的话总结：
- yc_think 是什么
- 当前版本是 v0.2，主要设计点是什么
- 目前已知问题和待验证点是什么
- 如果今天继续做 v0.3，你建议先测什么、再改什么

补充背景：
- 这是一个教练型元 skill，不是一次性给答案的工具
- 目标是让用户在使用过程中逐步内化“界定问题六问法”
- 默认中文，默认互动
- 第 1-3 问先问后导
- 0.5Why 主要用于第 4、5 问
- 如果第 3、4 问发现原问题不成立，需要重开
```

## 8. 为什么这样交接更稳

因为新的 Codex 不会自动继承今天这轮对话上下文。

所以最稳的方式不是依赖“记忆”，而是让仓库本身变成上下文载体：

- 方法在文档里
- 设计约束在文档里
- 历史测试在 session 归档里
- 下一步建议在交接文档里
- 给新 Codex 的启动提示词也固定下来

这样换电脑、换账号，甚至换 agent，都还能继续推进。
