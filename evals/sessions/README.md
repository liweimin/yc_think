# Session 索引

当前 `evals/sessions` 目录仍然保持扁平存放，但已经可以按“用途”来理解，不需要先移动文件才能使用。

## 1. 设计 / 演进类 session

| Session | Raw | 可读稿 | 说明 |
| --- | --- | --- | --- |
| `Claude 983d477f-4f8a-4e86-b51c-4cda31115d6a` | [raw/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.jsonl](raw/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.jsonl) | [parsed/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.md](parsed/claude-983d477f-4f8a-4e86-b51c-4cda31115d6a.md) | Claude Code 里的最早原型与技能安装尝试。 |
| `019d1ede-3c3e-7d60-8f60-ad244e62333b` | [raw/rollout-2026-03-24T16-02-54-019d1ede-3c3e-7d60-8f60-ad244e62333b.jsonl](raw/rollout-2026-03-24T16-02-54-019d1ede-3c3e-7d60-8f60-ad244e62333b.jsonl) | [parsed/019d1ede-3c3e-7d60-8f60-ad244e62333b.md](parsed/019d1ede-3c3e-7d60-8f60-ad244e62333b.md) | 在 Codex 中接手原始 Word 并形成最早技能雏形。 |
| `019d1fd0-2e90-7f90-92b4-8658a9adde4d` | [raw/019d1fd0-2e90-7f90-92b4-8658a9adde4d.jsonl](raw/019d1fd0-2e90-7f90-92b4-8658a9adde4d.jsonl) | [parsed/019d1fd0-2e90-7f90-92b4-8658a9adde4d.md](parsed/019d1fd0-2e90-7f90-92b4-8658a9adde4d.md) | 早期设计与项目定位。 |
| `019d22a8-e8f8-7da1-b5c5-f58c4907558a` | [raw/rollout-2026-03-25T09-43-08-019d22a8-e8f8-7da1-b5c5-f58c4907558a.jsonl](raw/rollout-2026-03-25T09-43-08-019d22a8-e8f8-7da1-b5c5-f58c4907558a.jsonl) | [parsed/019d22a8-e8f8-7da1-b5c5-f58c4907558a.md](parsed/019d22a8-e8f8-7da1-b5c5-f58c4907558a.md) | 从改 skill 转向先训练方法理解与教练能力。 |
| `019d2371-8161-7b71-93f4-2cad0fd9a5a8` | [raw/rollout-2026-03-25T13-22-14-019d2371-8161-7b71-93f4-2cad0fd9a5a8.jsonl](raw/rollout-2026-03-25T13-22-14-019d2371-8161-7b71-93f4-2cad0fd9a5a8.jsonl) | [parsed/019d2371-8161-7b71-93f4-2cad0fd9a5a8.md](parsed/019d2371-8161-7b71-93f4-2cad0fd9a5a8.md) | 用户如何重新理解六问法、行动风格与老师沟通。 |
| `019d2399-3a08-7ab2-a9bb-e43196ec99ea` | [raw/rollout-2026-03-25T14-05-37-019d2399-3a08-7ab2-a9bb-e43196ec99ea.jsonl](raw/rollout-2026-03-25T14-05-37-019d2399-3a08-7ab2-a9bb-e43196ec99ea.jsonl) | [parsed/019d2399-3a08-7ab2-a9bb-e43196ec99ea.md](parsed/019d2399-3a08-7ab2-a9bb-e43196ec99ea.md) | 明确把仓库重定位成给下一位 agent 的素材库，并补捞本机历史对话。 |

## 2. 测试类 session

| Session | Raw | 可读稿 | 说明 |
| --- | --- | --- | --- |
| `019d2086-9364-7370-bacd-9cea6da0c510` | [raw/019d2086-9364-7370-bacd-9cea6da0c510.jsonl](raw/019d2086-9364-7370-bacd-9cea6da0c510.jsonl) | [parsed/019d2086-9364-7370-bacd-9cea6da0c510.md](parsed/019d2086-9364-7370-bacd-9cea6da0c510.md) | `v0.2` 的真实测试与问题暴露。 |

## 3. 使用建议

如果你是下一位 agent，建议先读：

1. `Claude 983d...`
2. `019d1ede`
3. `019d22a8`
4. `019d2371`
5. `019d2399`
6. `019d2086`
7. `019d1fd0`

这个顺序更容易先看见：

- 项目是如何在 Claude / Codex 的原型尝试里启动的
- 方法理解如何一步步压过 skill 设计
- 用户与 AI 的协作风格如何逐渐显露
- 真实测试暴露了什么问题
- 仓库最早又如何被正式组织起来

## 4. 原来的简化顺序

如果你只想看当前最关键的四轮，也可以先读：

1. `019d22a8`
2. `019d2371`
3. `019d2399`
4. `019d2086`
5. `019d1fd0`
