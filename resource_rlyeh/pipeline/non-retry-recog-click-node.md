# 非重试识别点击节点 (Non-Retry Recognition+Click Nodes)

这些节点同时具有 recognition 和 click，但没有自跳重试，也没有被其他节点作为 JumpBack 目标。
计划：为它们添加 `自己名字` 到 next 列表末尾实现自跳重试。

**总计: 21 个节点**

## FreeStonePack
- **来源文件**: `free_stone.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: []

## Change2ImportantMail
- **来源文件**: `login.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['RecvImportant']

## ClickMail
- **来源文件**: `login.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['[JumpBack]ErrorPopup', 'ClickMailDelay', 'RecvNormal']

## CloseMail
- **来源文件**: `login.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: []

## RecvImportant
- **来源文件**: `login.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['[JumpBack]RecvNormalResult', 'RecvImportantDelay']

## RecvNormal
- **来源文件**: `login.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['[JumpBack]RecvNormalResult', 'RecvNormalDelay']

## SoundConfirmPopup_ClickOK
- **来源文件**: `login.json`
- **识别类型**: `ColorMatch`
- **动作类型**: `Click`
- **当前 next**: []

## CheckRecvMission
- **来源文件**: `mission.json`
- **识别类型**: `ColorMatch`
- **动作类型**: `Click`
- **当前 next**: ['ClickAllRecv']

## ClickAllRecv
- **来源文件**: `mission.json`
- **识别类型**: `ColorMatch`
- **动作类型**: `Click`
- **当前 next**: ['MissionResult']

## MissionClose
- **来源文件**: `mission.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: []

## MissionIcon
- **来源文件**: `mission.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['CheckMissionWindow', 'MissionIconDelay']

## MissionLabel
- **来源文件**: `mission.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['CheckMissionWindow', 'MissionIconDelay']

## MissionResult
- **来源文件**: `mission.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['MissionRecvPrise']

## PriseResult
- **来源文件**: `mission.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['MissionClose']

## 主线快速战斗免费
- **来源文件**: `shoujotai.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['主线快速战斗执行']

## 主线收菜弹出
- **来源文件**: `shoujotai.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['主线收菜弹出报酬弹窗']

## 主线收菜弹出报酬弹窗
- **来源文件**: `shoujotai.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['主线快速战斗']

## 展开跳过
- **来源文件**: `shoujotai.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['跳过']

## 祭坛挑战用完
- **来源文件**: `shoujotai.json`
- **识别类型**: `OCR`
- **动作类型**: `Click`
- **当前 next**: ['返回spot']

## 竞技场内部
- **来源文件**: `shoujotai.json`
- **识别类型**: `TemplateMatch`
- **动作类型**: `Click`
- **当前 next**: ['竞技场没次数', '竞技场找对手']

## 竞技场出击
- **来源文件**: `shoujotai.json`
- **识别类型**: `ColorMatch`
- **动作类型**: `Click`
- **当前 next**: ['[JumpBack]战斗中_副本33_副本50', '竞技场继续找对手']
