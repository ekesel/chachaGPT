from typing import Union
import re

from langchain.agents import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish

class SimpleOutputParser(AgentOutputParser):
    """
        Parse LLM output into an AgentAction or AgentFinish object.
    """

    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        """
            Parse LLM output into an AgentAction or AgentFinish object.
        """
        final_match = re.search(r"Final Answer\:\s*(.*)", text, flags=re.IGNORECASE | re.DOTALL)
        if final_match:
            final_text = final_match.group(1).strip()
            return AgentFinish({"output": final_text}, text)

        action_match = re.search(r"Action\:\s*(\w+)", text)
        input_match = re.search(r"Action Input\:\s*(.*)", text, flags=re.DOTALL)
        if action_match and input_match:
            tool_name = action_match.group(1).strip()
            tool_input = input_match.group(1).strip()
            return AgentAction(tool=tool_name, tool_input=tool_input, log=text)

        raise ValueError(f"Could not parse LLM output into an action or final answer:\n{text}")
