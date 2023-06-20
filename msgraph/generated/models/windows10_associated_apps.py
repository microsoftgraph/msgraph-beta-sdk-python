from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows10_app_type

@dataclass
class Windows10AssociatedApps(AdditionalDataHolder, Parsable):
    """
    Windows 10 Associated Application definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Windows 10 Application type.
    app_type: Optional[windows10_app_type.Windows10AppType] = None
    # Identifier.
    identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10AssociatedApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10AssociatedApps
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10AssociatedApps()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows10_app_type

        from . import windows10_app_type

        fields: Dict[str, Callable[[Any], None]] = {
            "appType": lambda n : setattr(self, 'app_type', n.get_enum_value(windows10_app_type.Windows10AppType)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
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
        writer.write_enum_value("appType", self.app_type)
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

