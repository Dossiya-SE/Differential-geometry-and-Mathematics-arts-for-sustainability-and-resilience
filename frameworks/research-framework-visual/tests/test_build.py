from framework.render import build


def test_build(tmp_path):
    result = build(spec_path="spec/framework.yaml", outdir=tmp_path)
    assert result["stages"] == 16
    assert result["png_exists"]
    assert result["pdf_exists"]
    assert result["svg_exists"]
    assert (tmp_path / "framework.png").exists()
    assert (tmp_path / "framework.pdf").exists()
    assert (tmp_path / "framework.svg").exists()
