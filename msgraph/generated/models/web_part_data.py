from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')
server_processed_content = lazy_import('msgraph.generated.models.server_processed_content')

class WebPartData(AdditionalDataHolder, Parsable):
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
    
    @property
    def audiences(self,) -> Optional[List[str]]:
        """
        Gets the audiences property value. Audience information of the web part. By using this property, specific content will be prioritized to specific audiences.
        Returns: Optional[List[str]]
        """
        return self._audiences
    
    @audiences.setter
    def audiences(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the audiences property value. Audience information of the web part. By using this property, specific content will be prioritized to specific audiences.
        Args:
            value: Value to set for the audiences property.
        """
        self._audiences = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new webPartData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Audience information of the web part. By using this property, specific content will be prioritized to specific audiences.
        self._audiences: Optional[List[str]] = None
        # Data version of the web part. The value is defined by the web part developer. Different dataVersions usually refers to a different property structure.
        self._data_version: Optional[str] = None
        # Description of the web part.
        self._description: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Properties bag of the web part.
        self._properties: Optional[json.Json] = None
        # Contains collections of data that can be processed by server side services like search index and link fixup.
        self._server_processed_content: Optional[server_processed_content.ServerProcessedContent] = None
        # Title of the web part.
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebPartData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebPartData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebPartData()
    
    @property
    def data_version(self,) -> Optional[str]:
        """
        Gets the dataVersion property value. Data version of the web part. The value is defined by the web part developer. Different dataVersions usually refers to a different property structure.
        Returns: Optional[str]
        """
        return self._data_version
    
    @data_version.setter
    def data_version(self,value: Optional[str] = None) -> None:
        """
        Sets the dataVersion property value. Data version of the web part. The value is defined by the web part developer. Different dataVersions usually refers to a different property structure.
        Args:
            value: Value to set for the dataVersion property.
        """
        self._data_version = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the web part.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the web part.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audiences": lambda n : setattr(self, 'audiences', n.get_collection_of_primitive_values(str)),
            "data_version": lambda n : setattr(self, 'data_version', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(json.Json)),
            "server_processed_content": lambda n : setattr(self, 'server_processed_content', n.get_object_value(server_processed_content.ServerProcessedContent)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        return fields
    
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
    def properties(self,) -> Optional[json.Json]:
        """
        Gets the properties property value. Properties bag of the web part.
        Returns: Optional[json.Json]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the properties property value. Properties bag of the web part.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("audiences", self.audiences)
        writer.write_str_value("dataVersion", self.data_version)
        writer.write_str_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("properties", self.properties)
        writer.write_object_value("serverProcessedContent", self.server_processed_content)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def server_processed_content(self,) -> Optional[server_processed_content.ServerProcessedContent]:
        """
        Gets the serverProcessedContent property value. Contains collections of data that can be processed by server side services like search index and link fixup.
        Returns: Optional[server_processed_content.ServerProcessedContent]
        """
        return self._server_processed_content
    
    @server_processed_content.setter
    def server_processed_content(self,value: Optional[server_processed_content.ServerProcessedContent] = None) -> None:
        """
        Sets the serverProcessedContent property value. Contains collections of data that can be processed by server side services like search index and link fixup.
        Args:
            value: Value to set for the serverProcessedContent property.
        """
        self._server_processed_content = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Title of the web part.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Title of the web part.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

