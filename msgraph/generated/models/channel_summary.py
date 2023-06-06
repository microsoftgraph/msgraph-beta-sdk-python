from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ChannelSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The guestsCount property
    guests_count: Optional[int] = None
    # The hasMembersFromOtherTenants property
    has_members_from_other_tenants: Optional[bool] = None
    # The membersCount property
    members_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ownersCount property
    owners_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "guestsCount": lambda n : setattr(self, 'guests_count', n.get_int_value()),
            "hasMembersFromOtherTenants": lambda n : setattr(self, 'has_members_from_other_tenants', n.get_bool_value()),
            "membersCount": lambda n : setattr(self, 'members_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownersCount": lambda n : setattr(self, 'owners_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("guestsCount", self.guests_count)
        writer.write_bool_value("hasMembersFromOtherTenants", self.has_members_from_other_tenants)
        writer.write_int_value("membersCount", self.members_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("ownersCount", self.owners_count)
        writer.write_additional_data_value(self.additional_data)
    

