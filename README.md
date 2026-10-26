# MCP server reliability — weekly open data by Faceabot

**Which public MCP servers actually work?** Every day, [Faceabot](https://faceabot.com) connects to thousands of public MCP (Model Context Protocol) servers like an AI agent would, and records whether they answer, list their tools and complete a real read-only task. This repository publishes, every Monday, the **100 best-proven servers** and the global figures.

**This week (2026-W44, generated 2026-10-26):** 22,613 public MCP servers measured out of 48,708 in the catalog; **6,594 proven reliable**; 5,319 completed a real task; 351,976 checks in total. On 2026-10-26 (UTC day in progress): 9,909 checks, 96 % success, average answer time 5,406 ms.

### Top 10 this week

| # | Server | Reliability | Real task | Latency |
|---|---|---|---|---|
| 1 | [com.faceabot/no-transit](https://faceabot.com/tools/com.faceabot/no-transit) | 100 % over 161 checks | proven_working | — ms |
| 2 | [com.faceabot/wikipedia](https://faceabot.com/tools/com.faceabot/wikipedia) | 100 % over 153 checks | proven_working | — ms |
| 3 | [com.faceabot/news](https://faceabot.com/tools/com.faceabot/news) | 100 % over 149 checks | proven_working | — ms |
| 4 | [com.faceabot/translate](https://faceabot.com/tools/com.faceabot/translate) | 100 % over 149 checks | proven_working | — ms |
| 5 | [com.faceabot/web-reader](https://faceabot.com/tools/com.faceabot/web-reader) | 100 % over 138 checks | proven_working | 1 ms |
| 6 | [com.faceabot/x](https://faceabot.com/tools/com.faceabot/x) | 100 % over 135 checks | proven_working | 4217 ms |
| 7 | [com.faceabot/reddit](https://faceabot.com/tools/com.faceabot/reddit) | 100 % over 134 checks | proven_working | 4213 ms |
| 8 | [com.faceabot/service-status](https://faceabot.com/tools/com.faceabot/service-status) | 100 % over 133 checks | proven_working | 2753 ms |
| 9 | [com.faceabot/rail-finland](https://faceabot.com/tools/com.faceabot/rail-finland) | 100 % over 111 checks | proven_working | — ms |
| 10 | [com.faceabot/rail-ireland](https://faceabot.com/tools/com.faceabot/rail-ireland) | 100 % over 111 checks | proven_working | — ms |

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
