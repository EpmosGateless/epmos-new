# EPMOS Website — OAuth Privacy Policy Validation — v0.1

Date: 2026-08-28
Lifecycle: WORKING / VALIDATION EVIDENCE — NOT MASTER
Branch: `working/oauth-privacy-policy-v0.1`
Base: `main` at `336973bda0c116761af9ecd673c71e29f1b89937`

## Governing source consulted
- `00 — PRODUCT RUNTIME AI GOVERNANCE PACKAGE — V1.0 — CANONICAL OPERATING CONTRACT`
- Status: LIVING IMPLEMENTATION STANDARD — NOT FOUNDER-LOCKED CORE.

## Change set
1. Added `pages/privacy.html`.
2. Added privacy URL to `sitemap.xml`.
3. Added homepage footer link to `pages/privacy.html`.

## Public-safe policy coverage
- Public website information.
- Google OAuth authorization metadata and tokens.
- Google Drive delivery artifacts and bounded-use limitation.
- No sale of Google user data.
- No advertising or unrelated profiling use.
- Credential/token protection expectations.
- Retention and audit/provenance handling.
- User revocation and privacy request path.
- Google API Services User Data Policy / Limited Use disclosure.
- Public disclosure boundary; no Founder-Locked mechanisms or credentials disclosed.

## Verification evidence
- Branch is ahead of `main` only; `main` was not modified by these WORKING changes.
- Git comparison shows only the intended privacy page, sitemap entry, and homepage privacy link before this validation record.
- Vercel commit status for `1eb2df692eaea39d3d3757130bd8efb555a5e070` reported `success` with description `Deployment has completed`.
- Canonical privacy URL prepared: `https://epmos.tech/pages/privacy.html`.

## Remaining gate
The privacy URL is not to be represented as live on `epmos.tech` until the WORKING change is explicitly approved for promotion and the production deployment is verified at that canonical URL. MASTER / production remains untouched by this validation record.
