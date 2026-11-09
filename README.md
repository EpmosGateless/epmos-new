# EPMOS Website

Public-facing EPMOS website.

## Disclosure boundary
This repository is PUBLIC-SAFE presentation material only. Do not place protected ATMOS architecture, Founder-locked formulas, private prompts, credentials, security topology, protected Creation materials, or other restricted system internals here.

## Current homepage
The initial homepage presents:
- EPMOS public positioning
- governance principles
- GATELESS public overview
- evidence/test standard
- explicit limits on what the public test counts prove

## Lifecycle
LIVING / public website implementation. No website content promotes EPMOS, GATELESS, ATMOS, or any suite to MASTER status.

## Public information portal

The site now includes a first public-safe multi-page portal around the restored homepage. It covers What is EPMOS, Principles, How Governed AI Works, GATELESS, Evidence & Testing, Research, Products & Projects, Knowledge Center, About, and Contact & Engagement. Shared navigation, responsive styling, accessibility-conscious focus states, `sitemap.xml`, `robots.txt`, and `404.html` are included.

The portal is **LIVING / WORKING** and remains public-safe. It intentionally does not publish protected formulas, prompts, controlled source code, credentials, private topology, exploit information, or architecture-reconstructing material. Unverified contact endpoints, independent validation, commercial availability, and maturity claims are stated as unresolved rather than invented.

## Provenance and lifecycle records

Source inventory, planning, LIVING, and WORKING records are preserved under `docs/`. The generator script `build_portal.py` makes the static page set reproducible. No material is promoted to MASTER by this implementation.
Deployment retrigger: 2026-08-27

## This repo

Live at https://admin.epmos.tech/epmos-new/, served from Iron
`/var/www/epmos-new/` via the `admin.epmos.tech` nginx site
(`/epmos-new/` location). Also holds `dashboard/` (Founder Dashboard
receipts ledger) and `founder-dashboard/` (product page + demo).

Rules: no phone numbers anywhere — contact goes through a QR code,
never a bare number or bare URL. No price in public copy that has not
been agreed in writing. No gauntlet or qualification numbers on public
surfaces. No invented sales, reach, or engagement.

Related: `EpmosGateless/epmos-homepage` links here as the rebuilt
EPMOS site. `EpmosGateless/earths-pharmacy` holds an older snapshot of
this portal under `site/epmos-new/` (the Earth's Pharmacy copy,
without the dashboard and founder-dashboard sections) — the live admin
portal is this repo, not that snapshot.
