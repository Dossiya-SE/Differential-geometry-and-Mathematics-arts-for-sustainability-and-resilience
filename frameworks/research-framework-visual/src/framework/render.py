from .controller import render_release


def build(spec_path=None, outdir='exports'):
    return render_release(request_path='render_requests/Research_Framework_V4.yaml', outdir=outdir)
