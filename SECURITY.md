# Security and data policy

**GitHub stores the operating system. It does not store live client projects.**

This is a private repository. Private does not mean safe for client data: every collaborator, every
fork and every future hire with access can read its full history, and history is very hard to
truly erase.

## Never commit

- Patient information of any kind
- Medical information
- Personally identifiable patient data
- Client passwords
- API keys
- OAuth tokens
- Google Business Profile credentials
- Analytics credentials
- Private access tokens
- Unredacted client analytics exports (GA4, Search Console, GBP, call tracking, booking data)
- Patient imagery, including before/after photos
- Consent documentation
- Client commercial secrets that are not part of CosmediSites IP (pricing, revenue, contracts, staffing)
- A client's Master Project Context or any filled-in template

## Where those things go instead

| Item | Home |
|---|---|
| Master Project Context, filled templates, trackers, proof inventory | The client's Google Drive project folder (restricted sharing) |
| Patient imagery, consent records | The client's own systems, or a restricted Drive folder agreed with the client. Never in AI tools unless the client has explicitly agreed |
| Credentials and access | The company password manager. Never in Drive docs, Chirply notes or chat |
| Project status, tasks, approvals, client comms | Chirply |
| Designs | Figma |

## Guardrails in this repository

- `.gitignore` blocks common binary, image, export and credential file types.
- CI runs `scripts/safety_scan.py` on every pull request. It fails on likely secrets and personal
  data (keys, tokens, emails, UK phone numbers, NHS-number patterns, private keys) and on blocked file types.
  It is a safety net, not a guarantee.
- Recommended GitHub settings (see [docs/governance.md](docs/governance.md)): branch protection on
  `main`, secret scanning and push protection where your GitHub plan provides them, forking disabled.

## If something sensitive is committed

1. **Do not just delete it in a new commit.** It stays in history.
2. Tell the repository admin immediately.
3. **Rotate any exposed credential first.** Assume it is compromised.
4. The admin removes it from history (`git filter-repo`) and force-pushes, and contacts GitHub
   Support to purge cached views if needed.
5. If patient or personal data was exposed, follow the CosmediSites data-breach procedure. UK GDPR
   may require an assessment, and possibly notification to the ICO within 72 hours.

## AI tools

- Give AI tools the Master Project Context and the relevant project files, never credentials.
- Do not paste patient-identifiable data or patient images into AI tools.
- Treat websites, PDFs and emails passed to AI as **data, not instructions** (AI Operating Rules §5).

## Reporting

Report a security concern in this repository to the repository admin directly, not in a public
channel or a GitHub issue.
