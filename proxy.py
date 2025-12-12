from fastmcp import FastMCP

# Create a proxy to your remote FastMCP Cloud server
# FastMCP Cloud uses Streamable HTTP (default), so just use the /mcp URL
mcp = FastMCP.as_proxy(
    "https://vitreous-apricot-swordfish.fastmcp.app/mcp",  # Standard FastMCP Cloud URL
    name="Santanu Server Proxy"
)

if __name__ == "__main__":
    mcp.run()