from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .pre_approval_detail import PreApprovalDetail

from .directory_object import DirectoryObject

@dataclass
class PermissionGrantPreApprovalPolicy(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.permissionGrantPreApprovalPolicy"
    # A list of condition sets describing the conditions under which the permission to grant consent for the app has been preapproved.
    conditions: Optional[List[PreApprovalDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionGrantPreApprovalPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantPreApprovalPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionGrantPreApprovalPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .pre_approval_detail import PreApprovalDetail

        from .directory_object import DirectoryObject
        from .pre_approval_detail import PreApprovalDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(PreApprovalDetail)),
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
        from .directory_object import DirectoryObject
        from .pre_approval_detail import PreApprovalDetail

        writer.write_collection_of_object_values("conditions", self.conditions)
    

