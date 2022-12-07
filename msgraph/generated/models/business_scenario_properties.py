from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BusinessScenarioProperties(AdditionalDataHolder, Parsable):
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
        Instantiates a new businessScenarioProperties and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The externalBucketId property
        self._external_bucket_id: Optional[str] = None
        # The externalContextId property
        self._external_context_id: Optional[str] = None
        # The externalObjectId property
        self._external_object_id: Optional[str] = None
        # The externalObjectVersion property
        self._external_object_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The webUrl property
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioProperties()
    
    @property
    def external_bucket_id(self,) -> Optional[str]:
        """
        Gets the externalBucketId property value. The externalBucketId property
        Returns: Optional[str]
        """
        return self._external_bucket_id
    
    @external_bucket_id.setter
    def external_bucket_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalBucketId property value. The externalBucketId property
        Args:
            value: Value to set for the externalBucketId property.
        """
        self._external_bucket_id = value
    
    @property
    def external_context_id(self,) -> Optional[str]:
        """
        Gets the externalContextId property value. The externalContextId property
        Returns: Optional[str]
        """
        return self._external_context_id
    
    @external_context_id.setter
    def external_context_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalContextId property value. The externalContextId property
        Args:
            value: Value to set for the externalContextId property.
        """
        self._external_context_id = value
    
    @property
    def external_object_id(self,) -> Optional[str]:
        """
        Gets the externalObjectId property value. The externalObjectId property
        Returns: Optional[str]
        """
        return self._external_object_id
    
    @external_object_id.setter
    def external_object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectId property value. The externalObjectId property
        Args:
            value: Value to set for the externalObjectId property.
        """
        self._external_object_id = value
    
    @property
    def external_object_version(self,) -> Optional[str]:
        """
        Gets the externalObjectVersion property value. The externalObjectVersion property
        Returns: Optional[str]
        """
        return self._external_object_version
    
    @external_object_version.setter
    def external_object_version(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectVersion property value. The externalObjectVersion property
        Args:
            value: Value to set for the externalObjectVersion property.
        """
        self._external_object_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "external_bucket_id": lambda n : setattr(self, 'external_bucket_id', n.get_str_value()),
            "external_context_id": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "external_object_id": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
            "external_object_version": lambda n : setattr(self, 'external_object_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("externalBucketId", self.external_bucket_id)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
        writer.write_str_value("externalObjectVersion", self.external_object_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The webUrl property
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The webUrl property
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

