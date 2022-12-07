from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_state = lazy_import('msgraph.generated.models.security.content_state')
key_value_pair = lazy_import('msgraph.generated.models.security.key_value_pair')

class ContentInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new contentInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The format of the content to be labeled. Possible values are: file, email.
        self._content_format: Optional[str] = None
        # Identifier used for Azure Information Protection Analytics.
        self._identifier: Optional[str] = None
        # Existing Microsoft Purview Information Protection metadata is passed as key-value pairs, where the key is the MSIP_Label_GUID_PropName.
        self._metadata: Optional[List[key_value_pair.KeyValuePair]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state property
        self._state: Optional[content_state.ContentState] = None
    
    @property
    def content_format(self,) -> Optional[str]:
        """
        Gets the contentFormat property value. The format of the content to be labeled. Possible values are: file, email.
        Returns: Optional[str]
        """
        return self._content_format
    
    @content_format.setter
    def content_format(self,value: Optional[str] = None) -> None:
        """
        Sets the contentFormat property value. The format of the content to be labeled. Possible values are: file, email.
        Args:
            value: Value to set for the contentFormat property.
        """
        self._content_format = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_format": lambda n : setattr(self, 'content_format', n.get_str_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(content_state.ContentState)),
        }
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. Identifier used for Azure Information Protection Analytics.
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. Identifier used for Azure Information Protection Analytics.
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
    @property
    def metadata(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the metadata property value. Existing Microsoft Purview Information Protection metadata is passed as key-value pairs, where the key is the MSIP_Label_GUID_PropName.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the metadata property value. Existing Microsoft Purview Information Protection metadata is passed as key-value pairs, where the key is the MSIP_Label_GUID_PropName.
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contentFormat", self.content_format)
        writer.write_str_value("identifier", self.identifier)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[content_state.ContentState]:
        """
        Gets the state property value. The state property
        Returns: Optional[content_state.ContentState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[content_state.ContentState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

