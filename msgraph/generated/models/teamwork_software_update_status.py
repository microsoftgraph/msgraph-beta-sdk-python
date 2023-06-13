from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_software_freshness

@dataclass
class TeamworkSoftwareUpdateStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The available software version to update.
    available_version: Optional[str] = None
    # The current software version.
    current_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The update status of the software. The possible values are: unknown, latest, updateAvailable, unknownFutureValue.
    software_freshness: Optional[teamwork_software_freshness.TeamworkSoftwareFreshness] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSoftwareUpdateStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkSoftwareUpdateStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_software_freshness

        fields: Dict[str, Callable[[Any], None]] = {
            "availableVersion": lambda n : setattr(self, 'available_version', n.get_str_value()),
            "currentVersion": lambda n : setattr(self, 'current_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "softwareFreshness": lambda n : setattr(self, 'software_freshness', n.get_enum_value(teamwork_software_freshness.TeamworkSoftwareFreshness)),
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
        writer.write_str_value("availableVersion", self.available_version)
        writer.write_str_value("currentVersion", self.current_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("softwareFreshness", self.software_freshness)
        writer.write_additional_data_value(self.additional_data)
    

