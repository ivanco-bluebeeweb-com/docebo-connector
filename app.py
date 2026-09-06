"""Extension declaration, capabilities, health check for Docebo Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "docebo-connector",
    version="0.1.0",
    display_name="Docebo",
    icon="icon.svg",
    capabilities=["docebo:manage"],
    description="Official Imperal connector for Docebo (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("docebo_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Docebo connection(s) configured." if count else "Not connected yet."
    }
