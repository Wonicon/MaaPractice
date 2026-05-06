# Non-Retry Recognition + Click Nodes

| Node Name | File | Next |
|-----------|------|------|
| MissionClickWeekly | mission.json | `MissionWeeklyAcceptAll`, `MissionClose` |
| MissionWeeklyRewardsOK | mission.json | `MissionClose` |
| 再度远征 | daily.json | `确认远征中` |
| 确认 | daily.json | `再度远征` |
| FS01 点商店 | reinforce.json | `FS02 点商品` |
| FS02 点商品 | reinforce.json | `FS03 点石头` |
| FS03 点石头 | reinforce.json | `FS04 买` |
| FS04 买 | reinforce.json | `FS05 OK` |
| FS05 OK | reinforce.json | `FS 关闭窗口` |
| 入场券不足 | reinforce.json | `取消出击窗口` |
| 关闭领票 | reinforce.json | `点击任务` |
| 取消出击窗口 | reinforce.json | `点击返回` |
| 取消强化结果弹窗 | reinforce.json | `取消出击窗口` |
| 增加次数 | reinforce.json | `点击强化跳过` |
| 点击任务 | reinforce.json | `点击强化任务` |
| 点击强化任务 | reinforce.json | `强化任务中转` |
| 点击强化跳过 | reinforce.json | `确认强化跳过`, `入场券不足` |
| 点击返回 | reinforce.json | *(empty)* |
| 确认强化跳过 | reinforce.json | `取消强化结果弹窗` |
| 确认领票 | reinforce.json | `领票OK` |
| 领票 | reinforce.json | `确认领票` |
| 领票OK | reinforce.json | `关闭领票` |
| 领票回家 | reinforce.json | `领票确认home` |
| RaidClickElement | raid.json | `RaidSelectRecomend12000` |
| RaidSelectRecomend12000 | raid.json | `[JumpBack]RaidAddCost`, `RaidClickChallenge` |