from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_mobile_app_identifier, ios_mobile_app_identifier, mac_app_identifier, windows_app_identifier

@dataclass
class MobileAppIdentifier(AdditionalDataHolder, Parsable):
    """
    The identifier for a mobile app.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppIdentifier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppIdentifier
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidMobileAppIdentifier".casefold():
            from . import android_mobile_app_identifier

            return android_mobile_app_identifier.AndroidMobileAppIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosMobileAppIdentifier".casefold():
            from . import ios_mobile_app_identifier

            return ios_mobile_app_identifier.IosMobileAppIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macAppIdentifier".casefold():
            from . import mac_app_identifier

            return mac_app_identifier.MacAppIdentifier()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppIdentifier".casefold():
            from . import windows_app_identifier

            return windows_app_identifier.WindowsAppIdentifier()
        return MobileAppIdentifier()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_mobile_app_identifier, ios_mobile_app_identifier, mac_app_identifier, windows_app_identifier

        from . import android_mobile_app_identifier, ios_mobile_app_identifier, mac_app_identifier, windows_app_identifier

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

