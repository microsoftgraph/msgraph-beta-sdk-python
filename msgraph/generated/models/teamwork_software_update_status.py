from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_software_freshness import TeamworkSoftwareFreshness

@dataclass
class TeamworkSoftwareUpdateStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The available software version to update.
    available_version: Optional[str] = None
    # The current software version.
    current_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The update status of the software. The possible values are: unknown, latest, updateAvailable, unknownFutureValue.
    software_freshness: Optional[TeamworkSoftwareFreshness] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSoftwareUpdateStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSoftwareUpdateStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_software_freshness import TeamworkSoftwareFreshness

        from .teamwork_software_freshness import TeamworkSoftwareFreshness

        fields: Dict[str, Callable[[Any], None]] = {
            "availableVersion": lambda n : setattr(self, 'available_version', n.get_str_value()),
            "currentVersion": lambda n : setattr(self, 'current_version', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "softwareFreshness": lambda n : setattr(self, 'software_freshness', n.get_enum_value(TeamworkSoftwareFreshness)),
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
        writer.write_str_value("availableVersion", self.available_version)
        writer.write_str_value("currentVersion", self.current_version)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("softwareFreshness", self.software_freshness)
        writer.write_additional_data_value(self.additional_data)
    

