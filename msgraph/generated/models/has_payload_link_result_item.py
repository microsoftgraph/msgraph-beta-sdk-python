from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_source = lazy_import('msgraph.generated.models.device_and_app_management_assignment_source')

class HasPayloadLinkResultItem(AdditionalDataHolder, Parsable):
    """
    A class containing the result of HasPayloadLinks action.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new hasPayloadLinkResultItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Exception information indicates if check for this item was successful or not.Empty string for no error.
        self._error: Optional[str] = None
        # Indicate whether a payload has any link or not.
        self._has_link: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Key of the Payload, In the format of Guid.
        self._payload_id: Optional[str] = None
        # The reason where the link comes from.
        self._sources: Optional[List[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]] = None
    
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
    
    @property
    def error(self,) -> Optional[str]:
        """
        Gets the error property value. Exception information indicates if check for this item was successful or not.Empty string for no error.
        Returns: Optional[str]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[str] = None) -> None:
        """
        Sets the error property value. Exception information indicates if check for this item was successful or not.Empty string for no error.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "has_link": lambda n : setattr(self, 'has_link', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payload_id": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_enum_values(device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource)),
        }
        return fields
    
    @property
    def has_link(self,) -> Optional[bool]:
        """
        Gets the hasLink property value. Indicate whether a payload has any link or not.
        Returns: Optional[bool]
        """
        return self._has_link
    
    @has_link.setter
    def has_link(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasLink property value. Indicate whether a payload has any link or not.
        Args:
            value: Value to set for the hasLink property.
        """
        self._has_link = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. Key of the Payload, In the format of Guid.
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. Key of the Payload, In the format of Guid.
        Args:
            value: Value to set for the payloadId property.
        """
        self._payload_id = value
    
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
    
    @property
    def sources(self,) -> Optional[List[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]]:
        """
        Gets the sources property value. The reason where the link comes from.
        Returns: Optional[List[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]]
        """
        return self._sources
    
    @sources.setter
    def sources(self,value: Optional[List[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]] = None) -> None:
        """
        Sets the sources property value. The reason where the link comes from.
        Args:
            value: Value to set for the sources property.
        """
        self._sources = value
    

