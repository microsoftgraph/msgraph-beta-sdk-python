from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')

class AnswerVariant(AdditionalDataHolder, Parsable):
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
        Instantiates a new answerVariant and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Answer variation description shown on search results page.
        self._description: Optional[str] = None
        # Answer variation name displayed in search results.
        self._display_name: Optional[str] = None
        # The languageTag property
        self._language_tag: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The platform property
        self._platform: Optional[device_platform_type.DevicePlatformType] = None
        # Answer variation URL link. When users click this answer variation in search results, they will go to this URL.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnswerVariant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnswerVariant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AnswerVariant()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Answer variation description shown on search results page.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Answer variation description shown on search results page.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Answer variation name displayed in search results.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Answer variation name displayed in search results.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The languageTag property
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The languageTag property
        Args:
            value: Value to set for the languageTag property.
        """
        self._language_tag = value
    
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
    def platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the platform property value. The platform property
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the platform property value. The platform property
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Answer variation URL link. When users click this answer variation in search results, they will go to this URL.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Answer variation URL link. When users click this answer variation in search results, they will go to this URL.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

