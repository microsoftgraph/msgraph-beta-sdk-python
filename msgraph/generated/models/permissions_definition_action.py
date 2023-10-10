from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction
    from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
    from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction
    from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction
    from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
    from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction
    from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
    from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
    from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction

@dataclass
class PermissionsDefinitionAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsDefinitionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsDefinitionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsActionsPermissionsDefinitionAction".casefold():
            from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction

            return AwsActionsPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsPermissionsDefinitionAction".casefold():
            from .aws_permissions_definition_action import AwsPermissionsDefinitionAction

            return AwsPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsPolicyPermissionsDefinitionAction".casefold():
            from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction

            return AwsPolicyPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureActionPermissionsDefinitionAction".casefold():
            from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction

            return AzureActionPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azurePermissionsDefinitionAction".casefold():
            from .azure_permissions_definition_action import AzurePermissionsDefinitionAction

            return AzurePermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureRolePermissionsDefinitionAction".casefold():
            from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction

            return AzureRolePermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpActionPermissionsDefinitionAction".casefold():
            from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction

            return GcpActionPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpPermissionsDefinitionAction".casefold():
            from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction

            return GcpPermissionsDefinitionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpRolePermissionsDefinitionAction".casefold():
            from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction

            return GcpRolePermissionsDefinitionAction()
        return PermissionsDefinitionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction
        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction
        from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction
        from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
        from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction
        from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
        from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
        from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction

        from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction
        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction
        from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction
        from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
        from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction
        from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
        from .gcp_permissions_definition_action import GcpPermissionsDefinitionAction
        from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

