<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="./assets/round_reboslime.png" style="border-radius: 100px;" width="200" height="200" alt="ReboSlime">
</p>


<div align="center">

# ReboSlime

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
<div>在 SlimeVR Server 中使用 ReboCap</div>
<div style="margin-bottom: 12px">Use ReboCap in SlimeVR Server</div>

<!-- prettier-ignore-end -->

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/colasama/reboslime/master/LICENSE">
    <img src="https://img.shields.io/github/license/colasama/reboslime" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.10.x-blue?logo=python&logoColor=edb641" alt="python">
</p>



## 使用说明

- 下载 `Releases` 中的可执行文件，最新 `v0.4.2` 已适配 Rebocap v40 及以后的版本，如果想要使用之前与 VMT 相配合的程序，请下载 `v0.31` 版本。
- 打开 SlimeVR 服务端。
- 打开 ReboCap 客户端，点击 **动作校准1**。
- 运行 `run.bat` 或者 `reboslime.exe`。
- 现在应该能在 SlimeVR 中看到追踪器了！之后按照 SlimeVR 的用法来就可以了。

## 配置说明 / Configuration

`config.json` 中与 SlimeVR 服务器相关的配置项如下 (SlimeVR server related options in `config.json`):

- `slimevr_ip`: SlimeVR 服务器的 IP 地址，默认为 `127.0.0.1`。当 SlimeVR 服务器运行在另一台主机上（例如虚拟机 / 容器经过 NAT 网络，UDP 广播无法自动发现服务器时），请填写该主机的 IP，即可单播直连。
  IP address of the SlimeVR server (default: `127.0.0.1`). Set this to the server machine's IP when SlimeVR runs on another host — e.g. across a VM/container NAT network where UDP broadcast auto-discovery cannot reach the server — so packets are sent via unicast directly.
- `slimevr_port`: SlimeVR 服务器的 UDP 端口，默认为 `6969`（SlimeVR 标准端口）。
  UDP port of the SlimeVR server (default: `6969`, the SlimeVR standard port).
- 旧版配置项 `slime_ip` / `slime_port` 仍然兼容；两者都未填写时保持原有行为（`127.0.0.1:6969`）。
  The legacy keys `slime_ip` / `slime_port` are still honored; with neither present the previous default (`127.0.0.1:6969`) is used.

配置示例 (Example):

```json
{
    "slimevr_ip": "192.168.1.23",
    "slimevr_port": 6969
}
```

## 开发相关

- 本项目使用 `Poetry` 进行依赖管理，请安装 3.10.x 版本的 Python 后运行 `pip install poetry`。
- 使用 `poetry install` 安装依赖，然后运行 `poetry run python reboslime.py` 即可运行程序。

## 打包相关

- 若要打包本项目为可执行文件，请在安装 `pyinstaller` 后运行以下代码。

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py
  ```

- 在打包完成后，将 `config.json` 放进可执行文件同目录下即可。

## 注意事项

- 由于 ReboCap 客户端自身限制原因，目前必须按照原 VR 使用方法中佩戴胸、腰以及腿部 8 点，并且目前至少佩戴以上 8 个才能正常运行，目前可以在 6 / 8 / 10 / 12 / 15 点中选择。
  - 6 点：胸 + 腰 + 大腿 + 小腿
  - 8 点：胸 + 腰 + 大腿 + 小腿 + 脚
  - 10 点：胸 + 腰 + 大腿 + 小腿 + 脚 + 大臂
  - 12 点：胸 + 腰 + 大腿 + 小腿 + 脚 + 大臂 + 小臂
  - 15 点：全身
- **注意**：目前每一种选择都会出现一个 0 号节点，可以考虑不分配或者分配到 髋部。

## ToDo

- [x] 完成佩戴数量的选择。
- [ ] 解决 15 点模式下头部节点疑似无法使用的问题。

## 感谢

- https://github.com/lmore377/moslime - SlimeVR 网络传输部分，很大程度参考了整个项目的结构
