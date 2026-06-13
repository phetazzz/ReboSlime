import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from libs.node_list import resolve_node_list


PRESETS = {
    "6": [0, 9, 3, 1, 2, 4, 5],
    "8": [0, 9, 3, 1, 2, 4, 5, 7, 8],
    "10": [0, 9, 3, 1, 2, 4, 5, 7, 8, 10, 11],
    "12": [0, 9, 3, 1, 2, 4, 5, 7, 8, 10, 11, 18, 19],
    "15": [0, 9, 3, 1, 2, 4, 5, 7, 8, 10, 11, 18, 19, 22, 23, 15],
}


class TestResolveNodeList(unittest.TestCase):
    def test_preset_used_when_no_custom_points(self):
        nodes, source = resolve_node_list({'imus': PRESETS}, 8)
        self.assertEqual(nodes, PRESETS['8'])
        self.assertEqual(source, '8-point preset')

    def test_all_presets_unchanged(self):
        # 后方兼容: 各プリセットがそのまま返ること
        for count, expected in (
                (6, PRESETS['6']), (8, PRESETS['8']), (10, PRESETS['10']),
                (12, PRESETS['12']), (15, PRESETS['15'])):
            nodes, source = resolve_node_list({'imus': PRESETS}, count)
            self.assertEqual(nodes, expected)
            self.assertEqual(source, f'{count}-point preset')

    def test_custom_points_take_precedence(self):
        cfg = {'imus': PRESETS, 'custom_points': [0, 9, 1, 2, 4, 5, 7, 8, 16, 17]}
        # プリセット (count=8) を渡しても custom_points が优先される
        nodes, source = resolve_node_list(cfg, 8)
        self.assertEqual(nodes, [0, 9, 1, 2, 4, 5, 7, 8, 16, 17])
        self.assertEqual(source, 'custom_points')

    def test_custom_points_used_when_count_is_none(self):
        cfg = {'imus': PRESETS, 'custom_points': [16, 17]}
        nodes, source = resolve_node_list(cfg, None)
        self.assertEqual(nodes, [16, 17])
        self.assertEqual(source, 'custom_points')

    def test_custom_points_order_preserved_and_deduped(self):
        cfg = {'custom_points': [17, 16, 0, 16, 17]}
        nodes, _ = resolve_node_list(cfg, None)
        # 顺序保持 + 重复除去, 勝手な並べ替え・追加をしない
        self.assertEqual(nodes, [17, 16, 0])

    def test_empty_custom_points_falls_back_to_preset(self):
        cfg = {'imus': PRESETS, 'custom_points': []}
        nodes, source = resolve_node_list(cfg, 6)
        self.assertEqual(nodes, PRESETS['6'])
        self.assertEqual(source, '6-point preset')

    def test_custom_points_returns_independent_list(self):
        # 返り值を变更しても元 config を壊さないこと
        cfg = {'custom_points': [0, 9]}
        nodes, _ = resolve_node_list(cfg, None)
        nodes.append(99)
        self.assertEqual(cfg['custom_points'], [0, 9])

    def test_invalid_preset_raises(self):
        with self.assertRaises(ValueError):
            resolve_node_list({'imus': PRESETS}, 7)

    def test_no_custom_no_valid_preset_raises(self):
        with self.assertRaises(ValueError):
            resolve_node_list({}, None)


if __name__ == '__main__':
    unittest.main()
