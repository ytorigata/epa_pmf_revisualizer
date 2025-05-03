from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# key directories
DATA_DIR = PROJECT_ROOT / 'data'
CONFIG_DIR = DATA_DIR / 'config'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
OUTPUT_IMG_DIR = PROJECT_ROOT / 'output_image'