from framework.environment import doctor


def test_core_environment_doctor_passes():
    report = doctor(require_notebook=False)
    assert report["checks"]["python_supported"]
    assert report["checks"]["cairosvg_conversion"]
    assert report["checks"]["pptx_creation"]
    assert report["pass"], report


def test_doctor_reports_platform_identity():
    report = doctor(require_notebook=False)
    assert report["platform"]
    assert report["machine"]
    assert report["python"]
    assert report["sys_executable"]
