from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

resource_connection = lazy_import('msgraph.generated.models.windows_updates.resource_connection')

class OperationalInsightsConnection(resource_connection.ResourceConnection):
    @property
    def azure_resource_group_name(self,) -> Optional[str]:
        """
        Gets the azureResourceGroupName property value. The name of the Azure resource group that contains the Log Analytics workspace.
        Returns: Optional[str]
        """
        return self._azure_resource_group_name
    
    @azure_resource_group_name.setter
    def azure_resource_group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the azureResourceGroupName property value. The name of the Azure resource group that contains the Log Analytics workspace.
        Args:
            value: Value to set for the azureResourceGroupName property.
        """
        self._azure_resource_group_name = value
    
    @property
    def azure_subscription_id(self,) -> Optional[str]:
        """
        Gets the azureSubscriptionId property value. The Azure subscription ID that contains the Log Analytics workspace.
        Returns: Optional[str]
        """
        return self._azure_subscription_id
    
    @azure_subscription_id.setter
    def azure_subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureSubscriptionId property value. The Azure subscription ID that contains the Log Analytics workspace.
        Args:
            value: Value to set for the azureSubscriptionId property.
        """
        self._azure_subscription_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OperationalInsightsConnection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.operationalInsightsConnection"
        # The name of the Azure resource group that contains the Log Analytics workspace.
        self._azure_resource_group_name: Optional[str] = None
        # The Azure subscription ID that contains the Log Analytics workspace.
        self._azure_subscription_id: Optional[str] = None
        # The name of the Log Analytics workspace.
        self._workspace_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OperationalInsightsConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OperationalInsightsConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OperationalInsightsConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_resource_group_name": lambda n : setattr(self, 'azure_resource_group_name', n.get_str_value()),
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "workspace_name": lambda n : setattr(self, 'workspace_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureResourceGroupName", self.azure_resource_group_name)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("workspaceName", self.workspace_name)
    
    @property
    def workspace_name(self,) -> Optional[str]:
        """
        Gets the workspaceName property value. The name of the Log Analytics workspace.
        Returns: Optional[str]
        """
        return self._workspace_name
    
    @workspace_name.setter
    def workspace_name(self,value: Optional[str] = None) -> None:
        """
        Sets the workspaceName property value. The name of the Log Analytics workspace.
        Args:
            value: Value to set for the workspaceName property.
        """
        self._workspace_name = value
    

