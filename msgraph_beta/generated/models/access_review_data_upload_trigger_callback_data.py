from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_data import CustomExtensionData
    from .principal_type import PrincipalType

from .custom_extension_data import CustomExtensionData

@dataclass
class AccessReviewDataUploadTriggerCallbackData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewDataUploadTriggerCallbackData"
    # A description for the permission.
    permission_description: Optional[str] = None
    # The id of the permission assigned to this principal.
    permission_id: Optional[str] = None
    # The name of the permission assigned to this principal.
    permission_name: Optional[str] = None
    # The type of the permission assigned to this principal.
    permission_type: Optional[str] = None
    # The id of the principal who has permissions on the custom data provided resource.
    principal_id: Optional[str] = None
    # The principalType property
    principal_type: Optional[PrincipalType] = None
    
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
        from .principal_type import PrincipalType

        from .custom_extension_data import CustomExtensionData
        from .principal_type import PrincipalType

        fields: dict[str, Callable[[Any], None]] = {
            "permissionDescription": lambda n : setattr(self, 'permission_description', n.get_str_value()),
            "permissionId": lambda n : setattr(self, 'permission_id', n.get_str_value()),
            "permissionName": lambda n : setattr(self, 'permission_name', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_str_value()),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "principalType": lambda n : setattr(self, 'principal_type', n.get_enum_value(PrincipalType)),
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
        writer.write_str_value("principalId", self.principal_id)
        writer.write_enum_value("principalType", self.principal_type)
    

