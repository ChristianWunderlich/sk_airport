import os
from typing import Annotated
import json
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from modules.airport.airportapiclient import AirportApiClient
from semantic_kernel.functions import KernelArguments

class AirportPlugin:
    def __init__(self, kernel: Kernel, arguments: KernelArguments):
        self.airport_data_endpoint = os.getenv("DATA_ENDPOINT")
        self.airport_api_client = AirportApiClient()
        self.kernel = kernel
        self.arguments = arguments

    @kernel_function(
            name="get_all_airports",
            description="This function is executed to get a list of all airports",
    )
    async def get_all_online_airports(self):
        t = await self.kernel.invoke(
            plugin_name="ModulePlugin",
            function_name="FilterInputQuestion",
            arguments=KernelArguments(
                question=self.arguments.get("user_input"),
            )
        )
        filter = json.loads(t.value[0].content)
        
        airports =  await self.airport_api_client.get(self.airport_data_endpoint)

        filtered_airports = airports

        if filter.get("airport"):
            filtered_airports = [airport for airport in filtered_airports if airport.get("code") == filter["airport"]]
            return filtered_airports

        if filter.get("city"):
            filtered_airports = [airport for airport in filtered_airports if airport.get("city") == filter["city"]]
            return filtered_airports

        if filter.get("country"):
            filtered_airports = [airport for airport in filtered_airports if airport.get("country") == filter["country"]]
            return filtered_airports
        
        return filtered_airports
    