from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_permissions_definition import AwsPermissionsDefinition
    from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
    from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
    from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition
    from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition

@dataclass
class PermissionsDefinition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The authorizationSystemInfo property
    authorization_system_info: Optional[PermissionsDefinitionAuthorizationSystem] = None
    # The identityInfo property
    identity_info: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionsDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsPermissionsDefinition".casefold():
            from .aws_permissions_definition import AwsPermissionsDefinition

            return AwsPermissionsDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleResourceAzurePermissionsDefinition".casefold():
            from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition

            return SingleResourceAzurePermissionsDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleResourceGcpPermissionsDefinition".casefold():
            from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition

            return SingleResourceGcpPermissionsDefinition()
        return PermissionsDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_permissions_definition import AwsPermissionsDefinition
        from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
        from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
        from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition
        from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition

        from .aws_permissions_definition import AwsPermissionsDefinition
        from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
        from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity
        from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition
        from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "authorizationSystemInfo": lambda n : setattr(self, 'authorization_system_info', n.get_object_value(PermissionsDefinitionAuthorizationSystem)),
            "identityInfo": lambda n : setattr(self, 'identity_info', n.get_object_value(PermissionsDefinitionAuthorizationSystemIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("authorizationSystemInfo", self.authorization_system_info)
        writer.write_object_value("identityInfo", self.identity_info)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

