"""SDG Agent specialized in sustainable development goals analysis and alignment."""

import logging
from typing import Dict, List, Optional, Any

from semantic_kernel.agents.azure_ai.azure_ai_agent import AzureAIAgent

from context.cosmos_memory_kernel import CosmosMemoryContext
from .agent_base import BaseAgent

logger = logging.getLogger(__name__)

class SDGAgent(BaseAgent):
    """SDG Agent for analyzing tasks through the lens of UN Sustainable Development Goals."""

    @classmethod
    def default_system_message(cls) -> str:
        """Get the default system message for the SDG Agent."""
        return """You are the UN Sustainable Development Goals (SDG) Agent, specialized in analyzing how tasks, projects, and initiatives align with the 17 SDGs.

Your responsibilities include:
1. Analyzing content for alignment with specific SDGs and their targets
2. Providing SDG impact assessments for proposals and projects
3. Suggesting modifications to better align initiatives with SDG frameworks
4. Identifying potential SDG indicators for measuring progress
5. Connecting initiatives to relevant UN agencies working on specific SDGs

The 17 SDGs are:
1. No Poverty
2. Zero Hunger
3. Good Health and Well-being
4. Quality Education
5. Gender Equality
6. Clean Water and Sanitation
7. Affordable and Clean Energy
8. Decent Work and Economic Growth
9. Industry, Innovation and Infrastructure
10. Reduced Inequalities
11. Sustainable Cities and Communities
12. Responsible Consumption and Production
13. Climate Action
14. Life Below Water
15. Life on Land
16. Peace, Justice and Strong Institutions
17. Partnerships for the Goals

Always frame your analysis using the official UN SDG framework, targets, and indicators. Provide specific references to relevant targets and indicators when possible. Consider interlinkages between SDGs, as progress in one area often affects others."""

    def __init__(
        self,
        agent_name: str = "SDGAgent",
        session_id: str = "",
        user_id: str = "",
        system_message: Optional[str] = None,
        memory_store: Optional[CosmosMemoryContext] = None,
        definition: Optional[AzureAIAgent] = None,
        client: Optional[Any] = None,
        **kwargs,
    ):
        """Initialize a new SDG Agent.

        Args:
            agent_name: The name of the agent
            session_id: The session ID
            user_id: The user ID
            system_message: The system message for the agent
            memory_store: The memory store
            definition: The agent definition
            client: The AI Project client
            **kwargs: Additional parameters for the agent
        """
        if system_message is None:
            system_message = self.default_system_message()

        super().__init__(
            agent_name=agent_name,
            session_id=session_id,
            user_id=user_id,
            system_message=system_message,
            memory_store=memory_store,
            definition=definition,
            client=client,
            **kwargs,
        )

    async def analyze_sdg_alignment(self, project_description: str, sdg_number: Optional[int] = None) -> Dict[str, Any]:
        """
        Analyze how a project aligns with the Sustainable Development Goals.
        
        Args:
            project_description: Description of the project to analyze
            sdg_number: Optional specific SDG number to focus on (1-17)
            
        Returns:
            Analysis result
        """
        if sdg_number:
            prompt = f"""Please analyze the following project for alignment with SDG {sdg_number}:

{project_description}

For SDG {sdg_number}:
1. Identify which specific targets the project addresses
2. Rate the alignment (strong, moderate, weak)
3. Suggest metrics that could be used to measure progress
4. Recommend improvements to strengthen SDG alignment

Provide a concise summary highlighting how the project contributes to SDG {sdg_number}."""
        else:
            prompt = f"""Please analyze the following project for alignment with the UN Sustainable Development Goals:

{project_description}

For each relevant SDG:
1. Identify which specific targets the project addresses
2. Rate the alignment (strong, moderate, weak)
3. Suggest metrics that could be used to measure progress
4. Recommend improvements to strengthen SDG alignment

Provide a concise summary at the end highlighting the primary SDGs addressed."""

        response = await self.completion_with_retry(prompt=prompt)
        return {"analysis": response}
    
    async def suggest_sdg_indicators(self, project_description: str) -> Dict[str, Any]:
        """
        Suggest appropriate SDG indicators for measuring project impact.
        
        Args:
            project_description: Description of the project
            
        Returns:
            Suggested indicators
        """
        prompt = f"""Based on the following project description, suggest appropriate SDG indicators that could be used to measure progress and impact:

{project_description}

For each suggested indicator:
1. Identify the specific SDG and target it relates to
2. Explain why this indicator is appropriate for this project
3. Suggest practical data collection methods
4. Note any potential challenges in measurement"""

        response = await self.completion_with_retry(prompt=prompt)
        return {"indicators": response}
    
    async def identify_un_agencies(self, initiative_description: str) -> Dict[str, Any]:
        """
        Identify relevant UN agencies for a project or initiative.
        
        Args:
            initiative_description: Description of the initiative
            
        Returns:
            List of relevant UN agencies with rationale
        """
        prompt = f"""Based on the following initiative, identify the most relevant UN agencies and entities that could provide support, expertise, or partnership:

{initiative_description}

For each identified agency:
1. Explain their relevance to this initiative
2. Note their specific expertise or resources that would be valuable
3. Suggest potential mechanisms for engagement (e.g., technical assistance, funding, partnership)"""

        response = await self.completion_with_retry(prompt=prompt)
        return {"agencies": response}

    async def process_message(self, message: str) -> str:
        """Process a message using the agent.
        
        Args:
            message: The message to process
            
        Returns:
            The processed message
        """
        # If no specific method is called, default to SDG alignment analysis
        if "analyze" in message.lower() or "alignment" in message.lower() or "sdg" in message.lower():
            result = await self.analyze_sdg_alignment(message)
            return result["analysis"]
        elif "indicator" in message.lower() or "measure" in message.lower() or "metric" in message.lower():
            result = await self.suggest_sdg_indicators(message)
            return result["indicators"]
        elif "agency" in message.lower() or "agencies" in message.lower() or "partner" in message.lower():
            result = await self.identify_un_agencies(message) 
            return result["agencies"]
        else:
            # General SDG-related response
            return await self.completion_with_retry(prompt=message)