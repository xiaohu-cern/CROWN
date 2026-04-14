import os
import yaml
import shutil

# ========= 配置 =========
input_dir = "."   # 改成你的目录
BACKUP = True  # 是否备份

# ========= 主逻辑 =========
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

            if "era" in data:
                old_era = data["era"]

                # 🔴 关键：用整数，不是字符串
                data["era"] = 2024

                if BACKUP:
                    shutil.copy(filepath, filepath + ".bak")

                with open(filepath, "w") as f:
                    yaml.safe_dump(
                        data,
                        f,
                        sort_keys=False,
                        default_flow_style=False,
                        allow_unicode=True
                    )

                print(f"[Updated] {filepath}: {old_era} -> 2024")

            else:
                print(f"[Skip] no era field: {filepath}")

        except Exception as e:
            print(f"[Error] {filepath}: {e}")

print("\n✅ Done!")