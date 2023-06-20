from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import provisioning_status_error_category, status_base

from . import status_base

@dataclass
class StatusDetails(status_base.StatusBase):
    odata_type = "#microsoft.graph.statusDetails"
    # Additional details in case of error.
    additional_details: Optional[str] = None
    # Categorizes the error code. Possible values are Failure, NonServiceFailure, Success.
    error_category: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory] = None
    # Unique error code if any occurred. Learn more
    error_code: Optional[str] = None
    # Summarizes the status and describes why the status happened.
    reason: Optional[str] = None
    # Provides the resolution for the corresponding error.
    recommended_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StatusDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StatusDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import provisioning_status_error_category, status_base

        from . import provisioning_status_error_category, status_base

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "errorCategory": lambda n : setattr(self, 'error_category', n.get_enum_value(provisioning_status_error_category.ProvisioningStatusErrorCategory)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recommendedAction", self.recommended_action)
    

