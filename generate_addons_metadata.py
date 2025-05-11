#!/usr/bin/env python3
import os
import hashlib

PLUGIN_DIR = "plugin.video.webshare_filmplayer"
REPO_DIR = "repository.webshare"

def generate_addons_xml():
    addon_xml_path = os.path.join(PLUGIN_DIR, "addon.xml")
    with open(addon_xml_path, "r", encoding="utf-8") as f:
        addon_content = f.read().strip()

    addons_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<addons>\n{addon_content}\n</addons>'
    addons_xml_path = os.path.join(REPO_DIR, "addons.xml")
    with open(addons_xml_path, "w", encoding="utf-8") as f:
        f.write(addons_xml)

    md5_hash = hashlib.md5(addons_xml.encode("utf-8")).hexdigest()
    with open(os.path.join(REPO_DIR, "addons.xml.md5"), "w", encoding="utf-8") as f:
        f.write(md5_hash)

    print("addons.xml a addons.xml.md5 byly úspěšně vytvořeny.")

if __name__ == "__main__":
    generate_addons_xml()
