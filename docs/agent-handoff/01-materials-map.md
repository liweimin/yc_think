# 材料总表

这份总表的目的，是让下一位 agent 不用先自己摸索，就能知道哪些材料是“源头”，哪些材料是“二次整理”，以及每份材料为什么重要。

## 1. 原始 source

- [../../sources/raw/界定问题六问法.docx](../../sources/raw/界定问题六问法.docx)
  说明：六问法主流程的原始方法文档，是问题界定骨架的主要源头。

- [../../sources/raw/真正用好5why（图文版）.docx](../../sources/raw/真正用好5why（图文版）.docx)
  说明：第五问与 `0.5Why / 5Why` 的核心原始依据。

- [../../sources/raw/chatgpt.com-六问法与生命观融合.docx](../../sources/raw/chatgpt.com-六问法与生命观融合.docx)
  说明：用户“最近的新路”的重要来源，把六问法和“从动到在”的生命观连起来。

- [../../sources/raw/六问法示例1：2个月内优化业务流程，提升团队工作效率20_.xmind](../../sources/raw/六问法示例1：2个月内优化业务流程，提升团队工作效率20_.xmind)
  说明：六问法示例材料，能帮助校准第三问、第四问和重开的真实用法。

- [../../sources/raw/01-5why原因要求示例-为什么我会拖延 本月学习任务？.xmind](../../sources/raw/01-5why原因要求示例-为什么我会拖延%20本月学习任务？.xmind)
  说明：第五问的原因分析与停止条件示例。

## 2. LLM 更容易直接阅读的衍生材料

- [../method/界定问题六问法.md](../method/界定问题六问法.md)
  说明：对六问法原始材料的结构化整理稿。

- [../六问法教练训练/README.md](../六问法教练训练/README.md)
  说明：从“先做 skill”切换到“先理解方法、先成为教练”的训练入口。

- [../六问法教练训练/02-第三问与第四问的边界.md](../六问法教练训练/02-第三问与第四问的边界.md)
  说明：老师反馈后的关键边界文档。

- [../六问法教练训练/06-六问法与从动到在的双模式融合.md](../六问法教练训练/06-六问法与从动到在的双模式融合.md)
  说明：把六问法与用户的新路连接起来的压缩版文档。

- [../design](../design)
  说明：历史设计与版本迭代文档，适合了解仓库为什么会先长成一个 skill 项目。

## 3. Session 语料

| 分类 | Session | Raw | 可读稿 | 价值 |
| --- | --- | --- | --- | --- |
| 前史原型（Claude Code） | `983d477f-4f8a-4e86-b51c-4cda31115d6a` | [../../evals/sessions/raw/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.jsonl](../../evals/sessions/raw/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.jsonl) | [../../evals/sessions/parsed/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.md](../../evals/sessions/parsed/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.md) | 项目在 Claude Code 里的最早原型与技能安装尝试。 |
| 前史原型（Codex） | `019d1ede-3c3e-7d60-8f60-ad244e62333b` | [../../evals/sessions/raw/rollout-2026-03-24T16-02-54-019d1ede-3c3e-7d60-8f60-ad244e62333b.jsonl](../../evals/sessions/raw/rollout-2026-03-24T16-02-54-019d1ede-3c3e-7d60-8f60-ad244e62333b.jsonl) | [../../evals/sessions/parsed/019d1ede-3c3e-7d60-8f60-ad244e62333b.md](../../evals/sessions/parsed/019d1ede-3c3e-7d60-8f60-ad244e62333b.md) | 把原始 Word 迁入 Codex 并形成最早本地 skill 思路。 |
| 设计起点 | `019d1fd0-2e90-7f90-92b4-8658a9adde4d` | [../../evals/sessions/raw/019d1fd0-2e90-7f90-92b4-8658a9adde4d.jsonl](../../evals/sessions/raw/019d1fd0-2e90-7f90-92b4-8658a9adde4d.jsonl) | [../../evals/sessions/parsed/019d1fd0-2e90-7f90-92b4-8658a9adde4d.md](../../evals/sessions/parsed/019d1fd0-2e90-7f90-92b4-8658a9adde4d.md) | 早期设计与项目定位来源。 |
| 测试验证 | `019d2086-9364-7370-bacd-9cea6da0c510` | [../../evals/sessions/raw/019d2086-9364-7370-bacd-9cea6da0c510.jsonl](../../evals/sessions/raw/019d2086-9364-7370-bacd-9cea6da0c510.jsonl) | [../../evals/sessions/parsed/019d2086-9364-7370-bacd-9cea6da0c510.md](../../evals/sessions/parsed/019d2086-9364-7370-bacd-9cea6da0c510.md) | v0.2 的真实测试依据。 |
| 方法训练与方向转向 | `019d22a8-e8f8-7da1-b5c5-f58c4907558a` | [../../evals/sessions/raw/rollout-2026-03-25T09-43-08-019d22a8-e8f8-7da1-b5c5-f58c4907558a.jsonl](../../evals/sessions/raw/rollout-2026-03-25T09-43-08-019d22a8-e8f8-7da1-b5c5-f58c4907558a.jsonl) | [../../evals/sessions/parsed/019d22a8-e8f8-7da1-b5c5-f58c4907558a.md](../../evals/sessions/parsed/019d22a8-e8f8-7da1-b5c5-f58c4907558a.md) | 从“改 skill”转向“先做教练理解”的关键 session。 |
| 自我理解与老师沟通 | `019d2371-8161-7b71-93f4-2cad0fd9a5a8` | [../../evals/sessions/raw/rollout-2026-03-25T13-22-14-019d2371-8161-7b71-93f4-2cad0fd9a5a8.jsonl](../../evals/sessions/raw/rollout-2026-03-25T13-22-14-019d2371-8161-7b71-93f4-2cad0fd9a5a8.jsonl) | [../../evals/sessions/parsed/019d2371-8161-7b71-93f4-2cad0fd9a5a8.md](../../evals/sessions/parsed/019d2371-8161-7b71-93f4-2cad0fd9a5a8.md) | 用户如何重新理解六问法、行动风格与训练需求。 |
| 当前重定位与补档 | `019d2399-3a08-7ab2-a9bb-e43196ec99ea` | [../../evals/sessions/raw/rollout-2026-03-25T14-05-37-019d2399-3a08-7ab2-a9bb-e43196ec99ea.jsonl](../../evals/sessions/raw/rollout-2026-03-25T14-05-37-019d2399-3a08-7ab2-a9bb-e43196ec99ea.jsonl) | [../../evals/sessions/parsed/019d2399-3a08-7ab2-a9bb-e43196ec99ea.md](../../evals/sessions/parsed/019d2399-3a08-7ab2-a9bb-e43196ec99ea.md) | 明确把仓库从 skill 项目重定位成“给下一位 agent 的素材库”。 |

## 4. 额外上下文

- [../HANDOFF_2026-03-25.md](../HANDOFF_2026-03-25.md)
  说明：早期交接文档，偏 skill 迭代阶段。

- [../NEXT_SESSION_BOOTSTRAP.md](../NEXT_SESSION_BOOTSTRAP.md)
  说明：给当时下一台 Codex 的启动说明，能看出旧阶段的优先级。

- [../PROJECT_OVERVIEW.md](../PROJECT_OVERVIEW.md)
  说明：项目总览，仍有参考价值，但需要结合当前目录重新理解。

## 5. 如果只能先读三份

建议先读：

1. [02-project-trajectory.md](02-project-trajectory.md)
2. [03-user-intent-and-coaching-guidance.md](03-user-intent-and-coaching-guidance.md)
3. `019d22a8` 与 `019d2371` 两个 session 的 raw 或可读稿
