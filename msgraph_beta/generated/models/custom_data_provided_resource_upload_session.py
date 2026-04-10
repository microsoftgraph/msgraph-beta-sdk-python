from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
    from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
    from .custom_extension_data import CustomExtensionData
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomDataProvidedResourceUploadSession(Entity, Parsable):
    # DateTime when the upload session was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # An object containing the context for which this data is being uploaded. Currently the only possible concrete type is accessReviewResourceDataUploadSessionContextData
    data: Optional[CustomExtensionData] = None
    # Indicates if all the necessary files have been uploaded to this session.
    is_upload_done: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the access data. This should be set to the customdataprovidedresource's name when creating the session.
    source: Optional[str] = None
    # The stats property
    stats: Optional[CustomDataProvidedResourceUploadStats] = None
    # The status property
    status: Optional[CustomDataProvidedResourceUploadStatus] = None
    # Schematized form of the expected CSV columns in the uploaded file. The only possible value currently is: accessReviewDataUploadTriggerCallbackData
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomDataProvidedResourceUploadSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomDataProvidedResourceUploadSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomDataProvidedResourceUploadSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
        from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
        from .custom_extension_data import CustomExtensionData
        from .entity import Entity

        from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
        from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
        from .custom_extension_data import CustomExtensionData
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "data": lambda n : setattr(self, 'data', n.get_object_value(CustomExtensionData)),
            "isUploadDone": lambda n : setattr(self, 'is_upload_done', n.get_bool_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "stats": lambda n : setattr(self, 'stats', n.get_object_value(CustomDataProvidedResourceUploadStats)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomDataProvidedResourceUploadStatus)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("data", self.data)
        writer.write_bool_value("isUploadDone", self.is_upload_done)
        writer.write_str_value("source", self.source)
        writer.write_object_value("stats", self.stats)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("type", self.type)
    

