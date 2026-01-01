import pathlib

txt_dir = pathlib.Path(".")

for txt_file in txt_dir.glob("*.txt"):
    content = txt_file.read_text()
    new_content = content.replace(".yaml", "")
    if content != new_content:
        txt_file.write_text(new_content)
        print(f"Updated: {txt_file}")
