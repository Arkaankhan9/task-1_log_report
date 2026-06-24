# Log Report

Parse the Apache-style access log at `/app/access.log` and emit a JSON
summary at `/app/report.json` describing the traffic.

## Output

Write `/app/report.json` containing a single JSON object with exactly
these three keys:

- `total_requests` (integer): the number of non-blank request lines.
- `unique_ips` (integer): the count of distinct client IP addresses
  (the first whitespace-separated field on each line).
- `top_path` (string): the request path that appears most often across
  all `GET`/`POST`/`PUT`/`DELETE`/`HEAD`/`PATCH` requests.

## Success criteria

1. `/app/report.json` exists and is valid JSON.
2. `report.json["total_requests"]` equals the number of non-blank lines in `access.log`.
3. `report.json["unique_ips"]` equals the number of distinct client IPs.
4. `report.json["top_path"]` is the single most-requested path.
