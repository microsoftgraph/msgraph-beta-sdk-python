from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class ApplicationSignInSummary(entity.Entity):
    # Name of the application that the user signed into.
    app_display_name: Optional[str] = None
    # Count of failed sign-ins made by the application.
    failed_sign_in_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Percentage of successful sign-ins made by the application.
    success_percentage: Optional[float] = None
    # Count of successful sign-ins made by the application.
    successful_sign_in_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationSignInSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSignInSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicationSignInSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "failedSignInCount": lambda n : setattr(self, 'failed_sign_in_count', n.get_int_value()),
            "successfulSignInCount": lambda n : setattr(self, 'successful_sign_in_count', n.get_int_value()),
            "successPercentage": lambda n : setattr(self, 'success_percentage', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_int_value("failedSignInCount", self.failed_sign_in_count)
        writer.write_int_value("successfulSignInCount", self.successful_sign_in_count)
        writer.write_float_value("successPercentage", self.success_percentage)
    

