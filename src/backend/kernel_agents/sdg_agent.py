from typing import List, Optional

import semantic_kernel as sk
from context.cosmos_memory_kernel import CosmosMemoryContext
from kernel_agents.agent_base import BaseAgent
from kernel_tools.sdg_tools import SDGTools
from models.messages_kernel import AgentType
from semantic_kernel.functions import KernelFunction


class SDGAgent(BaseAgent):
    """SDG agent implementation using Semantic Kernel.

    This agent specializes in analyzing projects' alignment with the UN Sustainable Development Goals
    and providing SDG-specific recommendations.
    """

    def __init__(
        self,
        session_id: str,
        user_id: str,
        memory_store: CosmosMemoryContext,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        agent_name: str = AgentType.SDG.value,
        client=None,
        definition=None,
    ) -> None:
        """Initialize the SDG Agent.

        Args:
            session_id: The current session identifier
            user_id: The user identifier
            memory_store: The Cosmos memory context
            tools: List of tools available to this agent (optional)
            system_message: Optional system message for the agent
            agent_name: Optional name for the agent (defaults to "SDGAgent")
            client: Optional client instance
            definition: Optional definition instance
        """
        # Load configuration if tools not provided
        if not tools:
            # Get tools directly from SDGTools class
            tools_dict = SDGTools.get_all_kernel_functions()
            tools = [KernelFunction.from_method(func) for func in tools_dict.values()]

        # Use system message from config if not explicitly provided
        if not system_message:
            system_message = self.default_system_message(agent_name)

        # Use agent name from config if available
        agent_name = AgentType.SDG.value

        super().__init__(
            agent_name=agent_name,
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            client=client,
            definition=definition,
        )

    @staticmethod
    def default_system_message(agent_name=None) -> str:
        """Get the default system message for the agent.
        Args:
            agent_name: The name of the agent (optional)
        Returns:
            The default system message for the agent
        """
        return "You are an SDG analysis expert that helps analyze projects and initiatives for alignment with the UN Sustainable Development Goals. You provide detailed analysis of how projects contribute to specific SDG targets, suggest relevant indicators for measuring impact, identify relevant UN agencies, and offer recommendations for enhancing SDG alignment."

    @property
    def plugins(self):
        """Get the plugins for the SDG agent."""
        return SDGTools.get_all_kernel_functions()

    # Explicitly inherit handle_action_request from the parent class
    async def handle_action_request(self, action_request_json: str) -> str:
        """Handle an action request from another agent or the system.

        This method is inherited from BaseAgent but explicitly included here for clarity.

        Args:
            action_request_json: The action request as a JSON string

        Returns:
            A JSON string containing the action response
        """
        return await super().handle_action_request(action_request_json)