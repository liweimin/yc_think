# yc_think

`yc_think` 当前更适合被理解成一个“给下一位 agent 的素材库”。

这个仓库保存的不是一套已经定型的 skill，而是一整组原始 source、真实 session、训练文档、设计迭代记录，以及用户与 AI 在推进这个项目过程中的关键转向。它的目标是让下一位 agent 在吃完这些材料后，不只是“会六问法”，而是更有机会：

- 理解六问法原始方法与边界
- 理解用户是如何和 AI 互动、试错、修正的
- 看见用户背后的真实目标、偏好与协作方式
- 以后更像一个“思维教练顾问”，而不只是一个会执行流程的 skill

## 当前重点

当前主线不是继续打磨 `skills/yc-think`，而是：

- 保留完整原始 source
- 保留完整原始 session
- 给下一位 agent 一条高信号阅读路径
- 补充项目过程中的关键启发、转向和用户画像

`skills/` 目录仍然保留，但现在更接近历史背景和阶段性产物，不是仓库的唯一重点。

## 建议先看

如果你是下一位接手的 agent，建议按这个顺序进入：

1. [docs/agent-handoff/README.md](docs/agent-handoff/README.md)
2. [docs/agent-handoff/01-materials-map.md](docs/agent-handoff/01-materials-map.md)
3. [docs/agent-handoff/02-project-trajectory.md](docs/agent-handoff/02-project-trajectory.md)
4. [docs/agent-handoff/03-user-intent-and-coaching-guidance.md](docs/agent-handoff/03-user-intent-and-coaching-guidance.md)
5. [docs/agent-handoff/04-next-agent-prompt.md](docs/agent-handoff/04-next-agent-prompt.md)
6. [docs/六问法教练训练/README.md](docs/六问法教练训练/README.md)
7. [evals/sessions/README.md](evals/sessions/README.md)

如果要追原始依据，再回看：

- [sources/raw](sources/raw)
- [evals/sessions/raw](evals/sessions/raw)

## 仓库结构

```text
docs/
  agent-handoff/
  design/
  method/
  六问法教练训练/
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

## 材料分层

可以把这个仓库理解成四层材料：

1. 原始层：`sources/raw/` 与 `evals/sessions/raw/`
2. 可读层：`docs/method/`、`docs/六问法教练训练/`、`evals/sessions/parsed/`
3. 演进层：`docs/design/` 与各类 handoff 文档
4. 交接层：`docs/agent-handoff/`

## 历史说明

这个仓库最早是围绕“六问法教练型 skill”来搭建的，所以你仍然会看到：

- 当前活跃 skill：[skills/yc-think](skills/yc-think/SKILL.md)
- 历史版本：[versions/skills](versions/skills)
- skill 设计文档：[docs/design](docs/design)

这些内容仍然重要，但现在应该作为“项目过程素材”来读，而不是默认把下一步理解成“继续改 skill”。
