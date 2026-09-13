from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add the numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int)->int:
    """_summary_
    Multiply the numbers
    """
    return a*b

if __name__=="__main__":
    mcp.run(transport="stdio")