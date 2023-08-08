from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesProvisioningError(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Category of the provisioning error. Note: Currently, there is only one possible value. Possible value: PropertyConflict - indicates a property value is not unique. Other objects contain the same value for the property.
    category: Optional[str] = None
    # The date and time at which the error occurred.
    occurred_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the directory property causing the error. Current possible values: UserPrincipalName or ProxyAddress
    property_causing_error: Optional[str] = None
    # Value of the property causing the error.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesProvisioningError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesProvisioningError
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesProvisioningError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "occurredDateTime": lambda n : setattr(self, 'occurred_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propertyCausingError": lambda n : setattr(self, 'property_causing_error', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_datetime_value("occurredDateTime", self.occurred_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("propertyCausingError", self.property_causing_error)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

