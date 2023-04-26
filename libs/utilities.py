import os
from pathlib import Path
import uuid


def get_hash():
    return uuid.uuid4().hex


def get_base_dir():
    return Path(__file__).resolve().parent.parent


def get_certs_dir():
    return get_base_dir() / "files" / "output" / "certs"


def ensure_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)
