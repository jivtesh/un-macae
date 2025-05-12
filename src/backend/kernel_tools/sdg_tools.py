import inspect
from typing import Annotated, Callable, List

from semantic_kernel.functions import kernel_function
from models.messages_kernel import AgentType
import inspect
import json
from typing import Any, Dict, List, get_type_hints


class SDGTools:
    """Define SDG Agent functions (tools) for analyzing UN Sustainable Development Goals"""

    formatting_instructions = "Instructions: returning the output of this function call verbatim to the user in markdown. Then write AGENT SUMMARY: and then include a summary of what you did."
    agent_name = AgentType.SDG.value

    @staticmethod
    @kernel_function(
        description="Analyze a project's alignment with SDG 4 (Quality Education). This should be used for ANY query related to education, training, learning, teaching, or SDG 4."
    )
    async def analyze_sdg4_alignment(project_description: str) -> str:
        """Analyze how a project aligns with SDG 4 (Quality Education) and its targets. Use this for ANY education-related query."""
        return (
            f"##### SDG 4 Alignment Analysis\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of project alignment with SDG 4 (Quality Education) completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Analyze a project's alignment with any SDG by specifying the SDG number. Use for all SDG alignment analysis except SDG 4 (which has its own function)."
    )
    async def analyze_sdg_alignment(sdg_number: int, project_description: str) -> str:
        """Analyze how a project aligns with a specified SDG and its targets."""
        return (
            f"##### SDG {sdg_number} Alignment Analysis\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of project alignment with SDG {sdg_number} completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Evaluate teacher training components in a project for SDG 4 alignment"
    )
    async def analyze_teacher_training(project_description: str) -> str:
        """Evaluate how a project's teacher training components align with SDG 4."""
        return (
            f"##### Teacher Training Analysis for SDG 4\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of teacher training components and alignment with SDG 4 completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Evaluate digital learning tools in a project for SDG 4 alignment"
    )
    async def analyze_digital_learning_tools(project_description: str) -> str:
        """Evaluate how a project's digital learning tools align with SDG 4."""
        return (
            f"##### Digital Learning Tools Analysis for SDG 4\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of digital learning tools and alignment with SDG 4 completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Evaluate gender equality aspects in education projects (SDG 4.5)"
    )
    async def analyze_gender_equality_in_education(project_description: str) -> str:
        """Evaluate how a project addresses gender equality in education (SDG 4.5)."""
        return (
            f"##### Gender Equality in Education Analysis (SDG 4.5)\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of gender equality aspects in education and alignment with SDG 4.5 completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Evaluate accessibility for persons with disabilities in education projects (SDG 4.5)"
    )
    async def analyze_education_accessibility(project_description: str) -> str:
        """Evaluate how a project addresses accessibility for persons with disabilities in education (SDG 4.5)."""
        return (
            f"##### Education Accessibility Analysis for Persons with Disabilities (SDG 4.5)\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of accessibility for persons with disabilities in education and alignment with SDG 4.5 completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Suggest SDG indicators for tracking project impact"
    )
    async def suggest_sdg_indicators(sdg_number: int) -> str:
        """Suggest SDG indicators for tracking project impact."""
        return (
            f"##### SDG {sdg_number} Indicators\n\n"
            f"Suggested indicators for tracking SDG {sdg_number} impact have been provided.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Identify UN agencies relevant to a specific SDG"
    )
    async def identify_un_agencies(sdg_number: int) -> str:
        """Identify UN agencies relevant to a specific SDG."""
        return (
            f"##### UN Agencies for SDG {sdg_number}\n\n"
            f"Identified UN agencies relevant to SDG {sdg_number}.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Generate SDG-specific recommendations for a project"
    )
    async def generate_sdg_recommendations(sdg_number: int, project_description: str) -> str:
        """Generate SDG-specific recommendations for a project."""
        return (
            f"##### SDG {sdg_number} Recommendations\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Recommendations for improving alignment with SDG {sdg_number} have been generated.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Analyze interlinkages between SDGs for a project"
    )
    async def analyze_sdg_interlinkages(primary_sdg: int, project_description: str) -> str:
        """Analyze interlinkages between SDGs for a project."""
        return (
            f"##### SDG Interlinkages Analysis\n"
            f"**Primary SDG:** {primary_sdg}\n"
            f"**Project:** {project_description[:50]}...\n\n"
            f"Analysis of interlinkages between SDG {primary_sdg} and other SDGs completed.\n"
            f"{SDGTools.formatting_instructions}"
        )
    
    @staticmethod
    @kernel_function(
        description="Provide implementation guidance for SDG targets"
    )
    async def provide_sdg_implementation_guidance(sdg_number: int, target_number: str) -> str:
        """Provide implementation guidance for SDG targets."""
        return (
            f"##### Implementation Guidance for SDG {sdg_number}.{target_number}\n\n"
            f"Implementation guidance for target {sdg_number}.{target_number} has been provided.\n"
            f"{SDGTools.formatting_instructions}"
        )

    @classmethod
    def get_all_kernel_functions(cls) -> dict[str, Callable]:
        """
        Returns a dictionary of all methods in this class that have the @kernel_function annotation.
        This function itself is not annotated with @kernel_function.

        Returns:
            Dict[str, Callable]: Dictionary with function names as keys and function objects as values
        """
        kernel_functions = {}

        # Get all class methods
        for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
            # Skip this method itself and any private/special methods
            if name.startswith("_") or name == "get_all_kernel_functions":
                continue

            # Check if the method has the kernel_function annotation
            # by looking at its __annotations__ attribute
            method_attrs = getattr(method, "__annotations__", {})
            if hasattr(method, "__kernel_function__") or "kernel_function" in str(
                method_attrs
            ):
                kernel_functions[name] = method

        return kernel_functions

    @classmethod
    def generate_tools_json_doc(cls) -> str:
        """
        Generate a JSON document containing information about all methods in the class.

        Returns:
            str: JSON string containing the methods' information
        """

        tools_list = []

        # Get all methods from the class that have the kernel_function annotation
        for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
            # Skip this method itself and any private methods
            if name.startswith("_") or name == "generate_tools_json_doc":
                continue

            # Check if the method has the kernel_function annotation
            if hasattr(method, "__kernel_function__"):
                # Get method description from docstring or kernel_function description
                description = ""
                if hasattr(method, "__doc__") and method.__doc__:
                    description = method.__doc__.strip()

                # Get kernel_function description if available
                if hasattr(method, "__kernel_function__") and getattr(
                    method.__kernel_function__, "description", None
                ):
                    description = method.__kernel_function__.description

                # Get argument information by introspection
                sig = inspect.signature(method)
                args_dict = {}

                # Get type hints if available
                type_hints = get_type_hints(method)

                # Process parameters
                for param_name, param in sig.parameters.items():
                    # Skip first parameter 'cls' for class methods (though we're using staticmethod now)
                    if param_name in ["cls", "self"]:
                        continue

                    # Get parameter type
                    param_type = "string"  # Default type
                    if param_name in type_hints:
                        type_obj = type_hints[param_name]
                        # Convert type to string representation
                        if hasattr(type_obj, "__name__"):
                            param_type = type_obj.__name__.lower()
                        else:
                            # Handle complex types like List, Dict, etc.
                            param_type = str(type_obj).lower()
                            if "int" in param_type:
                                param_type = "int"
                            elif "float" in param_type:
                                param_type = "float"
                            elif "bool" in param_type:
                                param_type = "boolean"
                            else:
                                param_type = "string"

                    # Create parameter description
                    param_desc = param_name.replace("_", " ")
                    args_dict[param_name] = {
                        "description": param_name,
                        "title": param_name.replace("_", " ").title(),
                        "type": param_type,
                    }

                # Add the tool information to the list
                tool_entry = {
                    "agent": cls.agent_name,  # Use SDG agent type
                    "function": name,
                    "description": description,
                    "arguments": json.dumps(args_dict).replace('"', "'"),
                }

                tools_list.append(tool_entry)

        # Return the JSON string representation
        return json.dumps(tools_list, ensure_ascii=False, indent=2)