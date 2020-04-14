import sys, os, click, glob, shutil
from pathlib import Path

@click.command()
@click.argument('pathname')
@click.option('-o', '--output', default=os.getcwd(), help='Specify the output path')
def cli(pathname, output):
    for target in get_dirs(Path(pathname)):
        create_zip(target, output)


def get_dirs(base_dir: Path) -> [Path]:
    return [p for p in base_dir.iterdir() if p.is_dir()]


def create_zip(target_dir: Path, output_dir: Path) -> str:
    """
    create zip archive with all files in target_dir.
    """
    return shutil.make_archive(
        base_name=Path(output_dir, target_dir.name),
        format='zip',
        root_dir=target_dir)
