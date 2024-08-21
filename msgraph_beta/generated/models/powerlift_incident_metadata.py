from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PowerliftIncidentMetadata(AdditionalDataHolder, BackedModel, Parsable):
    """
    Collection of app diagnostics associated with a user.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The name of the application the diagnostic is from. Example: com.microsoft.CompanyPortal
    application: Optional[str] = None
    # The version of the application. Example: 5.2203.1
    client_version: Optional[str] = None
    # The time the app diagnostic was created. Example: 2022-04-19T17:24:45.313Z
    created_at_date_time: Optional[datetime.datetime] = None
    # The unique app diagnostic identifier as a user friendly 8 character hexadecimal string. Example: 8520467A
    easy_id: Optional[str] = None
    # A list of files that are associated with the diagnostic.
    file_names: Optional[List[str]] = None
    # The locale information of the application. Example: en-US
    locale: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The device's OS the diagnostic is from. Example: iOS
    platform: Optional[str] = None
    # The unique identifier of the app diagnostic. Example: 8520467a-49a9-44a4-8447-8dfb8bec6726
    powerlift_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PowerliftIncidentMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PowerliftIncidentMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PowerliftIncidentMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "clientVersion": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "createdAtDateTime": lambda n : setattr(self, 'created_at_date_time', n.get_datetime_value()),
            "easyId": lambda n : setattr(self, 'easy_id', n.get_str_value()),
            "fileNames": lambda n : setattr(self, 'file_names', n.get_collection_of_primitive_values(str)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "powerliftId": lambda n : setattr(self, 'powerlift_id', n.get_uuid_value()),
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
        writer.write_str_value("application", self.application)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_datetime_value("createdAtDateTime", self.created_at_date_time)
        writer.write_str_value("easyId", self.easy_id)
        writer.write_collection_of_primitive_values("fileNames", self.file_names)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("platform", self.platform)
        writer.write_uuid_value("powerliftId", self.powerlift_id)
        writer.write_additional_data_value(self.additional_data)
    

