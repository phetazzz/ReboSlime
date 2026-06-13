# 送出ノードリストの解析 / Resolution of the node list sent to SlimeVR
#
# ノード番号は ReboCap SDK の関节索引 (REBOCAP_JOINT_NAMES) であり,
# これは SMPL 24 関节のインデックスと一致する (0=Pelvis/骨盆, 1=L_Hip, ...).
# したがって config 側に書く番号はそのまま tracker_id として送出される (変換不要).
#
# The node numbers are ReboCap SDK joint indices (REBOCAP_JOINT_NAMES), which
# match the SMPL 24-joint indices (0=Pelvis, 1=L_Hip, ...). Numbers written in
# the config are therefore used verbatim as tracker ids (no remapping).

VALID_PRESETS = (6, 8, 10, 12, 15)


def resolve_node_list(config: dict, count=None):
    """送出するノードの確定リストを決定する.

    优先级 / Priority:
      1. custom_points  (存在し空でなければ, 点数プリセットを完全に无视してこれを使う)
      2. imus[str(count)]  (従来の点数プリセット, 后方兼容)

    custom_points 指定时はリストに书かれた通りを尊重し, 勝手に 0 番ノード等を
    追加したり並べ替えたりしない (顺序保持のまま重复だけ取り除く).

    Returns:
        (nodes, source):
            nodes  -- list[int] 送出ノード番号 (= SMPL/REBOCAP joint index)
            source -- str       決定根拠の説明 (ログ用)

    Raises:
        ValueError: custom_points も有効なプリセットも无い場合.
    """
    custom = config.get('custom_points')
    if custom:
        nodes = []
        for n in custom:
            n = int(n)
            if n not in nodes:  # 顺序保持の重复除去 (重复追加はしない)
                nodes.append(n)
        return nodes, 'custom_points'

    presets = config.get('imus', {})
    key = str(count)
    if key not in presets:
        raise ValueError(
            f'未定义的点数プリセット: {count} (支持: {", ".join(map(str, VALID_PRESETS))})')
    return list(presets[key]), f'{count}-point preset'
