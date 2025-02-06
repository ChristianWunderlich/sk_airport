import asyncio
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory
from modules.setup.setup_kernel import KernelSetup
from plugins.setup.airport_setup import AirportPluginSetup


async def main():

    userInput = None
    history = ChatHistory()
    while True:
        userInput = input("User > ")

        if userInput == "exit":
            break

        history.add_user_message(userInput)

        kernel_setup = KernelSetup()
        kernel, kernel_arguments = await kernel_setup.setup_kernel(history, userInput)

        airport_plugin_setup = AirportPluginSetup(kernel,kernel_arguments)
        kernel = await airport_plugin_setup.add_plugins_and_functions()

        result = await kernel.invoke(kernel.get_function_from_fully_qualified_function_name("ChatCompletionPlugin-ChatCompletion"), arguments=kernel_arguments)

        # Print the results
        print("Assistant > " + str(result.value[0].content))

        # Add the message from the agent to the chat history
        history.add_message({"role": "assistant", "content": str(result.value[0].content)})

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())