
URLS = {
    "tokyo_xs": "https://drive.google.com/file/d/15TNQwa-CsUG7ZEyUybXMehxcAmUD-OQF/view?usp=share_link",
    "sf_xs": "https://drive.google.com/file/d/1XzirW9cRwyKlE0IefumeGvEkvcqrsXB-/view?usp=share_link",
    "gsv_xs": "https://drive.google.com/file/d/1A1_Tb4D-0i2WOvr6yOF0ZPQ21dhubxcv/view?usp=share_link"
}

import os
import gdown
import shutil

os.makedirs("data", exist_ok=True)
for dataset_name, url in URLS.items():
    print(f"Downloading {dataset_name}")
    zip_filepath = f"data/{dataset_name}.zip"
    gdown.download(url, zip_filepath, fuzzy=True)
    shutil.unpack_archive(zip_filepath, extract_dir="data")
    os.remove(zip_filepath)

