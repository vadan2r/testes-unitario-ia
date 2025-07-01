from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools.python.tool import PythonREPL

tools = [
    Tool(name="ExecCode", func=PythonREPL().run, description="Executa código Python")
]

# Assuming 'llm' is your initialized language model from Azure OpenAI
# You will need to replace this with your actual llm object.
# Example:
# from langchain.llms import AzureOpenAI
# llm = AzureOpenAI(deployment_name="your-deployment-name", model_name="gpt-35-turbo", openai_api_key="your-api-key", openai_api_base="your-api-base", openai_api_type="azure")


#Dummy llm (for demonstration purposes - REPLACE THIS WITH YOUR ACTUAL LLM)
class DummyLLM:
    def __call__(self, prompt):
        return "This is a dummy response from the LLM."

llm = DummyLLM()


agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  # Added verbose=True for debugging

try:
    result = agent.run("Calculate 2+2 in Python")
    print(f"Agent Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")


# Unit Tests using unittest:

import unittest

class TestLangchainAgent(unittest.TestCase):

    def test_agent_calculation(self):
        # This test specifically checks if the agent correctly executes the Python code to calculate 2+2.
        expected_output = "Agent Result: 4" # Modify this based on your actual LLM's output formatting
        try:
            result = agent.run("Calculate 2+2 in Python") # Rerun the agent for the test.  Important!
            self.assertEqual(f"Agent Result: {result.strip()}", expected_output) #Strip to remove any leading/trailing whitespaces.
        except Exception as e:
            self.fail(f"Agent run failed with error: {e}")


    def test_agent_tool_usage(self):
        # Check if the agent calls the 'ExecCode' tool to answer question
        # This will likely need adjusting based on your specific LLM prompt engineering
        response = agent.run("What is 5 * 5 in python?")
        self.assertTrue("ExecCode" in response or "ExecCode" in agent.agent.llm_chain.prompt.template, "Agent didn't use ExecCode tool. Check your LLM prompt.")

    def test_agent_invalid_input(self):
      # Test agent behavior with nonsensical input.
      try:
          response = agent.run("Bla bla bla") # Run agent with invalid input
          # Add your assertion here to check how the agent responds to invalid input.
          # For example, you can check for a specific error message or a default response.
          self.assertIn("I do not have the information", response)
      except Exception as e:
          self.fail(f"Agent failed to run with invalid input: {e}")


if __name__ == '__main__':
    unittest.main()