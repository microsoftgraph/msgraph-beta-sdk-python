from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import resource_connection

from . import resource_connection

class OperationalInsightsConnection(resource_connection.ResourceConnection):
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
            value: Value to set for the azure_resource_group_name property.
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
            value: Value to set for the azure_subscription_id property.
        """
        self._azure_subscription_id = value
    
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
        from . import resource_connection

        fields: Dict[str, Callable[[Any], None]] = {
            "azureResourceGroupName": lambda n : setattr(self, 'azure_resource_group_name', n.get_str_value()),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "workspaceName": lambda n : setattr(self, 'workspace_name', n.get_str_value()),
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
            value: Value to set for the workspace_name property.
        """
        self._workspace_name = value
    

