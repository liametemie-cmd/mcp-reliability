# MCP server reliability — weekly open data by Faceabot

**Which public MCP servers actually work?** Every day, [Faceabot](https://faceabot.com) connects to thousands of public MCP (Model Context Protocol) servers like an AI agent would, and records whether they answer, list their tools and complete a real read-only task. This repository publishes, every Monday, the **100 best-proven servers** and the global figures.

**This week (2026-W43, generated 2026-10-19):** 19,556 public MCP servers measured out of 44,737 in the catalog; **5,333 proven reliable**; 3,653 completed a real task; 228,972 checks in total. On 2026-10-19 (UTC day in progress): 9,542 checks, 93 % success, average answer time 7,401 ms.

### Top 10 this week

| # | Server | Reliability | Real task | Latency |
|---|---|---|---|---|
| 1 | [ai.contextstudios/mcp](https://faceabot.com/tools/ai.contextstudios/mcp) | 100 % over 42 checks | proven_working | 4816 ms |
| 2 | [com.deployedbyai/the-deploy-log](https://faceabot.com/tools/com.deployedbyai/the-deploy-log) | 100 % over 42 checks | proven_working | 4865 ms |
| 3 | [ai.deepdna/knowledge](https://faceabot.com/tools/ai.deepdna/knowledge) | 100 % over 42 checks | proven_working | 4919 ms |
| 4 | [ai.clearvoyance/clearvoyance](https://faceabot.com/tools/ai.clearvoyance/clearvoyance) | 100 % over 42 checks | proven_working | 4931 ms |
| 5 | [ai.human4ai/collaboration](https://faceabot.com/tools/ai.human4ai/collaboration) | 100 % over 42 checks | proven_working | 4934 ms |
| 6 | [ai.dripmetrics/mcp](https://faceabot.com/tools/ai.dripmetrics/mcp) | 100 % over 42 checks | proven_working | 4986 ms |
| 7 | [club.worldorder/cube-playground](https://faceabot.com/tools/club.worldorder/cube-playground) | 100 % over 42 checks | proven_working | 5001 ms |
| 8 | [ai.justautomate/website](https://faceabot.com/tools/ai.justautomate/website) | 100 % over 42 checks | proven_working | 5025 ms |
| 9 | [ai.councilof/gspc](https://faceabot.com/tools/ai.councilof/gspc) | 100 % over 42 checks | proven_working | 5030 ms |
| 10 | [com.animatemytravel/studio](https://faceabot.com/tools/com.animatemytravel/studio) | 100 % over 42 checks | proven_working | 5030 ms |

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
