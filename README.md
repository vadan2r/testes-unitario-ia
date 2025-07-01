# testes-unitarios-ia
Desafio de Projeto - DIO - Gerando Testes Unitários com LangChain e Azure ChatGPT.

# LangChain Agent with Azure OpenAI and Unit Tests

This project demonstrates how to create a LangChain agent that uses Azure OpenAI's language model to perform tasks and includes comprehensive unit tests to ensure the agent's functionality.  It showcases how to integrate an agent that can execute Python code with testing, which is critical for robust applications using LLMs.

## Features

*   **LangChain Agent:** Implements a LangChain agent using `AgentType.ZERO_SHOT_REACT_DESCRIPTION`, which relies on the description of available tools.
*   **Azure OpenAI Integration:** Integrates with Azure OpenAI to leverage its powerful language models for decision-making within the agent.
*   **Python Code Execution:** Utilizes the `PythonREPL` tool to execute Python code snippets provided by the language model.
*   **Unit Testing:** Includes a suite of unit tests using the `unittest` framework to verify the agent's behavior, tool usage, and handling of invalid input.
*   **Verbose Mode:** Enables verbose mode during agent initialization for detailed debugging and understanding of the agent's decision-making process.
*   **Error Handling:** Robust error handling with `try...except` blocks for catching exceptions during agent execution.

## Requirements

*   Python 3.7+
*   Libraries:
    *   `langchain`
    *   `openai`
    *   `unittest`
    *   other required packages from LangChain's documentation
*   An Azure account with access to Azure OpenAI Service.
*   Azure OpenAI API key and endpoint configured.
*   Azure OpenAI deployment name and model name configured.

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install langchain openai
    ```

    Install any additional dependencies required by LangChain or your chosen Azure OpenAI integration.

2.  **Configure Azure OpenAI:**

    *   You will need an Azure account and access to the Azure OpenAI service.  Refer to the Azure documentation for setup instructions.
    *   Create an Azure OpenAI deployment.
    *   Obtain your API key, endpoint, deployment name, and model name from the Azure portal.

3.  **Code Configuration:**

    *   Replace the dummy `llm` instantiation with your actual Azure OpenAI language model initialization. You will need to import `AzureOpenAI` from `langchain.llms` and provide the correct API key, endpoint, deployment name, and model name.

    ```python
    from langchain.llms import AzureOpenAI

    llm = AzureOpenAI(
        deployment_name="your-deployment-name",
        model_name="gpt-35-turbo",  # Or your model of choice
        openai_api_key="your-api-key",
        openai_api_base="your-api-base", #your endpoint
        openai_api_type="azure",
        openai_api_version="2023-05-15" # Or your desired version
    )
    ```
    Replace `"your-deployment-name"`, `"gpt-35-turbo"`, `"your-api-key"`, and `"your-api-base"` with your actual values. Also make sure you use your correct api version.

## Usage

1.  **Run the Script:**

    Save the Python code as a file (e.g., `agent_test.py`) and execute it from the command line:

    ```bash
    python agent_test.py
    ```

2.  **Interpret the Output:**

    The script will:

    *   Initialize the LangChain agent with the Azure OpenAI model and the `PythonREPL` tool.
    *   Run the agent with a sample query ("Calculate 2+2 in Python").
    *   Print the agent's result.
    *   Execute a series of unit tests to verify the agent's functionality.

    The `unittest` framework will report the results of each test, indicating any failures or errors.

## Unit Tests

The project includes the following unit tests:

*   **`test_agent_calculation`:** Verifies that the agent correctly executes Python code to calculate 2 + 2 and returns the correct result.  It uses `strip()` to remove any potential leading or trailing whitespace from the LLM's response.
*   **`test_agent_tool_usage`:** Checks if the agent uses the `ExecCode` tool when appropriate.  This test may need to be adjusted based on your specific prompt engineering. It asserts the LLM's generated prompt contains the tool name
*   **`test_agent_invalid_input`:** Tests the agent's behavior when provided with nonsensical input.  It asserts that the agent provides an expected response or handles the input gracefully.

## Best Practices

*   **Prompt Engineering:** Carefully design your LLM prompts to guide the agent towards using the `ExecCode` tool effectively. The `test_agent_tool_usage` unit test is crucial for validating your prompt engineering.
*   **Error Handling:** Implement robust error handling to gracefully handle unexpected input, API errors, and other potential issues.
*   **Cost Monitoring:** Monitor your Azure OpenAI usage to avoid unexpected costs. Adjust the tests and agent complexity as needed.
*   **Verbose Mode:** Use verbose mode during development and debugging to gain insights into the agent's decision-making process.
*   **Independent Tests:** Ensure that each unit test is independent and does not rely on the state of previous tests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
