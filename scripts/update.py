#!/usr/bin/env python3
"""Weekly snapshot of Faceabot's public reliability sample (top 100) and global figures.
Source: https://faceabot.com — only data that faceabot.com already publishes. No bulk copy."""
import csv, json, os, urllib.request, datetime

UA = {"User-Agent": "faceabot-open-data/1.0 (+https://github.com/liametemie-cmd/mcp-reliability)",
      "x-faceabot-test": "1", "Accept": "application/json"}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)

feed = get("https://faceabot.com/api/reliability-feed.json?w=" + datetime.datetime.now(datetime.timezone.utc).strftime("%G-W%V-%u"))
report = get("https://faceabot.com/api/report")
now = datetime.datetime.now(datetime.timezone.utc)
week = now.strftime("%G-W%V")

servers = sorted(feed["servers"], key=lambda s: (-(1 if (s.get("work") or {}).get("verdict") == "proven_working" else 0), -(s.get("successRate") or 0), -(s.get("consecutiveSuccesses") or 0), s.get("lastLatencyMs") or 10**9))
rows = []
for i, s in enumerate(servers, 1):
    w = s.get("work") or {}
    rows.append({
        "rank": i, "id": s["id"], "endpoint": s.get("url"), "verdict": s.get("verdict"),
        "success_rate": s.get("successRate"), "checks": s.get("attempts"),
        "consecutive_successes": s.get("consecutiveSuccesses"),
        "last_checked_at": s.get("lastCheckedAt"), "last_latency_ms": s.get("lastLatencyMs"),
        "tools_advertised": s.get("toolsAdvertised"), "real_task": w.get("verdict"),
        "real_task_success_rate": w.get("successRate"), "faceabot_page": s.get("page"),
    })

c, t = report.get("catalog", {}), report.get("today", {})
summary = {
    "week": week, "generated_at": now.isoformat(timespec="seconds"),
    "source": "https://faceabot.com", "attribution": "Reliability data: Faceabot (https://faceabot.com)",
    "catalog": {k: c.get(k) for k in ["total", "remote", "measured", "reliable", "workTested", "provenWorking", "runsTotal"]},
    "last_day": {k: t.get(k) for k in ["day", "checks", "successRate", "serversChecked", "avgLatencyMs"]},
    "failure_reasons_last_day": t.get("failureReasons", []),
    "method": feed.get("method"), "scope": feed.get("scope"),
    "terms": "https://faceabot.com/conditions",
}

def write(folder):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "top100.json"), "w") as f:
        json.dump({"week": week, "generated_at": summary["generated_at"], "attribution": summary["attribution"],
                   "method": summary["method"], "servers": rows}, f, indent=1, ensure_ascii=False)
    with open(os.path.join(folder, "top100.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
    with open(os.path.join(folder, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1, ensure_ascii=False)

write("data/latest")

# README : chiffres de la semaine et top 10, régénérés à chaque passage
def pct(x): return "—" if x is None else f"{round(x*100)} %"
cat = summary["catalog"]; ld = summary["last_day"]
top10 = "\n".join(f"| {r['rank']} | [{r['id']}]({r['faceabot_page']}) | {pct(r['success_rate'])} over {r['checks']} checks | {r['real_task'] or '—'} | {r['last_latency_ms'] or '—'} ms |" for r in rows[:10])
stats = f"""**This week ({week}, generated {summary['generated_at'][:10]}):** {cat['measured']:,} public MCP servers measured out of {cat['total']:,} in the catalog; **{cat['reliable']:,} proven reliable**; {cat['provenWorking']:,} completed a real task; {cat['runsTotal']:,} checks in total. On {ld['day']} (UTC day in progress): {ld['checks']:,} checks, {pct(ld['successRate'])} success, average answer time {ld['avgLatencyMs']:,} ms.

### Top 10 this week

| # | Server | Reliability | Real task | Latency |
|---|---|---|---|---|
{top10}

Full list: [`data/latest/top100.csv`](data/latest/top100.csv)"""
tpl = open("README.template.md").read()
open("README.md", "w").write(tpl.replace("<!-- STATS -->", stats).replace("<!-- METHOD -->", summary["method"] or ""))
write(os.path.join("data", "weekly", week))
print("ok", week, len(rows), "servers")
