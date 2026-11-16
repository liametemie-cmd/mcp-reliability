# MCP server reliability — weekly open data by Faceabot

**Which public MCP servers actually work?** Every day, [Faceabot](https://faceabot.com) connects to thousands of public MCP (Model Context Protocol) servers like an AI agent would, and records whether they answer, list their tools and complete a real read-only task. This repository publishes, every Monday, the **100 best-proven servers** and the global figures.

**This week (2026-W47, generated 2026-11-16):** 31,473 public MCP servers measured out of 62,597 in the catalog; **14,939 proven reliable**; 9,233 completed a real task; 565,673 checks in total. On 2026-11-16 (UTC day in progress): 6,035 checks, 87 % success, average answer time 772 ms.

### Top 10 this week

| # | Server | Reliability | Real task | Latency |
|---|---|---|---|---|
| 1 | [com.faceabot/no-transit](https://faceabot.com/tools/com.faceabot/no-transit) | 100 % over 637 checks | proven_working | — ms |
| 2 | [com.faceabot/news](https://faceabot.com/tools/com.faceabot/news) | 100 % over 625 checks | proven_working | 3 ms |
| 3 | [com.faceabot/translate](https://faceabot.com/tools/com.faceabot/translate) | 100 % over 620 checks | proven_working | — ms |
| 4 | [com.faceabot/web-reader](https://faceabot.com/tools/com.faceabot/web-reader) | 100 % over 612 checks | proven_working | 3 ms |
| 5 | [com.faceabot/youtube](https://faceabot.com/tools/com.faceabot/youtube) | 100 % over 606 checks | proven_working | 355 ms |
| 6 | [com.faceabot/transit-norway](https://faceabot.com/tools/com.faceabot/transit-norway) | 100 % over 587 checks | proven_working | — ms |
| 7 | [com.faceabot/rail-ireland](https://faceabot.com/tools/com.faceabot/rail-ireland) | 100 % over 585 checks | proven_working | — ms |
| 8 | [com.faceabot/places](https://faceabot.com/tools/com.faceabot/places) | 100 % over 570 checks | proven_working | 3 ms |
| 9 | [com.faceabot/geocode](https://faceabot.com/tools/com.faceabot/geocode) | 100 % over 568 checks | proven_working | — ms |
| 10 | [com.faceabot/weather](https://faceabot.com/tools/com.faceabot/weather) | 100 % over 557 checks | proven_working | 3 ms |

Full list: [`data/latest/top100.csv`](data/latest/top100.csv)

## Files

| File | Content |
|---|---|
| [`data/latest/top100.csv`](data/latest/top100.csv) / [`.json`](data/latest/top100.json) | The 100 best-proven public MCP servers this week, ranked |
| [`data/latest/summary.json`](data/latest/summary.json) | Global figures: servers in the catalog, measured, proven reliable, checks, failure reasons |
| `data/weekly/<year>-W<week>/` | Frozen weekly snapshots (history) |

Each row has: endpoint, verdict, success rate, number of checks, consecutive successes, last check (UTC), latency, number of tools, whether a **real task** succeeded, and a link to the server's page on Faceabot.

## Method

Each check is an MCP initialize + tools/list from Faceabot (User-Agent FaceabotProbe/1.0) plus, when the server declares a read-only tool (readOnlyHint), one call of that tool with a neutral sample input to check it really returns a result. reliable = ≥95% success over ≥3 checks with ≥3 consecutive successes; requires_authentication = private server, not counted as a failure.

Verdicts: `reliable` = at least 95 % success over at least 3 checks with at least 3 successes in a row; `proven_working` (real task) = a read-only tool returned a real, non-empty result. Private servers that require credentials are not counted as failures. Faceabot does not grade itself: its own status is checked from outside.

## Need a tool for your agent right now?

Ask Faceabot directly — no key, no account:
- MCP server: `https://faceabot.com/api/mcp` (tool `solve_need`)
- HTTP: `https://faceabot.com/resolve?need=send+an+email`
- Best tool by topic: https://faceabot.com/best

## Terms

Free to consult, cite and link, with the attribution **"Reliability data: Faceabot (https://faceabot.com)"**. Bulk copying or redistribution of the Faceabot database is not allowed. See [TERMS.md](TERMS.md).

---

### En français

**Quels serveurs MCP publics marchent vraiment ?** Chaque jour, [Faceabot](https://faceabot.com) se connecte à des milliers de serveurs MCP publics comme le ferait une IA, et note s'ils répondent, listent leurs outils et réussissent une vraie tâche en lecture seule. Ce dépôt publie chaque lundi les **100 serveurs les mieux prouvés** et les chiffres globaux. Données libres à consulter et à citer avec un lien vers faceabot.com ; copie en masse interdite ([TERMS.md](TERMS.md)). Meilleur outil par thème : https://faceabot.com/meilleur
