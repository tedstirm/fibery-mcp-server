"""
Fibery MCP Server initialization
"""

from . import server
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    #logger.debug("[DEBUG] code changes active! v0.1.33-tbs")
    """Main entry point for the package."""
    asyncio.run(server.main())


__all__ = ["main", "server"]
