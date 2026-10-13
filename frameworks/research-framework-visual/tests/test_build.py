from framework.controller import render_release, reproduce_bundle


def test_v4_release_contract(tmp_path):
    qa = render_release('render_requests/Research_Framework_V4.yaml', tmp_path)
    assert qa['final_status'] == 'RENDER_PASS'
    assert all(qa['gates'].values())
    required = [
        'poster_EDITABLE.svg', 'poster_EDITABLE.pptx', 'poster.png', 'poster.pdf',
        'render_request.yaml', 'equations.tex', 'research_data.json',
        'manifest.json', 'qa_report.json', 'SOURCE_BUNDLE.zip'
    ]
    for name in required:
        assert (tmp_path / name).exists(), name
    svg = (tmp_path / 'poster_EDITABLE.svg').read_text(encoding='utf-8')
    assert 'id="stage.validation"' in svg
    assert 'id="uncertainty.tube.visual"' in svg
    assert '<image ' not in svg


def test_source_only_reproduction(tmp_path):
    release = tmp_path / 'release'
    render_release('render_requests/Research_Framework_V4.yaml', release)
    result = reproduce_bundle(release / 'SOURCE_BUNDLE.zip', tmp_path / 'reproduced')
    assert result['pass']
    assert result['svg_hash_match']
    assert result['png_dimensions_match']
