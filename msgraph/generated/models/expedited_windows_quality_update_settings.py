from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ExpeditedWindowsQualityUpdateSettings(AdditionalDataHolder, Parsable):
    """
    A complex type to store the expedited quality update settings such as release date and days until forced reboot.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The number of days after installation that forced reboot will happen.
    days_until_forced_reboot: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The release date to identify a quality update.
    quality_update_release: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpeditedWindowsQualityUpdateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpeditedWindowsQualityUpdateSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExpeditedWindowsQualityUpdateSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "daysUntilForcedReboot": lambda n : setattr(self, 'days_until_forced_reboot', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qualityUpdateRelease": lambda n : setattr(self, 'quality_update_release', n.get_str_value()),
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
        writer.write_int_value("daysUntilForcedReboot", self.days_until_forced_reboot)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityUpdateRelease", self.quality_update_release)
        writer.write_additional_data_value(self.additional_data)
    

