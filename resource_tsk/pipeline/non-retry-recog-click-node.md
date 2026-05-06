# Non-Retry Recognition+Click Nodes

These nodes have recognition and click, no self-retry, and are not JumpBack targets.

- `daily.json` → `ClickExerciseRewards`
  - current next: ['BackToQuest']

- `daily.json` → `ConfirmExerciseSkip`
  - current next: ['ClickExerciseRewards']

- `daily.json` → `SelectUnlimitQuestType`
  - current next: ['SkipExerciseOk']

- `daily.json` → `SkipExercise`
  - current next: ['SelectUnlimitQuestType']

- `daily.json` → `SkipExerciseOk`
  - current next: ['ConfirmExerciseSkip']
