# Agent Blueprint

## Introduction

Agent Blueprint is a framework that enables you to create and manage your own agents with ease. This blueprint provides the foundation for building custom agents that can be used for various tasks. This README will guide you through the setup process, explain the structure, and help you get started with creating your own agent.

## Installation

To start using Agent Blueprint, follow these steps:

1. **Clone the Repository:**
```
git clone <repository-url>
cd agent-blueprint
```
2. **Create a `.env` File:**
- Duplicate the `.env.sample` file.
- Fill in the required values in the `.env` file.

3. **Set Up a Virtual Environment:**
```
python3 -m venv venv
source venv/bin/activate
```
4. **Install Dependencies:**
```
pip3 install -r requirements.txt
```
5. **Run the Application:**
```
uvicorn main:app --reload
```
6. **Access Agent Blueprint:**
Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Agent Blueprint documentation.

## Agent Configuration

To define your agent, please provide the required details in the `src/static/agent.json` file. This JSON file should include the following information:

- Agent name
- Agent description
- Capabilities
- Color
- Agent URL
- Input and output specifications

Refer to the A2A API schema for guidance on defining input and output formats for your agent.

## Supported API Endpoints

Agent Blueprint provides support for three API endpoints:

1. **Discover API**:
- Endpoint: `/discover`
- Purpose: The Discover API provides information about the agent, including its name, description, capabilities, color, agent URL, and input/output specifications.
- Usage: Use this API to retrieve metadata about the agent.

2. **Execute API**:
- Endpoint: `/execute`
- Purpose: The Execute API is where you implement the core functionality of your agent. It performs the tasks for which the agent is created.
- Usage: Write your agent's logic within the `execute` function in `src/controller/ExecuteController.py`. This is where your agent's operations are executed.

3. **Abort API**:
- Endpoint: `/abort`
- Purpose: The Abort API allows you to stop the execution of a running agent, providing a way to terminate any ongoing tasks.
- Usage: Implement the logic for aborting the agent within the `AbortController` or a relevant controller.

You can also extend the blueprint to include additional APIs as needed for your specific project.


## Creating Your Own Agent

To create your own agent using this blueprint, follow these steps:

1. **Create repo for your agent and commit basic code**
- Go to `agent-blueprint`
- Create Repo for your agent on github
- Switch repo url
```
git remote add origin <Your agent repo url>
```
- Commit code in your repo
```
git add .
git commit -m "Your message"
git push origin main
```

2. **Define Your Agent:**
- Fill in the details of your agent in `src/static/agent.json`.
- Specify the agent's capabilities, colors, and other metadata.

2. **Implement Functionality:**
- Start writing your agent's logic within the `execute` function in `src/controller/ExecuteController.py`.
- Create separate functions in the `src/agent/` directory to perform specific tasks and import them into `ExecuteController.py`.

3. **README.md File:**
- Create a `README.md` file in the root of your project to document your agent.
- Explain what your agent does, its installation steps, the functionality it offers, and how others can work with it to create their own agents.
