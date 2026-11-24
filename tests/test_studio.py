import json
import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent / "scripts"))
from render_video import REPO_PRESETS
from generate_audio import generate_hud_audio

def test_repo_presets_integrity():
    required_keys = ["repo_name", "repo_slug", "status_tag", "module_1", "module_2", "module_3", "logs"]
    for slug, preset in REPO_PRESETS.items():
        for k in required_keys:
            assert k in preset, f"Preset {slug} missing key {k}"
        assert len(preset["logs"]) >= 3, f"Preset {slug} has insufficient logs"

def test_template_interpolation(tmp_path):
    template_path = Path(__file__).resolve().parent.parent / "templates" / "dashboard.html.tmpl"
    assert template_path.exists(), "Template file missing"
    content = template_path.read_text(encoding="utf-8")
    
    assert "{{REPO_NAME}}" in content
    assert "{{STATUS_TAG}}" in content
    assert "{{MODULE_1_TITLE}}" in content
    assert "window.seekTo" in content

def test_audio_generator(tmp_path):
    out_audio = tmp_path / "test_cyber_audio.aac"
    generate_hud_audio(duration=2.0, output_path=str(out_audio))
    assert out_audio.exists()
    assert out_audio.stat().st_size > 1000
