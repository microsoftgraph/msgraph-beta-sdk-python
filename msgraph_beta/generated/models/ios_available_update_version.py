from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class IosAvailableUpdateVersion(AdditionalDataHolder, BackedModel, Parsable):
    """
    iOS available update version details
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The expiration date of the update.
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The posting date of the update.
    posting_date_time: Optional[datetime.datetime] = None
    # The version of the update.
    product_version: Optional[str] = None
    # List of supported devices for the update.
    supported_devices: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosAvailableUpdateVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosAvailableUpdateVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosAvailableUpdateVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postingDateTime": lambda n : setattr(self, 'posting_date_time', n.get_datetime_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "supportedDevices": lambda n : setattr(self, 'supported_devices', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("postingDateTime", self.posting_date_time)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_collection_of_primitive_values("supportedDevices", self.supported_devices)
        writer.write_additional_data_value(self.additional_data)
    

