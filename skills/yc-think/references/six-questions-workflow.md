# Six-Questions Workflow

## Core sequence

Run the workflow in this order:

1. Goal
2. Current state
3. Gap
4. Purpose behind the goal
5. Causes behind the current state
6. True cause of the gap
7. Restate the real problem

Do not skip steps.

## Interaction rule

Default mode is not one-shot completion.

For each unresolved step:

1. explain the step briefly
2. state the temporary understanding
3. ask first
4. give answer directions only if needed
5. ask one focused question
6. wait for the user's reply

Only continue without waiting if:

- the user explicitly asks for a draft
- or the current step is already grounded by the user's earlier information and only needs a short confirmation

## Question 1. What is the goal

Clarify what success means.

Requirements:

- clear
- measurable when possible
- same user, same scope, same time frame
- preferably one goal at a time

Useful prompts:

- What outcome do you want?
- By when?
- What would count as solved?
- Can we make that more concrete or measurable?

Chinese default prompts:

- 你真正想达到的结果是什么？
- 你希望在什么时间内做到？
- 到什么程度才算解决？

Only offer directions here if the user asks for help or cannot answer clearly.

## Question 2. What is the current state

Describe the current reality in the same dimension as the goal.

Requirements:

- facts over feelings
- same dimension as the goal
- include current examples, data, or frequency when possible

Useful prompts:

- What is happening now?
- What is the current level, count, rate, or condition?
- If nothing changes, what will happen by the target time?

Chinese default prompts:

- 现在真实发生的情况是什么？
- 如果什么都不改，到目标时间点大概会怎样？

Only offer directions here if the user asks for help or cannot answer clearly.

## Question 3. What is the gap

Compute the gap between goal and current state.

Formula:

- gap = goal - current state

If there is no real gap, or the gap points somewhere else, say so.

If question 3 shows the original problem is not a valid problem:

1. explain why
2. write the new problem
3. restart the workflow from question 1

Chinese default prompts:

- 现在看，原始问题真的成立吗？
- 真正的差距更像落在什么地方？
- 如果原问题不成立，我们要不要换成一个更准确的新问题？

Important:

- question 3 can confirm or reframe the gap
- question 3 should not be labeled as 0.5Why
- do not use 0.5Why language here
- avoid binary yes/no validation wording when possible
- prefer: ask the user to rewrite the gap in one sentence, or choose the closest version and then refine it

## Question 4. What is the purpose behind the goal

This question checks whether the stated goal is the real goal, or only a proposed solution.

Use 5Why and 0.5Why here.

### 0.5Why form for question 4

Use:

- [answer] means you must [current goal]?

Purpose:

- test whether the current goal is the only valid path
- surface a deeper goal if needed

If question 4 reveals a new real goal:

1. preserve the current round
2. name the old goal and new goal
3. explain why the old goal was only a provisional solution
4. restart the workflow from question 1 using the new goal

Chinese default prompts:

- 你想要这个目标，背后真正想解决的是什么？
- 这个目标一定是唯一办法吗？
- 如果不是唯一办法，那我们真正要解决的问题是哪一个？

## Question 5. What causes the current state

This question looks for the reasons behind the current state.

Use:

- a framework first
- then 5Why
- then 0.5Why

### 0.5Why form for question 5

Use:

- [reason] will definitely cause [current state or problem]?

Purpose:

- remove weak causes
- remove excuses
- remove background-only conditions
- find more direct causes

Recommended sub-sequence:

1. generate possible causes
2. group them with a framework
3. identify likely key causes
4. run 0.5Why on each key cause
5. keep digging only on causes that pass

Chinese default prompts:

- 造成当前现状的原因，你觉得更像是结构问题、顺序问题，还是优先级问题？
- 如果你一时说不全，我先给你几个方向，你来判断哪个最接近。
- 这个原因真的会直接导致当前现状吗，还是只是背景条件？

## Question 6. What is the true cause of the gap

This is a summary question, not a new brainstorm.

Summarize the first five questions into:

- whether the goal is reasonable
- which factors are constraints
- which factors are changeable

Then turn the result into the real problem statement.

## Restart rule

Restart when either of these is true:

- question 3 shows the original problem is not a real problem
- question 4 shows the stated goal is only a provisional solution

When restarting, always keep:

- original problem
- why it failed
- new problem
- new round result

## Stop rule

When digging causes in question 5, stop when:

- fixing this level would prevent recurrence
- you have reached the boundary of authority, resources, or knowledge
- you can no longer identify a more specific next-level cause

Also stop if:

- the chain becomes repetitive
- the chain becomes circular
- the chain drifts away from the original issue
