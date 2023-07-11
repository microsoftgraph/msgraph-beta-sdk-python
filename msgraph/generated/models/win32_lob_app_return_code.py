from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_return_code_type import Win32LobAppReturnCodeType

@dataclass
class Win32LobAppReturnCode(AdditionalDataHolder, Parsable):
    """
    Contains return code properties for a Win32 App
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Return code.
    return_code: Optional[int] = None
    # Indicates the type of return code.
    type: Optional[Win32LobAppReturnCodeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppReturnCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppReturnCode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppReturnCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_return_code_type import Win32LobAppReturnCodeType

        from .win32_lob_app_return_code_type import Win32LobAppReturnCodeType

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "returnCode": lambda n : setattr(self, 'return_code', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Win32LobAppReturnCodeType)),
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
        writer.write_int_value("returnCode", self.return_code)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

