# yc_think

`yc_think` 是一个教练型元 skill，用“界定问题六问法”帮助用户把模糊、情绪化、方案化的问题，逐步转成一个结构清晰、可继续求解的真正问题。

当前这个仓库的目标不是一次性定稿，而是支持持续测试和迭代。重点是让它：

- 能在 Codex 上稳定工作
- 再迁移到 Claude Code 和 OpenClaw 继续测试
- 即使换电脑、换账号，也能继续接着做

## 当前状态

当前活跃版本：

- [skills/yc-think](D:\code\0324_2025\skills\yc-think)

历史版本：

- [yc-think-0-0](D:\code\0324_2025\versions\skills\yc-think-0-0)
- [yc-think-0-1](D:\code\0324_2025\versions\skills\yc-think-0-1)

当前活跃版定位：

- `v0.2`
- 默认互动
- 默认中文
- 第 1-3 问先问再看要不要给提示
- `0.5Why` 只在第 4、5 问显式使用

## 仓库结构

```text
docs/
  design/
  method/
evals/
  sessions/
skills/
  yc-think/
sources/
  raw/
  processed/
tools/
versions/
```

## 推荐先看

如果你第一次接手这个项目，建议先看：

1. [项目总览](D:\code\0324_2025\docs\PROJECT_OVERVIEW.md)
2. [交接说明](D:\code\0324_2025\docs\HANDOFF_2026-03-25.md)
3. [界定问题六问法](D:\code\0324_2025\docs\method\界定问题六问法.md)
4. [yc_think v0.2 升级分析](D:\code\0324_2025\docs\design\yc_think_v0_2升级分析.md)

## 原始素材

原始方法素材保存在：

- [sources/raw](D:\code\0324_2025\sources\raw)

处理后的结构化素材保存在：

- [sources/processed](D:\code\0324_2025\sources\processed)

## 测试材料

手工测试和评测样例保存在：

- [evals](D:\code\0324_2025\evals)

真实测试对话记录保存在：

- [evals/sessions](D:\code\0324_2025\evals\sessions)

## 命名说明

项目展示名使用 `yc_think`。

skill metadata 名称使用 `yc-think`，这样更符合通用 skill 校验器和跨平台代理对 `hyphen-case` 的偏好。用户显式调用时，仍然按 `yc_think` 来理解和触发。
