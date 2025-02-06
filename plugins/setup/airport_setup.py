import logging
import os
from semantic_kernel import Kernel
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig
from plugins.airport.airport_plugin_from_module import AirportPlugin
from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings
from semantic_kernel.functions import KernelArguments


class AirportPluginSetup:

    def __init__(self, kernel: Kernel, arguments: KernelArguments):
        self.kernel = kernel
        self.arguments = arguments

    async def add_plugins_and_functions(self):
        logger = logging.getLogger("kernel")
        logger.info("Adding plugins to the kernel...")
        self.kernel.add_plugin(
            plugin=AirportPlugin(self.kernel, self.arguments),
            plugin_name="ModulePlugin")
        logger.info("Plugins added successfully.")

        logger.info("Adding functions to the kernel...")
       
        with open(os.path.join(os.getcwd(),"plugins","templates","airport", "filter_input_question.jinja2"), "r") as file:
            filter_input_question = file.read()
            if filter_input_question:
                prompt_template_config_for_metadata = PromptTemplateConfig(
                    template=filter_input_question,
                    name="FilterInputQuestion",
                    description="create a filter json response for the input question.",
                    template_format="jinja2",
                    input_variables=[
                        InputVariable(name="question", description="The user's question", is_required=True),
                    ],
                    execution_settings=AzureChatPromptExecutionSettings(
                        service_id="AzureChatCompletionService",temperature=0.0, response_format={"type": "json_object"} 
                    ),
                )
                self.kernel.add_function(
                    function_name="FilterInputQuestion",
                    plugin_name="ModulePlugin",
                    prompt_template_config=prompt_template_config_for_metadata,
                    template_format="jinja2"
                )

        return self.kernel
