import utils.session
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 171.64,
    "uptime_pct": 99.428,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 182.35,
    "uptime_pct": 98.049,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 138.19,
    "uptime_pct": 99.133,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 157.16,
    "uptime_pct": 98.727,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 221.98,
    "uptime_pct": 99.34,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 207.49,
    "uptime_pct": 98.808,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 143.65,
    "uptime_pct": 99.186,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 184.63,
    "uptime_pct": 99.101,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 155.97,
    "uptime_pct": 97.171,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 150.63,
    "uptime_pct": 97.596,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 142.93,
    "uptime_pct": 97.214,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 178.55,
    "uptime_pct": 98.22,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 198.86,
    "uptime_pct": 98.248,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 143.49,
    "uptime_pct": 97.689,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 202.05,
    "uptime_pct": 97.218,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 140.3,
    "uptime_pct": 97.204,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 207.85,
    "uptime_pct": 99.386,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 187.83,
    "uptime_pct": 97.211,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 176.95,
    "uptime_pct": 97.238,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 175.38,
    "uptime_pct": 98.14,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 177.67,
    "uptime_pct": 98.416,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 145.36,
    "uptime_pct": 97.277,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 227.7,
    "uptime_pct": 97.356,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 224.95,
    "uptime_pct": 98.4,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 181.5,
    "uptime_pct": 97.828,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 171.86,
    "uptime_pct": 99.353,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 220.06,
    "uptime_pct": 98.44,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 124.67,
    "uptime_pct": 98.738,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 161.06,
    "uptime_pct": 98.599,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 221.42,
    "uptime_pct": 99.482,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 118.64,
    "uptime_pct": 98.38,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 195.08,
    "uptime_pct": 98.431,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 190.95,
    "uptime_pct": 97.293,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 185.5,
    "uptime_pct": 99.218,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 157.91,
    "uptime_pct": 97.845,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 114.37,
    "uptime_pct": 98.256,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
