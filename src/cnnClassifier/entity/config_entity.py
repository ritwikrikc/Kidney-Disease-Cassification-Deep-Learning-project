from dataclasses import dataclass
from pathlib import Path

#dataclass is used to create classes that are primarily used to store data
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path