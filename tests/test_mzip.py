import os
from pathlib import Path
from click.testing import CliRunner

from multizip import mzip

def test_get_targets():
    base_dir = Path(os.getcwd(), 'tests', 'sample2')
    result = mzip.get_dirs(base_dir)
    assert len(result) == 3
    assert result[0] == base_dir.joinpath('テスト１')
    assert result[1] == base_dir.joinpath('テスト２')
    assert result[2] == base_dir.joinpath('テスト３')

def test_create_zip(tmp_path):
    result = mzip.create_zip(
        Path('tests', 'sample'),
        Path(tmp_path))
    assert Path(tmp_path, 'sample.zip') == Path(result)
    assert Path(tmp_path, 'sample.zip').exists() == True

def test_cli(tmp_path):
    p1 = Path(os.getcwd(), 'tests', 'sample2')
    p2 = Path(tmp_path)
    runner = CliRunner()
    result = runner.invoke(mzip.cli, [str(p1), '-o', str(p2)])
    assert Path(tmp_path, 'テスト１.zip').exists() == True
    assert Path(tmp_path, 'テスト２.zip').exists() == True
    assert Path(tmp_path, 'テスト３.zip').exists() == True
