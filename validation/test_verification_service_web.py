from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = {
    "index.html": ["Qualified testing foundation", "ATMOS LAB", "EPMOS FLAGSHIP", "pages/pricing.html"],
    "pages/verification-service.html": ["Bring us your AI. We attack it before production does.", "MASTER", "Adversarial governance families", "High-volume qualification", "Every outside target must be separately identified"],
    "pages/evidence-testing.html": ["pages/verification-service.html", "Request an AI Authority Test"],
    "pages/projects.html": ["EPMOS VERIFICATION SERVICE", "MASTER", "full mutation detection"],
    "sitemap.xml": ["https://earthspharmacy.org/epmos-new/pages/verification-service.html"],
}

for rel, needles in required.items():
    path = ROOT / rel
    assert path.exists(), f"missing required file: {rel}"
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"{rel} missing required integration marker: {needle}"

page = (ROOT / "pages/verification-service.html").read_text(encoding="utf-8").lower()
for forbidden in ["api key", "secret key", "private prompt:", "exploit payload", "credential="]:
    assert forbidden not in page, f"public page contains forbidden disclosure marker: {forbidden}"

print("verification-service-web-integration: PASS")
