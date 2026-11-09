from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"
PAGES.mkdir(exist_ok=True)

nav = [
    ("Home", "index.html"),
    ("What is EPMOS", "pages/what-is-epmos.html"),
    ("Principles", "pages/principles.html"),
    ("Governed AI", "pages/governed-ai.html"),
    ("GATELESS", "pages/gateless.html"),
    ("Evidence & Testing", "pages/evidence-testing.html"),
    ("Research", "pages/research.html"),
    ("Projects", "pages/projects.html"),
    ("Knowledge", "pages/knowledge.html"),
    ("About", "pages/about.html"),
    ("Contact", "pages/contact.html"),
]

pages = {
    "what-is-epmos": {
        "title": "What is EPMOS?",
        "kicker": "THE GOVERNANCE PROBLEM",
        "intro": "Capability can make an action possible. Governance determines whether that action is authorized.",
        "lede": "EPMOS is a public-facing governance architecture and systems initiative for keeping intelligent capability accountable to evidence, scoped authority, provenance, testing, and human control.",
        "sections": [
            ("The distinction that matters", "An intelligent system may be technically able to perform an action without having permission to perform it. EPMOS treats that distinction as a first-order design concern. A good answer, a reliable tool call, or a successful prior task does not grant permanent authority."),
            ("Why EPMOS exists", "AI systems can reason, write, research, code, access tools, handle records, coordinate workflows, and initiate external actions. As capability grows, the important questions become: Who authorized this? Under what conditions? What evidence supports it? What happens when evidence is missing or the system is wrong? Can the action be reconstructed and can authority be revoked?"),
            ("Public-safe model", "EPMOS describes the requirements and reasons for governed behavior without publishing protected implementation details. Authority should be scoped, granted, enforceable, conditional, and revocable. Consequential actions require stronger controls than ordinary explanation, and uncertainty should remain visible rather than being converted into confidence."),
        ],
        "cards": [("Capability", "What the system can technically do."), ("Authority", "What the system is actually permitted to do."), ("Evidence", "What the available record really establishes."), ("Human control", "Who can grant, limit, review, or revoke authority.")],
    },
    "principles": {
        "title": "EPMOS Principles",
        "kicker": "PUBLIC GOVERNANCE STANDARD",
        "intro": "A governed system is judged by the boundaries it keeps visible, not only by the tasks it completes.",
        "lede": "These principles are public-safe statements of direction. They do not disclose protected formulas, prompts, source code, identity-gate internals, or decision pipelines.",
        "principles": [
            ("CAPABILITY ≠ AUTHORITY", "Technical ability does not create permission."),
            ("AUTHORITY MUST BE EXPLICIT", "Authority is scoped, granted, enforceable, and revocable."),
            ("CONFIDENCE ≠ EVIDENCE", "A confident output is not automatically a supported fact."),
            ("UNCERTAINTY MUST REMAIN VISIBLE", "Missing evidence should produce a visible limit, not a manufactured conclusion."),
            ("FAILURES ARE EVIDENCE", "A failed test becomes material for repair and regression testing."),
            ("HUMANS RETAIN GOVERNING AUTHORITY", "Delegation does not transfer sovereignty."),
            ("PROVENANCE MATTERS", "Sources, records, inferences, and unresolved questions should remain distinguishable."),
            ("HIGHER CONSEQUENCE REQUIRES STRONGER CONTROL", "The control surface should match the potential impact."),
            ("AUTHORITY MUST BE REVOCABLE", "A grant that cannot be reduced or suspended is not accountable delegation."),
            ("MATURITY MUST BE EARNED", "Creation, novelty, or one successful run does not establish maturity."),
            ("SUCCESS DOES NOT ERASE FAILURE HISTORY", "A repaired failure remains part of the system's evidence."),
            ("SYSTEMS SHOULD EXPLAIN WHY", "People should be able to understand why an action was taken, held, escalated, or refused."),
        ],
    },
    "governed-ai": {
        "title": "How Governed AI Works",
        "kicker": "CONCEPTUAL EDUCATION",
        "intro": "From prompt-to-answer to accountable decision discipline.",
        "lede": "The following is a conceptual public illustration. It explains a governed behavioral sequence and does not depict protected EPMOS internal architecture.",
        "flow": ["INPUT / REQUEST", "SOURCE & CONTEXT REVIEW", "AUTHORITY / SCOPE CHECK", "UNCERTAINTY & CONSEQUENCE ASSESSMENT", "DECISION", "EXECUTE / ESCALATE / HOLD / REFUSE", "RECORD / PROVENANCE", "REVIEW / LEARNING"],
        "sections": [
            ("The difference", "A conventional interaction can appear to be request followed by answer. A governed interaction adds questions about source, scope, consequence, uncertainty, and record before it treats an action as ready to execute."),
            ("Decision discipline", "EXECUTE means required conditions are satisfied within verified authority. AUDIBLE describes an authorized alternative when the original path is no longer appropriate. TIMEOUT means a consequential dependency, permission, identity, source, or state is uncertain and the system pauses. REFUSE means the request is outside authority, prohibited, unsafe, or otherwise fails governing conditions."),
            ("The important limit", "This page intentionally explains behavioral categories rather than claiming to expose a complete internal mechanism. Public education should make the boundary understandable without making protected reconstruction possible."),
        ],
    },
    "gateless": {
        "title": "GATELESS",
        "kicker": "EPMOS-GOVERNED PROJECT",
        "intro": "GATELESS is a governed operating environment within the EPMOS ecosystem.",
        "lede": "Its public role is to coordinate complex work while preserving defined authority, accountability, and operational history. The labels below separate documented status from vision and future planning.",
        "status": [("CURRENT PUBLIC STATUS", "LIVING"), ("CURRENT MATURITY STATE", "WORKING"), ("PUBLICLY DESCRIBED ROLE", "Governed project and operating environment"), ("AUTHORITY POSTURE", "Human authority remains defined and gated")],
        "sections": [
            ("What is documented", "GATELESS is presented as an EPMOS-governed intelligent-system project / implementation. Public materials describe its purpose and governance posture, not protected implementation details."),
            ("What this page does not claim", "This page does not claim universal deployment, certification, independent validation, commercial maturity, or authority. Planned features are not presented as current capabilities."),
            ("Lifecycle discipline", "A project can be living and working while still requiring further testing, validation, authorization, and evidence. Creation is not promotion; working is not automatically MASTER."),
        ],
    },
    "evidence-testing": {
        "title": "Evidence & Testing",
        "kicker": "EVIDENCE BEFORE AUTHORITY",
        "intro": "A failed test is not garbage. It becomes evidence.",
        "lede": "EPMOS emphasizes preserved failures, repair, regression testing, and honest limits on what evidence proves. Metrics are not invented where records do not exist.",
        "flow": ["DEFINE", "BUILD", "VERIFY", "ATTACK", "PRESERVE FAILURE", "REPAIR", "RETEST", "WIDEN TESTING", "REPEAT"],
        "sections": [
            ("Testing philosophy", "Mature engineering does not pretend failures did not occur. A useful test record preserves the question, the result, the failure, the repair, the retest, and the limits of the conclusion."),
            ("Evidence categories", "Public materials may distinguish validated results, known failures, repairs, regression tests, and independent validation. Internal testing is not called independent testing, and a successful internal run is not silently converted into external proof."),
            ("Security boundary", "Protected test inputs, exploit details, credentials, private prompts, and architecture-revealing weaknesses are deliberately withheld from the public portal."),
        ],
    },
    "research": {
        "title": "Research Center",
        "kicker": "PUBLIC RESEARCH SURFACE",
        "intro": "A place for public-safe findings, questions, and technical notes to accumulate without overstating certainty.",
        "lede": "The research center is an expandable information architecture. At this stage, it records the categories and evidence posture rather than fabricating papers, dates, or external validation.",
        "cards": [("EPMOS POSITION", "A documented public-safe governance stance."), ("RESEARCH FINDING", "A result supported by an identified investigation."), ("HYPOTHESIS", "A proposition that still requires testing."), ("EXTERNAL SOURCE", "A finding attributable to an outside source."), ("UNRESOLVED QUESTION", "A question retained rather than answered by inference.")],
        "sections": [("Planned collection", "Future public-safe material may include governance studies, AI authority research, provenance research, testing methodology, human/AI delegation research, public presentations, and external validation reports."), ("Publication discipline", "Every item should show a date, version, status, classification, and provenance pointer where practical. No research concept is automatically a released product, and no external validation is claimed without an actual independent party and record."), ("Current state", "The portal architecture is ready for additions. The current public record remains intentionally limited to documented EPMOS positioning and the approved website material available in this repository." )],
    },
    "projects": {
        "title": "Products & Projects",
        "kicker": "EPMOS ECOSYSTEM",
        "intro": "Projects are described by evidence and status, not by presentation alone.",
        "lede": "This page establishes the public profile format for governed systems developed under EPMOS. It avoids private repository topology and does not turn concepts into released products.",
        "projects": [("GATELESS", "Governed operating environment within the EPMOS ecosystem.", "LIVING / WORKING", "Further public validation and documented project evidence are required before stronger maturity claims."), ("EPMOS PUBLIC PORTAL", "Central public knowledge surface for EPMOS principles, evidence, research, and engagement.", "LIVING / WORKING", "The portal is an active implementation and should evolve through reviewed public-safe content." )],
        "sections": [("Standard public profile", "Each future project profile should identify purpose, domain, current public status, current maturity state, current capabilities, what is being tested, known limitations, latest public validation date, and public documentation."), ("Status discipline", "CONCEPT, RESEARCH, PLANNING, LIVING, WORKING, VALIDATION, MASTER, EXPERIMENTAL, PUBLIC DEMONSTRATION, ARCHIVED, and SUPERSEDED are not interchangeable labels. A visual treatment must never imply a higher maturity level than the evidence supports." )],
    },
    "knowledge": {
        "title": "Knowledge Center",
        "kicker": "PUBLIC EDUCATIONAL LIBRARY",
        "intro": "Learn the vocabulary before evaluating the claims.",
        "lede": "The knowledge center is organized so the EPMOS public record can grow by topic, document, project, status, date, and version without collapsing into an unstructured landing page.",
        "glossary": [("EPMOS", "A public-safe governance architecture and systems initiative focused on accountable intelligent capability."), ("GATELESS", "An EPMOS-governed project / operating environment described according to its documented status."), ("Capability", "The technical ability to perform an action."), ("Authority", "Permission to perform an action under defined conditions."), ("Provenance", "The lineage of a statement, record, source, or inference."), ("Evidence", "What the available record actually establishes."), ("Uncertainty", "A meaningful limit or unresolved condition that should remain visible."), ("Escalation", "Moving a decision or action to an authorized human or stronger control."), ("Refusal", "Declining a request because it is outside authority, prohibited, unsafe, or otherwise not governable."), ("Validation", "Evidence that a defined claim or behavior has been tested against stated criteria."), ("Regression test", "A test retained to check that a previously repaired failure does not return."), ("Bounded autonomy", "Delegated action within explicit scope, conditions, and revocation paths.")],
        "faq": [("Is EPMOS an AI model?", "No. EPMOS is presented as a governance architecture and systems initiative, not as a single model."), ("Is EPMOS a chatbot?", "No. A conversational interface could be one surface, but it is not the definition of EPMOS."), ("Does EPMOS eliminate human control?", "No. The public-safe position is that human governing authority remains defined, scoped, and revocable."), ("Can EPMOS make decisions?", "The public record does not authorize a blanket claim of decision-making. Consequential authority requires explicit conditions and evidence."), ("Has EPMOS been independently validated?", "The current public record does not claim independent validation unless a specific external record is published."), ("Is EPMOS commercially available?", "The current public record does not establish broad commercial availability."), ("Why preserve failures?", "Because a failure can become repair and regression evidence instead of disappearing from the record.")],
    },
    "about": {
        "title": "About EPMOS",
        "kicker": "THE INSTITUTIONAL CONTEXT",
        "intro": "EPMOS is an emerging governance architecture and systems initiative.",
        "lede": "The public portal explains the initiative's principles and evidence posture while keeping protected invention architecture outside the public disclosure boundary.",
        "sections": [("A public-safe description", "EPMOS addresses a fundamental problem in advanced AI: capability alone is not authority. Powerful intelligent systems require evidence, boundaries, provenance, accountability, testing, recoverability, and human-governed authority."), ("The Founding Architect", "The Founding Architect may be referenced as the responsible origin point for the initiative. This public site does not invent staff, offices, partnerships, certifications, customers, funding, affiliations, or endorsements."), ("Current maturity", "The website and its public portal implementation are living and working. That status describes an active public implementation; it does not promote the institution or its protected systems to MASTER status." )],
    },
    "contact": {
        "title": "Contact & Engagement",
        "kicker": "CONTROLLED PUBLIC INQUIRY",
        "intro": "Different questions deserve different paths, even when the answer begins with the same boundary: inquiry is not authorization.",
        "lede": "The public portal is prepared for structured engagement without making automatic commitments. A contact submission, when a verified channel is configured, means inquiry received—not agreement, authorization, partnership, representation, investment acceptance, NDA, or contract.",
        "cards": [("GENERAL INFORMATION", "Public orientation and non-sensitive questions."), ("RESEARCHERS / UNIVERSITIES", "Research collaboration and public-safe evidence questions."), ("ENGINEERS", "Technical evaluation within the public disclosure boundary."), ("LEGAL / IP", "Legal or intellectual-property inquiries through an authorized channel."), ("ENTERPRISE / STRATEGIC", "Bounded discussion of public-safe use cases and evaluation."), ("MEDIA / CAPITAL", "Public information requests and carefully bounded interest." )],
        "sections": [("Current contact posture", "No public intake address is asserted here without a verified authorized channel. This prevents the portal from inventing a contact route or implying a commitment that has not been configured."), ("What to include", "When a channel is published, inquiries should identify the audience, topic, requested public-safe material, and whether the question concerns current status, research, evidence, or engagement." )],
    },
}


def link_path(page_dir: bool, target: str) -> str:
    return "../" + target if page_dir else target


def render_nav(page_dir: bool) -> str:
    items = []
    for label, target in nav:
        items.append(f'<a href="{escape(link_path(page_dir, target))}">{escape(label)}</a>')
    return "\n".join(items)


def render_footer(page_dir: bool) -> str:
    return f'''<footer class="site-footer"><div><strong>EPMOS</strong><span>Human-Governed · Traceable · Accountable</span></div><div><span>Public-safe information portal</span><a href="{link_path(page_dir, 'pages/contact.html')}">Contact &amp; engagement</a></div></footer>'''


def render_cards(cards):
    return '<div class="card-grid">' + ''.join(f'<article class="info-card"><span class="card-index">{i+1:02d}</span><h3>{escape(a)}</h3><p>{escape(b)}</p></article>' for i, (a,b) in enumerate(cards)) + '</div>'


def render_sections(sections):
    return '<div class="prose-grid">' + ''.join(f'<article><h2>{escape(a)}</h2><p>{escape(b)}</p></article>' for a,b in sections) + '</div>'


def render_flow(flow):
    return '<div class="flow" aria-label="Conceptual public-safe flow">' + ''.join(f'<div class="flow-step"><span>{i+1:02d}</span><strong>{escape(item)}</strong></div>' for i,item in enumerate(flow)) + '</div>'


def page_shell(title, body, page_dir=True, description=None, page_slug=None):
    css = link_path(page_dir, 'styles.css')
    js = link_path(page_dir, 'site.js')
    canonical = 'https://epmos.tech/' + ('' if title == 'Home' else 'pages/' + (page_slug or title.lower().replace(' ', '-')) + '.html')
    desc = description or 'Public-safe information about EPMOS, governed AI, evidence, authority, provenance, testing, and human control.'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | EPMOS</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)} | EPMOS">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{escape(canonical)}">
<link rel="canonical" href="{escape(canonical)}">
<link rel="stylesheet" href="{css}">
</head>
<body>
<header class="site-header"><a class="brand" href="{link_path(page_dir, 'index.html')}" aria-label="EPMOS home"><span class="brand-mark">E</span><span>EPMOS</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" aria-label="Primary navigation">{render_nav(page_dir)}</nav></header>
<main>{body}</main>
{render_footer(page_dir)}
<script src="{js}" defer></script>
</body>
</html>'''


def page_content(key, data):
    title, kicker, intro, lede = data['title'], data['kicker'], data['intro'], data['lede']
    blocks = [f'<section class="page-hero"><div class="eyebrow">{escape(kicker)}</div><h1>{escape(intro)}</h1><p class="lede">{escape(lede)}</p><div class="status-chip"><span class="status-dot"></span>PUBLIC-SAFE · {"LIVING / WORKING" if key in {"gateless", "projects"} else "EDUCATIONAL PORTAL"}</div></section>']
    if 'flow' in data:
        blocks.append(f'<section class="content-section"><div class="section-label">CONCEPTUAL SEQUENCE</div><h2>Governed behavior keeps the decision path visible.</h2>{render_flow(data["flow"])}</section>')
    if 'cards' in data:
        blocks.append(f'<section class="content-section"><div class="section-label">PUBLIC-SAFE FRAMEWORK</div>{render_cards(data["cards"])}</section>')
    if 'principles' in data:
        blocks.append('<section class="content-section"><div class="section-label">THE PRINCIPLES</div><div class="principle-list">' + ''.join(f'<article><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a,b in data['principles']) + '</div></section>')
    if 'status' in data:
        blocks.append('<section class="content-section"><div class="section-label">DOCUMENTED STATUS</div><div class="status-table">' + ''.join(f'<div><span>{escape(a)}</span><strong>{escape(b)}</strong></div>' for a,b in data['status']) + '</div></section>')
    if 'projects' in data:
        blocks.append('<section class="content-section"><div class="section-label">PUBLIC PROJECT PROFILES</div><div class="project-list">' + ''.join(f'<article><div class="project-top"><h2>{escape(a)}</h2><span class="status-chip">{escape(c)}</span></div><p>{escape(b)}</p><small>{escape(d)}</small></article>' for a,b,c,d in data['projects']) + '</div></section>')
    if 'glossary' in data:
        blocks.append('<section class="content-section"><div class="section-label">GLOSSARY</div><div class="glossary">' + ''.join(f'<div><dt>{escape(a)}</dt><dd>{escape(b)}</dd></div>' for a,b in data['glossary']) + '</div></section>')
    if 'faq' in data:
        blocks.append('<section class="content-section"><div class="section-label">FAQ</div><div class="faq">' + ''.join(f'<details><summary>{escape(a)}</summary><p>{escape(b)}</p></details>' for a,b in data['faq']) + '</div></section>')
    if 'sections' in data:
        blocks.append(f'<section class="content-section"><div class="section-label">EXPLANATION</div>{render_sections(data["sections"])}</section>')
    blocks.append('<section class="portal-note"><strong>Disclosure boundary</strong><p>This portal explains public-safe principles, goals, behavioral standards, evidence posture, and documented status. It does not publish protected formulas, private prompts, controlled source code, credentials, security topology, or material that would enable reconstruction of protected invention architecture.</p></section>')
    return '\n'.join(blocks)


home_body = '''<section class="hero hero-home"><div class="hero-copy"><div class="eyebrow">EPMOS · PUBLIC INFORMATION PORTAL</div><h1>Capability alone is not <em>authority.</em></h1><p class="lede">EPMOS is an emerging governance architecture and systems initiative for intelligent capability that remains accountable to evidence, boundaries, provenance, testing, recoverability, and human-governed authority.</p><div class="hero-actions"><a class="button primary" href="pages/what-is-epmos.html">Understand EPMOS</a><a class="button" href="pages/evidence-testing.html">See the evidence model</a></div><p class="fine">Public overview only. Protected architecture, formulas, private governance mechanisms, credentials, and Founder-locked material are not disclosed here.</p></div><div class="hero-art"><img src="assets/epmos-gateless-logo.jpg" alt="EPMOS Gateless — Engineered Governance Kernel"><span>GATELESS · EPMOS ECOSYSTEM</span></div></section>
<section class="content-section intro-band"><div><div class="section-label">THE QUESTION</div><h2>Can the AI do this? is no longer the only question.</h2></div><p>As systems gain access to tools, records, workflows, and external actions, governance must also ask who authorized an action, what evidence supports it, what happens when evidence is missing, and whether the action can be reconstructed or reversed.</p></section>
<section class="content-section"><div class="section-label">EXPLORE THE PORTAL</div><div class="feature-grid"><a class="feature-card" href="pages/what-is-epmos.html"><span>01</span><h2>What is EPMOS?</h2><p>The difference between capability and authority, in human language first.</p></a><a class="feature-card" href="pages/principles.html"><span>02</span><h2>Principles</h2><p>The public-safe standards that keep confidence, evidence, and human control distinct.</p></a><a class="feature-card" href="pages/governed-ai.html"><span>03</span><h2>Governed AI</h2><p>A conceptual decision sequence: review, scope, assess, decide, record, learn.</p></a><a class="feature-card" href="pages/gateless.html"><span>04</span><h2>GATELESS</h2><p>The EPMOS-governed project, described according to documented status.</p></a><a class="feature-card" href="pages/evidence-testing.html"><span>05</span><h2>Evidence &amp; testing</h2><p>Failure preservation, repair, retest, and honest limits on conclusions.</p></a><a class="feature-card" href="pages/knowledge.html"><span>06</span><h2>Knowledge center</h2><p>A growing glossary and FAQ for researchers, institutions, engineers, and the public.</p></a></div></section>
<section class="content-section split-callout"><div><div class="section-label">THE OPERATING PRINCIPLE</div><h2>Autonomy is not sovereignty.</h2></div><p>Delegated action can be scoped, conditional, expanded, reduced, suspended, and revoked. EPMOS keeps human governing authority visible while intelligent systems operate within defined bounds.</p></section>
<section class="portal-note"><strong>Current public status</strong><p>The portal implementation is <b>LIVING / WORKING</b>. Public claims remain bounded by the evidence actually established. Internal success is not automatically independent validation.</p></section>'''

# The restored homepage is preserved as a known-good baseline and is not regenerated.
for key, data in pages.items():
    (PAGES / f'{key}.html').write_text(page_shell(data['title'], page_content(key, data), page_dir=True, description=data['lede'], page_slug=key), encoding='utf-8')

print(f'Generated {len(pages)} portal pages; preserved the restored homepage.')
