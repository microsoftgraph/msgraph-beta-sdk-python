from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_extension_endpoint_configuration = lazy_import('msgraph.generated.models.custom_extension_endpoint_configuration')

class LogicAppTriggerEndpointConfiguration(custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new LogicAppTriggerEndpointConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.logicAppTriggerEndpointConfiguration"
        # The name of the logic app.
        self._logic_app_workflow_name: Optional[str] = None
        # The Azure resource group name for the logic app.
        self._resource_group_name: Optional[str] = None
        # Identifier of the Azure subscription for the logic app.
        self._subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LogicAppTriggerEndpointConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LogicAppTriggerEndpointConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LogicAppTriggerEndpointConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "logic_app_workflow_name": lambda n : setattr(self, 'logic_app_workflow_name', n.get_str_value()),
            "resource_group_name": lambda n : setattr(self, 'resource_group_name', n.get_str_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def logic_app_workflow_name(self,) -> Optional[str]:
        """
        Gets the logicAppWorkflowName property value. The name of the logic app.
        Returns: Optional[str]
        """
        return self._logic_app_workflow_name
    
    @logic_app_workflow_name.setter
    def logic_app_workflow_name(self,value: Optional[str] = None) -> None:
        """
        Sets the logicAppWorkflowName property value. The name of the logic app.
        Args:
            value: Value to set for the logicAppWorkflowName property.
        """
        self._logic_app_workflow_name = value
    
    @property
    def resource_group_name(self,) -> Optional[str]:
        """
        Gets the resourceGroupName property value. The Azure resource group name for the logic app.
        Returns: Optional[str]
        """
        return self._resource_group_name
    
    @resource_group_name.setter
    def resource_group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceGroupName property value. The Azure resource group name for the logic app.
        Args:
            value: Value to set for the resourceGroupName property.
        """
        self._resource_group_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("logicAppWorkflowName", self.logic_app_workflow_name)
        writer.write_str_value("resourceGroupName", self.resource_group_name)
        writer.write_str_value("subscriptionId", self.subscription_id)
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. Identifier of the Azure subscription for the logic app.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. Identifier of the Azure subscription for the logic app.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    

