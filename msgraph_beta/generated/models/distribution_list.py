from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .distribution_list_member import DistributionListMember
    from .member import Member
    from .outlook_item import OutlookItem
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class DistributionList(OutlookItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.distributionList"
    # The display name of the distribution list.
    display_name: Optional[str] = None
    # The expanded members of the distribution list. Each member contains detailed information including resolved email addresses. Read-only.
    distribution_list_members: Optional[list[DistributionListMember]] = None
    # The list of members in the distribution list. Not returned by default; use $select=members to include.
    members: Optional[list[Member]] = None
    # The notes property
    notes: Optional[str] = None
    # The personIdentifier property
    person_identifier: Optional[str] = None
    # The singleValueExtendedProperties property
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DistributionList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DistributionList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DistributionList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .distribution_list_member import DistributionListMember
        from .member import Member
        from .outlook_item import OutlookItem
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .distribution_list_member import DistributionListMember
        from .member import Member
        from .outlook_item import OutlookItem
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "distributionListMembers": lambda n : setattr(self, 'distribution_list_members', n.get_collection_of_object_values(DistributionListMember)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(Member)),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "personIdentifier": lambda n : setattr(self, 'person_identifier', n.get_str_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("distributionListMembers", self.distribution_list_members)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("personIdentifier", self.person_identifier)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
    

