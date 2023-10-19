from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AndroidDeviceOwnerSystemUpdateFreezePeriod(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents one item in the list of freeze periods for Android Device Owner system updates
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The day of the end date of the freeze period. Valid values 1 to 31
    end_day: Optional[int] = None
    # The month of the end date of the freeze period. Valid values 1 to 12
    end_month: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The day of the start date of the freeze period. Valid values 1 to 31
    start_day: Optional[int] = None
    # The month of the start date of the freeze period. Valid values 1 to 12
    start_month: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerSystemUpdateFreezePeriod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerSystemUpdateFreezePeriod
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerSystemUpdateFreezePeriod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "endDay": lambda n : setattr(self, 'end_day', n.get_int_value()),
            "endMonth": lambda n : setattr(self, 'end_month', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDay": lambda n : setattr(self, 'start_day', n.get_int_value()),
            "startMonth": lambda n : setattr(self, 'start_month', n.get_int_value()),
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
        writer.write_int_value("endDay", self.end_day)
        writer.write_int_value("endMonth", self.end_month)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("startDay", self.start_day)
        writer.write_int_value("startMonth", self.start_month)
        writer.write_additional_data_value(self.additional_data)
    

