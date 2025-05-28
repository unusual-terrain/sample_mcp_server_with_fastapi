from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
async def app_status_check():
    return {
        "name": "SAMPLE_MCP_SERVER_WITH_FASTAPI",
        "description": "SAMPLE_MCP_SERVER_WITH_FASTAPI",
        "version": "1.0",
        "status": "Running Ok!",
    }
