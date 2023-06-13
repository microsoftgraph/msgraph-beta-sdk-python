from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PowerliftDownloadRequest(AdditionalDataHolder, Parsable):
    """
    Request used to download app diagnostic files.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The list of files to download
    files: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique id for the request
    powerlift_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PowerliftDownloadRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PowerliftDownloadRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PowerliftDownloadRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "files": lambda n : setattr(self, 'files', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "powerliftId": lambda n : setattr(self, 'powerlift_id', n.get_uuid_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("files", self.files)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("powerliftId", self.powerlift_id)
        writer.write_additional_data_value(self.additional_data)
    

