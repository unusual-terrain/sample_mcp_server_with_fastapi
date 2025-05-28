# Sample MCP Server with FastAPI

This repository contains a sample **MCP (Model Context Protocol)** server implemented using **FastAPI**. It demonstrates how to expose tools and resources over MCP using dummy recruitment data such as candidates, jobs, and interviews.

## 🚀 Features

* Streamable HTTP-based MCP server
* Resources (SAMPLE) for:

  * Candidate, Job, and Interview lookup by ID
  * Interview list by date
* Tools for:

  * Creating, updating, deleting candidates
  * Listing candidates
  * Searching candidates by skill
  * Listing interviews by date

---

## 📁 Project Structure

```
project-root/
├── main.py
├── app/
│   ├── mcp/
│   │   └── mcp.py
│   └── datasources/
│       ├── candidates.py
│       ├── job_postings.py
│       └── interviews.py
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:unusual-terrain/sample_mcp_client_with_fastapi.git
cd sample_mcp_client_with_fastapi
```


### 2. Install Dependencies

```bash
uv sync
```


### 3. Run the MCP Server

```bash
make run-dev
```

The server should now be running at `http://127.0.0.1:8000` and MCP endpoint at:

```
http://127.0.0.1:8000/recruit/mcp
```

### 4 . Run the MCP Server in dev mode.

```bash
mcp dev main.py
```

The MCP Inspector will be up and running at http://127.0.0.1:6274

---

## 🧠 How It Works

### `main.py`

* Initializes FastAPI with a lifespan event to manage MCP session
* Mounts the streamable MCP server at `/recruit/mcp`

### `mcp.py`

* Defines:

  * **Resources**: Static access endpoints for candidates, jobs, and interviews
  * **Tools**: Dynamic, callable tools for CRUD operations and filtering

### Example Tool:

```python
@mcp.tool()
def search_candidates_by_skill(skill: str) -> List[Dict]:
    return [c for c in candidates if skill in c["skills"]]
```

### Example Resource:

```python
@mcp.resource("candidate://{candidate_id}")
def get_candidate(candidate_id: str) -> Dict:
    return next((c for c in candidates if c["candidate_id"] == candidate_id), None)
```

---

## 🧪 Testing the Server

You can test your endpoints using:

* **FastAPI Swagger UI**: `http://127.0.0.1:8000/docs`
* **Postman or cURL**: To send HTTP requests
* **Claude Client** (see below)

---

## 🤖 Connecting with Claude Client

If you're using a Claude-powered MCP client:

* Ensure the MCP server is running at the expected URL (`http://0.0.0.0:8000/recruit/mcp`)
* Use `list_tools()` to discover callable tools
* Use Claude's tool-use API to invoke tools dynamically

---

## 🧹 Cleanup

Ensure that you handle session and resource cleanup with `AsyncExitStack` where required. This is built into the lifespan event in `main.py`.

---

## 📌 Notes

* This example uses **in-memory dummy data** in JSON lists. Replace with a database in production.
* MCP tools and resources can be extended easily.
* Claude client must handle `tool_use` responses correctly and loop them into conversation context.

---

## 📄 License

This sample project is licensed under the MIT License.

---

## 🙋 Support

For issues, contact \[[unusual.terrain.9@gmail.com](mailto:unusual.terrain.9@gmail.com)] or raise a GitHub issue.

---

Happy coding! 🎉
