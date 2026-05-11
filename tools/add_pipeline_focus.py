# -*- coding: utf-8 -*-
"""
为 resource_*/pipeline/*.json 中的 pipeline 节点自动生成 focus 日志。

运行方式（请在项目根目录执行）：
    python tools/add_pipeline_focus.py

规则：
- 跳过以 '.' 开头的 JSON 文件
- 跳过 $__ 开头的编辑器配置节点
- 保留已有手工编写的 focus（判断依据：不含自动化特征词）
- 生成的 focus 以节点 key name 开头，后接识别类型、模板名/OCR文字、动作类型及屏幕方位
"""

import json
import os
import glob


def get_recog_info(node):
    rec = node.get("recognition")
    if isinstance(rec, str):
        rec_type = rec
        template = node.get("template")
        if isinstance(template, list):
            template = template[0] if template else None
        expected = node.get("expected")
        if isinstance(expected, list):
            expected = expected[0] if expected else None
        roi = node.get("roi")
        return rec_type, template, expected, roi
    elif isinstance(rec, dict):
        rec_type = rec.get("type", "DirectHit")
        param = rec.get("param", {})
        template = param.get("template")
        if isinstance(template, list):
            template = template[0] if template else None
        expected = param.get("expected")
        if isinstance(expected, list):
            expected = expected[0] if expected else None
        roi = param.get("roi")
        return rec_type, template, expected, roi
    else:
        return "DirectHit", None, None, None


def get_action_info(node):
    act = node.get("action")
    if isinstance(act, str):
        act_type = act
        target = node.get("target")
        return act_type, target
    elif isinstance(act, dict):
        act_type = act.get("type", "DoNothing")
        param = act.get("param", {})
        target = param.get("target")
        return act_type, target
    else:
        return "DoNothing", None


def describe_direction(rect):
    if not rect or len(rect) < 4:
        return None
    x, y, w, h = rect
    cx = x + w / 2
    cy = y + h / 2

    # 中央区域
    if 480 <= cx <= 800 and 240 <= cy <= 480:
        if 560 <= cx <= 720 and 300 <= cy <= 420:
            return "中央"
        if cx < 640 and cy < 360:
            return "中上偏左"
        elif cx >= 640 and cy < 360:
            return "中上偏右"
        elif cx < 640 and cy >= 360:
            return "中下偏左"
        else:
            return "中下偏右"

    h_dir = "左" if cx < 640 else "右"
    v_dir = "上" if cy < 360 else "下"

    # 如果靠近中间线，只给一个方向
    if 560 <= cx <= 720:
        return v_dir + "方"
    if 300 <= cy <= 420:
        return h_dir + "侧"

    return h_dir + v_dir


def is_auto_generated_focus(node):
    """判断 focus 是否看起来像是由本脚本自动生成的，以便重新生成。"""
    focus = node.get("focus")
    if not focus:
        return True
    if set(focus.keys()) != {"Node.Recognition.Succeeded"}:
        return False
    text = focus["Node.Recognition.Succeeded"]
    # 手工编写的 focus 通常不含这些自动化前缀
    markers = ["识别到", "直接命中", "，点击", "，等待", "停止任务", "执行", "滑动"]
    return any(m in text for m in markers)


def generate_focus(name, node):
    rec_type, template, expected, roi = get_recog_info(node)
    act_type, target = get_action_info(node)

    # 动作方位优先使用 action target（如果是矩形）
    action_pos = None
    if isinstance(target, list) and len(target) == 4:
        action_pos = target
    if not action_pos and roi and len(roi) == 4:
        action_pos = roi

    action_direction = describe_direction(action_pos)

    parts = []

    # 识别描述
    if rec_type == "DirectHit":
        parts.append("直接命中")
    elif rec_type == "TemplateMatch":
        if template:
            tpl_name = os.path.splitext(template)[0]
            parts.append(f"识别到{tpl_name}")
        else:
            parts.append("识别到目标图像")
    elif rec_type == "OCR":
        if expected:
            exp_text = expected if len(expected) <= 20 else expected[:20] + "…"
            parts.append(f"识别到{exp_text}文字")
        else:
            parts.append("识别到文字")
    elif rec_type == "ColorMatch":
        parts.append("识别到颜色目标")
    elif rec_type == "FeatureMatch":
        parts.append("识别到特征目标")
    elif rec_type == "NeuralNetwork":
        parts.append("识别到神经网络目标")
    elif rec_type == "And":
        parts.append("识别到组合目标(And)")
    elif rec_type == "Or":
        parts.append("识别到组合目标(Or)")
    else:
        parts.append(f"识别({rec_type})")

    # 动作描述
    if act_type == "Click":
        if action_direction:
            parts.append(f"点击{action_direction}")
        else:
            parts.append("点击目标")
    elif act_type == "DoNothing":
        parts.append("等待通过")
    elif act_type == "StopTask":
        parts.append("停止任务")
    elif act_type == "Swipe":
        if action_direction:
            parts.append(f"向{action_direction}滑动")
        else:
            parts.append("滑动操作")
    elif act_type == "Scroll":
        parts.append("滚动操作")
    elif act_type == "Key":
        parts.append("按键输入")
    elif act_type == "Shell":
        parts.append("执行Shell命令")
    elif act_type == "Command":
        parts.append("执行指令")
    elif act_type == "StartApp":
        parts.append("启动应用")
    elif act_type == "StopApp":
        parts.append("停止应用")
    else:
        parts.append(f"执行{act_type}")

    body = "，".join(parts)
    return f"{name}: {body}"


def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[ERROR] 无法读取 {filepath}: {e}")
        return 0

    if not isinstance(data, dict):
        return 0

    modified = False
    count = 0

    for name, node in data.items():
        if not isinstance(node, dict):
            continue
        if name.startswith("$__"):
            continue

        if not is_auto_generated_focus(node):
            continue

        focus_text = generate_focus(name, node)
        node["focus"] = {"Node.Recognition.Succeeded": focus_text}
        modified = True
        count += 1

    if modified:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.write("\n")
            print(f"[OK] {filepath} 更新了 {count} 个 focus")
        except Exception as e:
            print(f"[ERROR] 无法写入 {filepath}: {e}")
    else:
        print(f"[SKIP] {filepath} 无需修改")

    return count


def main():
    files = []
    for d in glob.glob("resource_*"):
        pipe_dir = os.path.join(d, "pipeline")
        if os.path.isdir(pipe_dir):
            for f in os.listdir(pipe_dir):
                if f.endswith(".json") and not f.startswith("."):
                    files.append(os.path.join(pipe_dir, f))

    total = 0
    for fp in sorted(files):
        total += process_file(fp)

    print(f"\n总计处理 {total} 个 focus 节点")


if __name__ == "__main__":
    main()
