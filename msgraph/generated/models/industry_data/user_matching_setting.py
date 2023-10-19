from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identifier_type_reference_value import IdentifierTypeReferenceValue
    from .role_group import RoleGroup
    from .user_match_target_reference_value import UserMatchTargetReferenceValue

@dataclass
class UserMatchingSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The RefUserMatchTarget for matching a user from the source with a Microsoft Entra user object.
    match_target: Optional[UserMatchTargetReferenceValue] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority order to apply when a user has multiple RefRole codes assigned.
    priority_order: Optional[int] = None
    # The roleGroup property
    role_group: Optional[RoleGroup] = None
    # The sourceIdentifier property
    source_identifier: Optional[IdentifierTypeReferenceValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserMatchingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserMatchingSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserMatchingSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .role_group import RoleGroup
        from .user_match_target_reference_value import UserMatchTargetReferenceValue

        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .role_group import RoleGroup
        from .user_match_target_reference_value import UserMatchTargetReferenceValue

        fields: Dict[str, Callable[[Any], None]] = {
            "matchTarget": lambda n : setattr(self, 'match_target', n.get_object_value(UserMatchTargetReferenceValue)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priorityOrder": lambda n : setattr(self, 'priority_order', n.get_int_value()),
            "roleGroup": lambda n : setattr(self, 'role_group', n.get_object_value(RoleGroup)),
            "sourceIdentifier": lambda n : setattr(self, 'source_identifier', n.get_object_value(IdentifierTypeReferenceValue)),
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
        writer.write_object_value("matchTarget", self.match_target)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("priorityOrder", self.priority_order)
        writer.write_object_value("roleGroup", self.role_group)
        writer.write_object_value("sourceIdentifier", self.source_identifier)
        writer.write_additional_data_value(self.additional_data)
    

