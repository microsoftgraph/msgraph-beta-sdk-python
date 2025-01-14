from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PowerliftIncidentDetail(AdditionalDataHolder, BackedModel, Parsable):
    """
    This type contains specific information regarding a Powerlift incident, such as when it was uploaded, the platform the device was on, and a string array of files associated to the incident.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # TThe name of the application for which the diagnostic is collected. Example: com.microsoft.CompanyPortal
    application_name: Optional[str] = None
    # The version of the application for which the diagnostic is collected. Example: 5.2203.1
    client_application_version: Optional[str] = None
    # The time the app diagnostic was created. The value cannot be modified and is automatically populated when the diagnostic is uploaded. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.Example: 2022-04-19T17:24:45.313Z
    created_date_time: Optional[datetime.datetime] = None
    # The unique app diagnostic identifier as a user friendly 8 character hexadecimal string. This id is smaller compared to the powerliftId. Th Example: 8520467A
    easy_id: Optional[str] = None
    # A list of files that are associated with the diagnostic.
    file_names: Optional[list[str]] = None
    # The locale information of the application for which the diagnostic is collected. Example: en-US
    locale: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system of the device from which diagnostics are collected. Example: iOS
    platform_display_name: Optional[str] = None
    # The unique identifier of the app diagnostic. This id is assigned to a diagnostic when it is uploaded to Powerlift. Example: 8520467a-49a9-44a4-8447-8dfb8bec6726
    powerlift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PowerliftIncidentDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PowerliftIncidentDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PowerliftIncidentDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "applicationName": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "clientApplicationVersion": lambda n : setattr(self, 'client_application_version', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "easyId": lambda n : setattr(self, 'easy_id', n.get_str_value()),
            "fileNames": lambda n : setattr(self, 'file_names', n.get_collection_of_primitive_values(str)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platformDisplayName": lambda n : setattr(self, 'platform_display_name', n.get_str_value()),
            "powerliftId": lambda n : setattr(self, 'powerlift_id', n.get_str_value()),
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
        writer.write_str_value("applicationName", self.application_name)
        writer.write_str_value("clientApplicationVersion", self.client_application_version)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("easyId", self.easy_id)
        writer.write_collection_of_primitive_values("fileNames", self.file_names)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("platformDisplayName", self.platform_display_name)
        writer.write_str_value("powerliftId", self.powerlift_id)
        writer.write_additional_data_value(self.additional_data)
    

