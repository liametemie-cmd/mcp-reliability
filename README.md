# MCP server reliability — weekly open data by Faceabot

**Which public MCP servers actually work?** Every day, [Faceabot](https://faceabot.com) connects to thousands of public MCP (Model Context Protocol) servers like an AI agent would, and records whether they answer, list their tools and complete a real read-only task. This repository publishes, every Monday, the **100 best-proven servers** and the global figures.

**This week (2026-W42, generated 2026-10-15):** 13,407 public MCP servers measured out of 42,599 in the catalog; **4,342 proven reliable**; 3,165 completed a real task; 161,986 checks in total. On 2026-10-15 (UTC day in progress): 11,929 checks, 96 % success, average answer time 4,416 ms.

### Top 10 this week

| # | Server | Reliability | Real task | Latency |
|---|---|---|---|---|
| 1 | [io.github.PrivateAISystems/needhave](https://faceabot.com/tools/io.github.PrivateAISystems/needhave) | 100 % over 32 checks | proven_working | 2808 ms |
| 2 | [co.bindler/regulatory-calculators](https://faceabot.com/tools/co.bindler/regulatory-calculators) | 100 % over 32 checks | proven_working | 2836 ms |
| 3 | [ai.councilof/gspc-free](https://faceabot.com/tools/ai.councilof/gspc-free) | 100 % over 32 checks | proven_working | 3353 ms |
| 4 | [au.com.ministryofgems/gemmology](https://faceabot.com/tools/au.com.ministryofgems/gemmology) | 100 % over 32 checks | proven_working | 3373 ms |
| 5 | [ai.huntboard/huntboard](https://faceabot.com/tools/ai.huntboard/huntboard) | 100 % over 32 checks | proven_working | 3411 ms |
| 6 | [art.thisisstill/still-mcp](https://faceabot.com/tools/art.thisisstill/still-mcp) | 100 % over 32 checks | proven_working | 3454 ms |
| 7 | [ai.kikaret/mcp](https://faceabot.com/tools/ai.kikaret/mcp) | 100 % over 32 checks | proven_working | 3494 ms |
| 8 | [ai.human4ai/collaboration](https://faceabot.com/tools/ai.human4ai/collaboration) | 100 % over 32 checks | proven_working | 3510 ms |
| 9 | [ai.zdte/market-structure](https://faceabot.com/tools/ai.zdte/market-structure) | 100 % over 32 checks | proven_working | 3531 ms |
| 10 | [br.com.acorridadosbairros/metro-quadrado](https://faceabot.com/tools/br.com.acorridadosbairros/metro-quadrado) | 100 % over 32 checks | proven_working | 3554 ms |

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
