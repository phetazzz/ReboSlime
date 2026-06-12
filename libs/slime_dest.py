# SlimeVR 服务器地址解析 / SlimeVR server destination resolution
DEFAULT_SLIME_IP = '127.0.0.1'
DEFAULT_SLIME_PORT = 6969


def resolve_slime_destination(config: dict):
    """解析 SlimeVR 服务器的发送地址。

    优先级 / Priority:
      1. slimevr_ip / slimevr_port  (新配置项, 用于跨主机 NAT 场景的单播发送)
      2. slime_ip / slime_port      (旧配置项, 保持向后兼容)
      3. 默认值 127.0.0.1:6969      (SlimeVR 标准端口)
    """
    ip = config.get('slimevr_ip') or config.get('slime_ip') or DEFAULT_SLIME_IP
    port = config.get('slimevr_port') or config.get('slime_port') or DEFAULT_SLIME_PORT
    return ip, int(port)
