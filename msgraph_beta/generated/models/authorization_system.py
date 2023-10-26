from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_authorization_system import AwsAuthorizationSystem
    from .azure_authorization_system import AzureAuthorizationSystem
    from .data_collection_info import DataCollectionInfo
    from .entity import Entity
    from .gcp_authorization_system import GcpAuthorizationSystem

from .entity import Entity

@dataclass
class AuthorizationSystem(Entity):
    # The authorizationSystemId property
    authorization_system_id: Optional[str] = None
    # The authorizationSystemName property
    authorization_system_name: Optional[str] = None
    # The authorizationSystemType property
    authorization_system_type: Optional[str] = None
    # The dataCollectionInfo property
    data_collection_info: Optional[DataCollectionInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystem".casefold():
            from .aws_authorization_system import AwsAuthorizationSystem

            return AwsAuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystem".casefold():
            from .azure_authorization_system import AzureAuthorizationSystem

            return AzureAuthorizationSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystem".casefold():
            from .gcp_authorization_system import GcpAuthorizationSystem

            return GcpAuthorizationSystem()
        return AuthorizationSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_authorization_system import AwsAuthorizationSystem
        from .azure_authorization_system import AzureAuthorizationSystem
        from .data_collection_info import DataCollectionInfo
        from .entity import Entity
        from .gcp_authorization_system import GcpAuthorizationSystem

        from .aws_authorization_system import AwsAuthorizationSystem
        from .azure_authorization_system import AzureAuthorizationSystem
        from .data_collection_info import DataCollectionInfo
        from .entity import Entity
        from .gcp_authorization_system import GcpAuthorizationSystem

        fields: Dict[str, Callable[[Any], None]] = {
            "authorizationSystemId": lambda n : setattr(self, 'authorization_system_id', n.get_str_value()),
            "authorizationSystemName": lambda n : setattr(self, 'authorization_system_name', n.get_str_value()),
            "authorizationSystemType": lambda n : setattr(self, 'authorization_system_type', n.get_str_value()),
            "dataCollectionInfo": lambda n : setattr(self, 'data_collection_info', n.get_object_value(DataCollectionInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("authorizationSystemId", self.authorization_system_id)
        writer.write_str_value("authorizationSystemName", self.authorization_system_name)
        writer.write_str_value("authorizationSystemType", self.authorization_system_type)
        writer.write_object_value("dataCollectionInfo", self.data_collection_info)
    

