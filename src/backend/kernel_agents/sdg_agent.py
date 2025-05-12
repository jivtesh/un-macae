# src/backend/kernel_agents/sdg_agent.py

import logging
from typing import Dict, List

from .agent_base import KernelAgentBase
from .agent_utils import get_completion_config

logger = logging.getLogger(__name__)

class SDGAgent(KernelAgentBase):
    """SDG Agent specialized in sustainable development goals analysis and alignment."""

    def __init__(
        self,
        name: str = "SDGAgent",
        system_prompt: str = None,
        llm_config: Dict = None,
        **kwargs,
    ):
        """Initialize a new instance of the SDG Agent."""
        
        # Default system prompt if none is provided
        if system_prompt is None:
            system_prompt = """You are the UN Sustainable Development Goals (SDG) Agent, specialized in analyzing how tasks, projects, and initiatives align with the 17 SDGs.

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

        super().__init__(
            name=name,
            system_prompt=system_prompt,
            llm_config=llm_config or get_completion_config(),
            **kwargs,
        )

    async def analyze_sdg_alignment(self, content: str) -> str:
        """
        Analyze how content aligns with the SDGs.
        
        Args:
            content: The text content to analyze for SDG alignment
            
        Returns:
            A detailed analysis of SDG alignment
        """
        prompt = f"""Please analyze the following content for alignment with the UN Sustainable Development Goals:

{content}

For each relevant SDG:
1. Identify which specific targets the content addresses
2. Rate the alignment (strong, moderate, weak)
3. Suggest metrics that could be used to measure progress
4. Recommend improvements to strengthen SDG alignment

Provide a concise summary at the end highlighting the primary SDGs addressed."""

        return await self.get_single_llm_completion(
            prompt=prompt,
            use_history=True
        )
    
    async def suggest_sdg_indicators(self, project_description: str) -> str:
        """
        Suggest appropriate SDG indicators for a project.
        
        Args:
            project_description: Description of the project or initiative
            
        Returns:
            Suggested SDG indicators with rationale
        """
        prompt = f"""Based on the following project description, suggest appropriate SDG indicators that could be used to measure progress and impact:

{project_description}

For each suggested indicator:
1. Identify the specific SDG and target it relates to
2. Explain why this indicator is appropriate for this project
3. Suggest practical data collection methods
4. Note any potential challenges in measurement"""

        return await self.get_single_llm_completion(
            prompt=prompt,
            use_history=True
        )
    
    async def identify_relevant_un_agencies(self, initiative: str) -> str:
        """
        Identify UN agencies relevant to a specific initiative.
        
        Args:
            initiative: Description of the initiative or project
            
        Returns:
            List of relevant UN agencies with rationale
        """
        prompt = f"""Based on the following initiative, identify the most relevant UN agencies and entities that could provide support, expertise, or partnership:

{initiative}

For each identified agency:
1. Explain their relevance to this initiative
2. Note their specific expertise or resources that would be valuable
3. Suggest potential mechanisms for engagement (e.g., technical assistance, funding, partnership)"""

        return await self.get_single_llm_completion(
            prompt=prompt,
            use_history=True
        )