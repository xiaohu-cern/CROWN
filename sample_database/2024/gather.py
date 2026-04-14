import os
import yaml

# ========= 配置 =========
input_dir = "."   # 改成你的目录
output_file = "merged.yaml"

# 是否缩短 key（强烈推荐 True）
SIMPLIFY_KEY = True

# 要提取的字段
FIELDS = [
    "dbs",
    "era",
    "generator_weight",
    "nevents",
    "nfiles",
    "nick",
    "sample_type",
    "xsec",
]

# ========= 主逻辑 =========
result = {}

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if not (file.endswith(".yaml") or file.endswith(".yml")):
            continue

        filepath = os.path.join(root, file)

        try:
            with open(filepath, "r") as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            nick = data.get("nick")
            if not nick:
                print(f"[Skip] no nick: {filepath}")
                continue

            # ===== 处理 key =====
            if SIMPLIFY_KEY:
                key = nick.split("_Run")[0]
            else:
                key = nick

            key = str(key)  # 🔴 关键：强制字符串，避免 ? key

            # ===== 提取字段 =====
            entry = {}
            for field in FIELDS:
                if field in data:
                    entry[field] = data[field]

            result[key] = entry

        except Exception as e:
            print(f"[Error] {filepath}: {e}")

# ========= 写输出 =========
with open(output_file, "w") as f:
    yaml.safe_dump(
        result,
        f,
        sort_keys=False,
        default_flow_style=False,  # 🔴 防止奇怪格式
        allow_unicode=True
    )

print(f"\n✅ Done! Output written to: {output_file}")