# Agent Plugins

One plugin marketplace that brings together plugins from several repositories. Add it once and you get every plugin below. Each plugin is fetched straight from its own repository at an exact, reviewed commit.

```bash
# Claude Code
/plugin marketplace add Marinski/agent-plugins
/plugin install code-quality-skills@marinski-plugins

# GitHub Copilot CLI
copilot plugin marketplace add Marinski/agent-plugins
```

```jsonc
// VS Code settings.json (GitHub Copilot agent plugins)
"chat.plugins.marketplaces": ["Marinski/agent-plugins"]
```

## What's included

A **plugin** is a bundle of skills. Add the marketplace once and every plugin below is available; each is fetched from its own repository at the exact commit pinned in [`sources.lock.json`](./sources.lock.json). Install only the ones you want — every installed plugin's skill and agent descriptions load into every session (see [Cost](#cost)). Some plugins cover the same ground; those overlaps are called out in [Overlaps between plugins](#overlaps-between-plugins).

Each heading below is one source repository and the ref it is tracked at.

### [Marinski/ClaudeSkills](https://github.com/Marinski/ClaudeSkills) · `master`

General-purpose skill bundles.

- **document-skills** — Create, edit, and analyse Excel spreadsheets, PowerPoint decks, and PDFs.
- **development-skills** — Playwright web-app testing, MCP server development, D3.js data visualisation, and REST/GraphQL API design.
- **database-skills** — Writing, optimising, and schema-designing SQL for PostgreSQL, MySQL, SQLite, and SQL Server.
- **devops-skills** — Docker containerisation workflows plus environment and secrets configuration.
- **code-quality-skills** — Advanced Git operations, automated code review, and systematic debugging with the TRACE framework.
- **communication-skills** — Brand-guideline enforcement, internal-communications templates, and professional Markdown docs.

### [Marinski/ai-enablement-prompts](https://github.com/Marinski/ai-enablement-prompts) · `main`

Marinski's AI-enablement prompts, packaged as installable plugins.

- **creating-prompts** — Authoring new agent skills for Claude Code and VS Code Copilot.
- **figma-from-code** — Rebuild a Figma design system from a running web app's codebase.
- **implement-workflow** — End-to-end feature implementation: design, build, test, self-review through a code-reviewer agent, then prep a PR.
- **code** — Baseline planning, spec, and codebase-understanding skills for any codebase and stack.
- **react** — React component patterns: modlet structure, component extraction, a registry, reuse, and validation.
- **react-mock** — Mock data and data-model patterns for Zod-based React apps.
- **figma-react** — Full Figma-to-React lifecycle: design analysis, component implementation, visual sync, and Code Connect mapping (requires Figma MCP).
- **playwright** — Playwright QA workflows: E2E testing, debugging, responsive verification, visual diffing, and pixel-perfect orchestration (requires Playwright MCP).
- **trpc-prisma** — Type-safety patterns for tRPC + Prisma monorepos (AppRouter type inference, package templates).

### [Marinski/agency-agents](https://github.com/Marinski/agency-agents) · `plugins`

Eighteen "agency" divisions, each a large pool of specialist agent personas. These are the biggest token cost, so install a division only when you want its whole roster.

- **agency-academic** — Academic division (6 specialists).
- **agency-design** — Design division (10 specialists).
- **agency-engineering** — Engineering division (64 specialists).
- **agency-finance** — Finance division (5 specialists).
- **agency-game-development** — Game-development division (21 specialists).
- **agency-gis** — GIS division (13 specialists).
- **agency-healthcare** — Healthcare division (3 specialists).
- **agency-marketing** — Marketing division (36 specialists).
- **agency-paid-media** — Paid-media division (7 specialists).
- **agency-product** — Product division (5 specialists).
- **agency-project-management** — Project-management division (7 specialists).
- **agency-research** — Research division (1 specialist).
- **agency-sales** — Sales division (9 specialists).
- **agency-security** — Security division (12 specialists).
- **agency-spatial-computing** — Spatial-computing division (6 specialists).
- **agency-specialized** — Specialized division (59 specialists).
- **agency-support** — Support division (6 specialists).
- **agency-testing** — Testing division (9 specialists).

### [jakubkrehel/skills](https://github.com/jakubkrehel/skills) · `main`

- **interfaces** — Product-interface craft: typography, colour, layout, accessibility, UI polish, and UX writing.

### [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman) · `main`

- **caveman** — A terse "caveman" writing style; cuts filler, keeps technical detail explicit.

### [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) · `main`

Anthropic's legal skill packs.

- **commercial-legal** — Reviews vendor agreements, NDAs, and SaaS subscriptions against your sales- or purchasing-side playbook; tracks renewal/cancel-by deadlines and routes approvals.
- **privacy-legal** — Triage of processing activities, PIAs, controller/processor DPA review, DSAR responses, and policy-drift monitoring.
- **product-legal** — Launch risk review, quick "is this a problem?" answers, and substantiation checks on marketing claims.
- **corporate-legal** — M&A diligence with cited tabular review, disclosure schedules, board consents/minutes, and entity-compliance deadlines.
- **employment-legal** — Hire/termination risk flags, worker classification, leave deadlines, internal investigations, and policy drafting.
- **regulatory-legal** — Monitors regulatory feeds, diffs new rules against policy, tracks comment deadlines, and writes the weekly digest.
- **ai-governance-legal** — AI use-case triage, impact assessments, vendor AI-term review, and keeping the AI policy current.
- **litigation-legal** — Runs the litigation portfolio and its work product: matters, deadlines, claim charts, chronologies, depo prep, privilege logs, and briefs.
- **law-student** — Socratic drilling, case briefs, outlines, bar prep, IRAC grading, and study planning.
- **legal-clinic** — Clinic setup, student onboarding, structured intake, deadline tracking, and semester handoff.
- **legal-builder-hub** — Finds, evaluates, and installs community legal skills behind a security-review gate.
- **ip-legal** — Trademark clearance, freedom-to-operate triage, patentability screening, cease-and-desist/DMCA, open-source compliance, and IP clauses.
- **cocounsel-legal** — CoCounsel Legal: Westlaw Deep Research reports with inline, linked Westlaw and Practical Law citations.

### [mattpocock/skills](https://github.com/mattpocock/skills) · `main`

- **mattpocock-skills** — Matt Pocock's engineering skills for real work: grilling, spec/ticket flows, TDD, code review, domain modelling, and more.

### [Marinski/wordpress-skills](https://github.com/Marinski/wordpress-skills) · `main`

- **wordpress-platform** — WordPress core and operations: hooks, coding/documentation standards, installation/migration/staging, multisite, content modelling (CPTs, taxonomies, meta), options and transients, wpdb and custom tables, performance, and security hardening.
- **wordpress-development** — Building on WordPress: plugin development (lifecycle hooks, admin menus, Settings API, shortcodes, AJAX, cron, i18n, release workflow), theme development (classic and block themes, template hierarchy, theme.json, patterns, Customizer, accessibility), and REST API integration.
- **wordpress-content-sync** — Bidirectional content sync over the WP REST API with Application Passwords: pull posts/pages as markdown, push approved drafts, resolve taxonomies, upload media, and manage SEO meta (Yoast/RankMath).

### [algotradingspace-dev/metatrader-skills](https://github.com/algotradingspace-dev/metatrader-skills) · `main`

- **mql5-development** — End-to-end MQL5 Expert Advisor development: 5-layer architecture, risk engine, signal generation (SMC/ICT, indicators, multi-timeframe), regime detection, and trade lifecycle.
- **metatrader-platform** — MetaTrader 4/5 operations, the MetaTrader5 Python package, and the mt5-httpapi REST bridge.
- **metatrader-research** — Backtest methodology and performance analytics: Strategy Tester setup, walk-forward and Monte Carlo, overfitting detection, Sharpe/Calmar/Profit Factor/drawdown, and HTML-report parsing.
- **mt5-httpapi** — REST access to a running mt5-httpapi bridge: market data, orders, positions, history, and server-side technical analysis.
- **mql-developer** — Broad MQL4/MQL5 language and platform reference covering syntax, OOP/EA patterns, indicators and UI panels, WebRequest/REST, the tester, licensing, and MQL4-to-MQL5 migration (vendored from ThomasPraun's MQL library).
- **trading-fundamentals** — Forex macroeconomic reference: CPI, GDP, NFP, PMI, rate decisions, employment, trade balance and more, with trading context per currency.
- **trading-web-systems** — TypeScript/React fintech engineering: decimal-safe money maths, trading metrics, WebSocket feeds on Cloudflare Durable Objects, live-price hooks, trading dashboards, and OHLCV ingestion.

### [pskoett/pskoett-ai-skills](https://github.com/pskoett/pskoett-ai-skills) · `main`

- **pskoett-ai-skills** — A two-loop engineering pipeline. Inner loop: plan-interview, intent-framed-agent, context-surfing, verify-gate, self-healing, simplify-and-harden. Outer loop: learning-aggregator, harness-updater, eval-creator, pre-flight-check.

### [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) · `main`

- **andrej-karpathy-skills** — Behavioural guidelines that cut common LLM coding mistakes: think before coding, simplicity first, surgical changes, goal-driven execution.

### [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · `main`

- **marketing-skills** — 50 marketing skills for technical marketers and founders:
  - *Conversion & growth* — `cro`, `ab-testing`, `analytics`, `attribution`, `popups`, `signup`, `onboarding`, `paywalls`, `churn-prevention`, `referrals`, `lead-magnets`, `free-tools`.
  - *Copy, content & channels* — `copywriting`, `copy-editing`, `content-strategy`, `social`, `video`, `image`, `ad-creative`, `community-marketing`, `co-marketing`, `events`.
  - *SEO & discovery* — `seo-audit`, `ai-seo`, `schema`, `programmatic-seo`, `site-architecture`, `competitors`, `competitor-profiling`, `directory-submissions`, `aso`.
  - *Paid ads & outbound* — `ads`, `cold-email`, `prospecting`, `emails`, `sms`, `influencer-marketing`, `public-relations`.
  - *Strategy, pricing & revenue* — `marketing-plan`, `marketing-ideas`, `marketing-loops`, `marketing-psychology`, `marketing-council`, `offers`, `pricing`, `product-marketing`, `customer-research`, `revops`, `sales-enablement`, `launch`.

### [Marinski/graph-plugins](https://github.com/Marinski/graph-plugins) · `main`

Wrappers for two code knowledge-graph tools that don't ship their own marketplace. Both leave out the upstream hooks, so Claude Desktop can copy them to SSH hosts. Each needs its upstream CLI installed on every machine where you use it.

- **graphify** — The `/graphify` skill from [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify): turns code, docs, papers, images or videos into a queryable knowledge graph (`graph.html`, `graph.json`, `GRAPH_REPORT.md`). Requires `uv tool install graphifyy`.
- **codegraph** — The MCP server from [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph): a pre-indexed, local code graph queried with `codegraph_explore`. Requires `npm i -g @colbymchenry/codegraph` and `codegraph init` per project. Telemetry is off for the MCP server.

### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) · `main`

- **ponytail** — YAGNI coding style: before writing, stop at the first rung that holds (does it need to exist, already in the codebase, the standard library, a platform feature, an installed dependency, one line, then the minimum that works). Cuts code, cost and tokens; never cuts validation, error handling, security or accessibility. Adds `/ponytail`, `/ponytail-review`, `/ponytail-audit` and `/ponytail-debt`.

### Overlaps between plugins

Sources are independent and the marketplace does **not** de-duplicate skills across plugins, so a few plugins cover the same ground. Installing both loads duplicate descriptions into every session, which costs tokens and can make the agent pick either one at random. The overlaps worth knowing:

- **Marketing** — `marketing-skills` overlaps heavily with the agency `agency-marketing` (36) and `agency-paid-media` (7) divisions, and partly with `agency-sales` (`sales-enablement`) and `agency-product` (`product-marketing`). Choose one side rather than both.
- **Frontend & Figma** — `figma-from-code` (code → Figma) and `figma-react` (Figma → React) are two halves of the same Figma workflow; `react`, `react-mock`, and `trpc-prisma` overlap each other and the frontend skills inside `development-skills` and `agency-engineering`.
- **QA & testing** — `playwright` overlaps `development-skills` (bundles Playwright testing) and `agency-testing`.
- **Engineering workflow** — `implement-workflow`, `code`, `mattpocock-skills`, and `pskoett-ai-skills` all span planning → spec/tickets → implement → review/TDD; `code-quality-skills` (review, debugging), `andrej-karpathy-skills` (coding-behaviour rules), and `ponytail` (lazy/YAGNI coding and review) cover the same territory.
- **Design & UI** — `interfaces` overlaps `agency-design` and the design/UI specialists inside `agency-specialized`.
- **MetaTrader** — `mql5-development` and `mql-developer` both cover MQL EA development (the latter is the broader reference); `metatrader-platform` already documents `mt5-httpapi`; `trading-web-systems` overlaps `react`/`code` on the web side.
- **WordPress** — `wordpress-platform` and `wordpress-development` split core/ops from plugin/theme/REST but both touch core and the REST API; `wordpress-content-sync` stands alone.
- **Legal** — `legal-builder-hub` is a meta-installer for other legal skills; `cocounsel-legal` (Westlaw research) complements `litigation-legal`, `regulatory-legal`, and `ip-legal`; the niche packs overlap on contract review (`commercial-legal`/`product-legal`) and on data/AI terms (`privacy-legal`/`ai-governance-legal`).
- **Writing & tone** — `caveman` overlaps `communication-skills` and `copy-editing`.
- **Code graphs** — `graphify` and `codegraph` both index a codebase into a graph and both tell the agent to query it before grep or file reads. Pick one per project to avoid conflicting guidance.

### Cost

Install only what you need: every installed plugin's skill and agent descriptions are loaded into each session. The large agency divisions cost the most, for example about 12k tokens for `agency-engineering` and 10.6k for `agency-specialized`, compared with about 0.5k for `document-skills`. Run `claude plugin details <name>` to see a plugin's cost.

## Updating your local copy

Every plugin is pinned to an exact commit, so a new release — a merged [pin update](#keeping-it-up-to-date), or a newly added source such as `marketing-skills` — does not reach you until you refresh your client's catalogue and update the plugin.

**Claude Code**

```bash
claude plugin marketplace update marinski-plugins   # re-fetch the catalogue
claude plugin update marketing-skills               # update one plugin; restart to apply
```

In a session, the equivalents are `/plugin marketplace update marinski-plugins` and `/plugin update marketing-skills`.

**GitHub Copilot CLI**

```bash
copilot plugin marketplace update marinski-plugins  # re-fetch the catalogue (alias: refresh)
copilot plugin update marketing-skills              # or `--all` for every installed plugin
```

In a session, `/plugin marketplace update marinski-plugins`, or press `R` in the `/plugin` marketplace view.

**VS Code** (Copilot Chat agent plugins): registered marketplaces are re-read when the window reloads. Open the `/plugin` dashboard; it flags installed plugins with a newer upstream version and offers an update.

**A local clone of this repo** just needs `git pull` — the pins and the generated manifest are committed, so your clone matches what clients fetch.

## How it works

Nothing is copied or vendored, and there are no submodules. The repo holds three files that matter:

| File | Edited by | Purpose |
|------|-----------|---------|
| `sources.json` | you | Which repos to include, which branch or tag each one tracks, and optional filters |
| `sources.lock.json` | the update workflow | The exact commit each source is pinned to |
| `.claude-plugin/marketplace.json` | generated | One entry per upstream plugin, whose `source` points at the upstream repo at the pinned commit (`url` or `git-subdir` source with `sha`, fetched over https) |

`scripts/build_marketplace.py` reads each upstream's own `.claude-plugin/marketplace.json` at the pinned commit and rewrites every plugin's relative source into a pinned remote source. New plugins that appear upstream are picked up automatically at the next pin update. `.github/plugin/marketplace.json` is a symlink to the same file, for Copilot tools.

## Keeping it up to date

- **`update-pins.yml`** runs daily and on demand. It moves each pin to the tip of its tracked ref, regenerates the manifest, validates it, installs every plugin from its new pin, and then opens (or refreshes) **one PR** listing what moved, with a compare link per upstream. Merging that PR publishes the update; until then, users keep getting the old pins.
- **`check.yml`** runs on every PR and push. It fails if the manifest isn't exactly what the sources and pins generate, if Claude Code's validator rejects it, or if any plugin fails to install or registers nothing.

**Setup for the update workflow:**
- Turn on *Settings → Actions → General → Allow GitHub Actions to create and approve pull requests*.
- Optionally add a `PIN_UPDATE_TOKEN` secret (a fine-grained PAT or GitHub App token with contents and pull-requests write on this repo). This lets `check.yml` also run on the bump PRs, since PRs opened with the default token don't trigger workflows. The update workflow runs the same checks itself either way.

## Adding or changing a source

Edit `sources.json`:

```jsonc
{
  "id": "my-repo",                                  // unique short name
  "repo": "https://github.com/owner/my-repo.git",   // any git URL
  "ref": "main",                                    // branch or tag to track
  "prefix": "my-",                                  // optional: prefix plugin names to avoid clashes
  "include": ["plugin-a"],                          // optional: only these plugins
  "exclude": ["plugin-b"],                          // optional: skip these plugins
  "manifest": ".claude-plugin/marketplace.json",    // optional: upstream manifest path
  "enabled": false                                  // optional: keep but skip
}
```

The source repo must have its own plugin marketplace manifest. Then pin it, regenerate, and check:

```bash
python3 scripts/build_marketplace.py --update   # pin every source to its ref's tip + regenerate
python3 scripts/build_marketplace.py            # regenerate from the current pins only
claude plugin validate ./
./scripts/smoke-test-plugins.sh                 # or pass plugin names to test a subset
```

Two sources can't publish the same plugin name; the build stops and asks for a `prefix`.

## Compatibility

Pinned remote sources (`url` and `git-subdir` with `sha`) are tested with Claude Code: CI installs every plugin this way. VS Code and Copilot CLI read the same manifest format, but check that your version supports `git-subdir` sources before relying on it there.
