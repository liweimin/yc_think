# 项目总览

## 1. 项目是什么

`yc_think` 是一个教练型元 skill。

它的核心不是替用户直接下结论，而是：

- 先判断用户当前输入是否适合用“界定问题六问法”
- 如果适合，就一步步带用户完成问题界定
- 如果不适合，就先帮助用户识别问题类型并给出更合适的处理方式

这个 skill 的额外目标是：

- 不只是帮用户完成一次分析
- 还要让用户逐步内化这套思考方式

## 2. 当前活跃版本

当前活跃版：

- [skills/yc-think](D:\code\0324_2025\skills\yc-think)

当前版本特征：

- 默认互动
- 默认中文
- 默认先让用户回答
- 用户明确要提示，或明显卡住时，才给回答方向
- `0.5Why` 只在第 4 问和第 5 问显式使用

## 3. 历史版本

为了方便回溯和对比，历史版本保存在：

- [yc-think-0-0](D:\code\0324_2025\versions\skills\yc-think-0-0)
- [yc-think-0-1](D:\code\0324_2025\versions\skills\yc-think-0-1)

当前活跃版相当于：

- `v0.2`

## 4. 目录说明

### `skills/yc-think`

当前活跃版 skill 本体。

### `versions/skills`

历史版本归档。

### `docs/method`

方法文档与方法说明。

### `docs/design`

设计分析、升级分析、需求对齐。

### `sources/raw`

原始素材：

- Word
- XMind
- 图片

### `sources/processed`

从原始素材转换出来的 LLM 可读结构化版本。

### `evals`

测试用例和真实 session 归档。

## 5. 关键文档

方法主文档：

- [界定问题六问法](D:\code\0324_2025\docs\method\界定问题六问法.md)

设计对齐文档：

- [yc_think需求对齐](D:\code\0324_2025\docs\design\yc_think需求对齐.md)
- [六问法Skill设计分析](D:\code\0324_2025\docs\design\六问法Skill设计分析.md)

版本升级文档：

- [yc_think v0.1 升级分析](D:\code\0324_2025\docs\design\yc_think_v0_1升级分析.md)
- [yc_think v0.2 升级分析](D:\code\0324_2025\docs\design\yc_think_v0_2升级分析.md)

## 6. 当前已知测试重点

当前重点验证的不是“它会不会六问法”，而是：

- 互动是否自然
- 第 1-3 问是否先问后导
- 第 3 问是否不再给人“提前 0.5Why”的感觉
- 用户卡住时，提示是否刚好够用

## 7. 下一步最重要的工作

下一步优先做：

1. 在 Codex 上继续用真实问题测试
2. 记录新的 session 到 `evals/sessions`
3. 根据真实体验继续迭代
4. 再在 Claude Code 和 OpenClaw 上迁移测试
