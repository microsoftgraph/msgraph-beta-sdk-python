from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group import Group
    from .policy_scope import PolicyScope

from .entity import Entity

@dataclass
class MobilityManagementPolicy(Entity):
    # Indicates the user scope of the mobility management policy. Possible values are: none, all, selected.
    applies_to: Optional[PolicyScope] = None
    # Compliance URL of the mobility management application.
    compliance_url: Optional[str] = None
    # Description of the mobility management application.
    description: Optional[str] = None
    # Discovery URL of the mobility management application.
    discovery_url: Optional[str] = None
    # Display name of the mobility management application.
    display_name: Optional[str] = None
    # Microsoft Entra groups under the scope of the mobility management application if appliesTo is selected
    included_groups: Optional[List[Group]] = None
    # Whether policy is valid. Invalid policies may not be updated and should be deleted.
    is_valid: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Terms of Use URL of the mobility management application.
    terms_of_use_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobilityManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobilityManagementPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobilityManagementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group import Group
        from .policy_scope import PolicyScope

        from .entity import Entity
        from .group import Group
        from .policy_scope import PolicyScope

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_enum_value(PolicyScope)),
            "complianceUrl": lambda n : setattr(self, 'compliance_url', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoveryUrl": lambda n : setattr(self, 'discovery_url', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "includedGroups": lambda n : setattr(self, 'included_groups', n.get_collection_of_object_values(Group)),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "termsOfUseUrl": lambda n : setattr(self, 'terms_of_use_url', n.get_str_value()),
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
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_str_value("complianceUrl", self.compliance_url)
        writer.write_str_value("description", self.description)
        writer.write_str_value("discoveryUrl", self.discovery_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("includedGroups", self.included_groups)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_str_value("termsOfUseUrl", self.terms_of_use_url)
    

