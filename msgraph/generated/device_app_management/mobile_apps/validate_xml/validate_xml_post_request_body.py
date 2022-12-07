from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ValidateXmlPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the validateXml method.
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
        Instantiates a new validateXmlPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The officeConfigurationXml property
        self._office_configuration_xml: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateXmlPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateXmlPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateXmlPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "office_configuration_xml": lambda n : setattr(self, 'office_configuration_xml', n.get_bytes_value()),
        }
        return fields
    
    @property
    def office_configuration_xml(self,) -> Optional[bytes]:
        """
        Gets the officeConfigurationXml property value. The officeConfigurationXml property
        Returns: Optional[bytes]
        """
        return self._office_configuration_xml
    
    @office_configuration_xml.setter
    def office_configuration_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the officeConfigurationXml property value. The officeConfigurationXml property
        Args:
            value: Value to set for the officeConfigurationXml property.
        """
        self._office_configuration_xml = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("officeConfigurationXml", self.office_configuration_xml)
        writer.write_additional_data_value(self.additional_data)
    

