from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_source

@dataclass
class HasPayloadLinkResultItem(AdditionalDataHolder, Parsable):
    """
    A class containing the result of HasPayloadLinks action.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Exception information indicates if check for this item was successful or not.Empty string for no error.
    error: Optional[str] = None
    # Indicate whether a payload has any link or not.
    has_link: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Key of the Payload, In the format of Guid.
    payload_id: Optional[str] = None
    # The reason where the link comes from.
    sources: Optional[List[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HasPayloadLinkResultItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HasPayloadLinkResultItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HasPayloadLinkResultItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_source

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "hasLink": lambda n : setattr(self, 'has_link', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_enum_values(device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource)),
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
        writer.write_str_value("error", self.error)
        writer.write_bool_value("hasLink", self.has_link)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("sources", self.sources)
        writer.write_additional_data_value(self.additional_data)
    

