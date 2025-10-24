from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_data import CustomExtensionData

from .custom_extension_data import CustomExtensionData

@dataclass
class AccessReviewDataUploadTriggerCallbackData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewDataUploadTriggerCallbackData"
    # The permissionDescription property
    permission_description: Optional[str] = None
    # The permissionId property
    permission_id: Optional[str] = None
    # The permissionName property
    permission_name: Optional[str] = None
    # The permissionType property
    permission_type: Optional[str] = None
    # The principalAADId property
    principal_a_a_d_id: Optional[str] = None
    # The resourceDescription property
    resource_description: Optional[str] = None
    # The resourceId property
    resource_id: Optional[str] = None
    # The resourceName property
    resource_name: Optional[str] = None
    # The resourceOwners property
    resource_owners: Optional[list[str]] = None
    # The resourceType property
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewDataUploadTriggerCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewDataUploadTriggerCallbackData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewDataUploadTriggerCallbackData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_data import CustomExtensionData

        from .custom_extension_data import CustomExtensionData

        fields: dict[str, Callable[[Any], None]] = {
            "permissionDescription": lambda n : setattr(self, 'permission_description', n.get_str_value()),
            "permissionId": lambda n : setattr(self, 'permission_id', n.get_str_value()),
            "permissionName": lambda n : setattr(self, 'permission_name', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_str_value()),
            "principalAADId": lambda n : setattr(self, 'principal_a_a_d_id', n.get_str_value()),
            "resourceDescription": lambda n : setattr(self, 'resource_description', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "resourceOwners": lambda n : setattr(self, 'resource_owners', n.get_collection_of_primitive_values(str)),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("permissionDescription", self.permission_description)
        writer.write_str_value("permissionId", self.permission_id)
        writer.write_str_value("permissionName", self.permission_name)
        writer.write_str_value("permissionType", self.permission_type)
        writer.write_str_value("principalAADId", self.principal_a_a_d_id)
        writer.write_str_value("resourceDescription", self.resource_description)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_collection_of_primitive_values("resourceOwners", self.resource_owners)
        writer.write_str_value("resourceType", self.resource_type)
    

