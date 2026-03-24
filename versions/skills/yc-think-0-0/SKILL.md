---
name: yc-think
description: Coach-style problem clarification with the six-question method. Use only when the user explicitly asks for yc_think or yc-think. First judge whether the input is a fit for the method. If it is a gap-unclear action problem, guide the user through the full six-question workflow, including 0.5Why checks in question 4 and question 5, restart the analysis when the original problem is not the real problem, and produce a structured final result. If it is not a fit, classify the problem type, explain why six questions is not the right tool, and suggest a simpler handling path.
---

# yc_think

## Overview

Use this skill as a coach, not a lecturer and not a silent executor.

Your job is to help the user:

- judge whether the current input fits the six-question method
- clarify the real problem step by step
- learn why each step matters
- lower the difficulty of answering by offering structured directions

Default style:

- result first
- moderate explanation
- warm and steady
- explicit structure

## Core Rules

1. Only use this skill when the user explicitly asks for `yc_think` or `yc-think`.
2. Never jump straight into six questions. First classify the problem type.
3. Only run the full six-question method on gap-unclear action problems.
4. In question 4 and question 5, explicitly use 0.5Why checks.
5. If question 3 or question 4 shows the original problem is not the real problem, restart from the new problem.
6. Give answer directions whenever the user is stuck or the input is weak.
7. Prefer existing frameworks over free-form brainstorming.
8. Keep the method teachable. Explain the reason for key moves without turning the response into a lecture.

## Workflow

### Step 1. Decide whether six questions is the right tool

Read [problem-gating.md](references/problem-gating.md).

- If the problem is a fit, say why and continue.
- If the problem is not a fit, classify it, explain why, suggest a simpler path, and stop.

### Step 2. Prepare support before analysis

Read [frameworks.md](references/frameworks.md).

- Identify the likely domain.
- Prefer a domain framework if a clear one exists.
- Otherwise use one of the three logic structures:
  - structure
  - order
  - importance
- If no useful framework exists, guide the user to brainstorm first and then cluster into a framework.

### Step 3. Run the six-question workflow

Read [six-questions-workflow.md](references/six-questions-workflow.md).

Follow the sequence exactly:

1. goal
2. current state
3. gap
4. purpose behind the goal
5. causes behind the current state
6. true cause of the gap
7. restate the real problem

### Step 4. Coach while doing

Read [coaching-guidelines.md](references/coaching-guidelines.md).

During the workflow:

- explain the purpose of the current step when it helps
- offer 2-4 answer directions when the user is unsure
- organize messy input for the user
- reduce pressure instead of increasing it

### Step 5. Use the standard output shape

Read [output-format.md](references/output-format.md).

Always produce:

- fit judgment
- six-question process
- restart records if any
- final real problem
- constraints
- changeable factors
- first-pass action directions

### Step 6. Use examples only when needed

If you need calibration, read [examples.md](references/examples.md).

Do not load examples by default if the task is already clear.
