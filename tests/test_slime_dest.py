import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from libs.slime_dest import resolve_slime_destination


class TestResolveSlimeDestination(unittest.TestCase):
    def test_new_keys(self):
        ip, port = resolve_slime_destination(
            {'slimevr_ip': '192.168.1.50', 'slimevr_port': 7000})
        self.assertEqual((ip, port), ('192.168.1.50', 7000))

    def test_legacy_keys_still_work(self):
        # 旧 config.json (slime_ip / slime_port) 必须保持原有行为
        ip, port = resolve_slime_destination(
            {'slime_ip': '127.0.0.1', 'slime_port': 6969})
        self.assertEqual((ip, port), ('127.0.0.1', 6969))

    def test_new_keys_take_precedence(self):
        ip, port = resolve_slime_destination({
            'slime_ip': '127.0.0.1', 'slime_port': 6969,
            'slimevr_ip': '10.0.0.2', 'slimevr_port': 6970,
        })
        self.assertEqual((ip, port), ('10.0.0.2', 6970))

    def test_defaults_when_unspecified(self):
        ip, port = resolve_slime_destination({})
        self.assertEqual((ip, port), ('127.0.0.1', 6969))

    def test_port_string_is_coerced(self):
        ip, port = resolve_slime_destination(
            {'slimevr_ip': '10.0.0.2', 'slimevr_port': '6969'})
        self.assertEqual(port, 6969)


if __name__ == '__main__':
    unittest.main()
