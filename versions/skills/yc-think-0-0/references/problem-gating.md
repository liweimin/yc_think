# Problem Gating

## Purpose

Before using six questions, judge whether the user's input is a fit.

The method is best for:

- gap-unclear action problems

That usually means:

- someone needs to take action
- the current problem statement is vague, mixed, or emotionally framed
- goal, current state, or gap is unclear
- the user may be naming a solution instead of the real problem

## First-pass classification

Classify the input into one of these buckets.

### A. Gap-unclear action problem

Use full six-question workflow.

Examples:

- I want to improve team efficiency but I am not sure what the real problem is.
- I keep delaying this work and cannot explain why.
- I do not know what issue I should solve first in this project.

### B. Goal-unclear problem

Do not run full six questions yet.
Help the user define a clear goal first.

Examples:

- I want to do better.
- I want more growth.

### C. Current-state-unclear problem

Do not run full six questions yet.
Help the user collect facts, examples, and data.

Examples:

- I feel the team is not in good shape.
- The website feels weak.

### D. Pure information question

Do not use six questions.
Answer directly with normal reasoning or research.

Examples:

- What does this metric mean?
- How do I use this framework?

### E. Choice problem

Use a lighter decision analysis first.
If the real blocker is still a vague action problem, then switch into six questions.

Examples:

- Should I quit?
- Should I change teams?

### F. Emotional expression or venting

Do not force the method immediately.
First acknowledge the emotion and ask whether the user wants analysis, support, or both.

Examples:

- I am really overwhelmed.
- I am frustrated and do not know what to do.

## Output for the gating step

Always state:

1. whether six questions is a fit
2. what category the input belongs to
3. why that judgment makes sense
4. what you will do next

## If it is not a fit

Do not pretend it is.

Instead:

- name the problem type
- explain why six questions is not the best tool here
- use normal LLM reasoning to suggest a simpler handling path
- help the user build problem classification awareness
