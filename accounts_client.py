

import mcp
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from agents import FunctionTool
import json
from pydantic import AnyUrl, TypeAdapter
from mcp.types import TextResourceContents, BlobResourceContents
params = StdioServerParameters(command="uv", args=["run", "accounts_server.py"], env=None)


async def list_accounts_tools():
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            tools_result = await session.list_tools()
            return tools_result.tools
        
async def call_accounts_tool(tool_name, tool_args):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, tool_args)
            return result
            
async def read_accounts_resource(name: str):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            uri = TypeAdapter(AnyUrl).validate_python(f"accounts://accounts_server/{name}")
            result = await session.read_resource(uri)
            content = result.contents[0]
            if isinstance(content, TextResourceContents):
                return content.text
            elif isinstance(content, BlobResourceContents):
                return content.model_dump_json()
            else:
                raise TypeError(f"Unexpected resource content type: {type(content)}")

async def read_strategy_resource(name: str):
    async with stdio_client(params) as streams:
        async with mcp.ClientSession(*streams) as session:
            await session.initialize()
            uri = TypeAdapter(AnyUrl).validate_python(f"accounts://accounts_server/{name}")
            result = await session.read_resource(uri)
            content = result.contents[0]
            if isinstance(content, TextResourceContents):
                return content.text
            elif isinstance(content, BlobResourceContents):
                return content.model_dump_json()
            else:
                raise TypeError(f"Unexpected resource content type: {type(content)}")

async def get_accounts_tools_openai():
    openai_tools = []
    for tool in await list_accounts_tools():
        schema = {**tool.inputSchema, "additionalProperties": False}
        openai_tool = FunctionTool(
            name=tool.name,
            description=tool.description,
            params_json_schema=schema,
            on_invoke_tool=lambda ctx, args, toolname=tool.name: call_accounts_tool(toolname, json.loads(args))
                
        )
        openai_tools.append(openai_tool)
    return openai_tools