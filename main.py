import contextlib
from fastapi import FastAPI
from app.mcp.mcp import mcp
from app.routers import defaults


# Define application lifespan to manage MCP session lifecycle
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        # Start the MCP session manager during app startup
        await stack.enter_async_context(mcp.session_manager.run())
        yield  # Yield control back to FastAPI after setup

# Initialize FastAPI app with custom metadata
app = FastAPI(
    lifespan=lifespan,
    title="Sample MCP Server with Fast API",
    version="1.0.0",
    description="Sample MCP Server with Fast API running in streamable http",
)

# Mount the MCP streamable HTTP interface at the /recruit endpoint
app.mount("/recruit", mcp.streamable_http_app())
app.include_router(defaults.router)
