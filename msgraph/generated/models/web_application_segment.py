from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_segment, cors_configuration_v2

from . import application_segment

class WebApplicationSegment(application_segment.ApplicationSegment):
    def __init__(self,) -> None:
        """
        Instantiates a new WebApplicationSegment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.webApplicationSegment"
        # If you're configuring a traffic manager in front of multiple App Proxy application segments, this property contains the user-friendly URL that will point to the traffic manager.
        self._alternate_url: Optional[str] = None
        # A collection of CORS Rule definitions for a particular application segment.
        self._cors_configurations: Optional[List[cors_configuration_v2.CorsConfiguration_v2]] = None
        # The published external URL for the application segment; for example, https://intranet.contoso.com/.
        self._external_url: Optional[str] = None
        # The internal URL of the application segment; for example, https://intranet/.
        self._internal_url: Optional[str] = None
    
    @property
    def alternate_url(self,) -> Optional[str]:
        """
        Gets the alternateUrl property value. If you're configuring a traffic manager in front of multiple App Proxy application segments, this property contains the user-friendly URL that will point to the traffic manager.
        Returns: Optional[str]
        """
        return self._alternate_url
    
    @alternate_url.setter
    def alternate_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateUrl property value. If you're configuring a traffic manager in front of multiple App Proxy application segments, this property contains the user-friendly URL that will point to the traffic manager.
        Args:
            value: Value to set for the alternate_url property.
        """
        self._alternate_url = value
    
    @property
    def cors_configurations(self,) -> Optional[List[cors_configuration_v2.CorsConfiguration_v2]]:
        """
        Gets the corsConfigurations property value. A collection of CORS Rule definitions for a particular application segment.
        Returns: Optional[List[cors_configuration_v2.CorsConfiguration_v2]]
        """
        return self._cors_configurations
    
    @cors_configurations.setter
    def cors_configurations(self,value: Optional[List[cors_configuration_v2.CorsConfiguration_v2]] = None) -> None:
        """
        Sets the corsConfigurations property value. A collection of CORS Rule definitions for a particular application segment.
        Args:
            value: Value to set for the cors_configurations property.
        """
        self._cors_configurations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationSegment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebApplicationSegment()
    
    @property
    def external_url(self,) -> Optional[str]:
        """
        Gets the externalUrl property value. The published external URL for the application segment; for example, https://intranet.contoso.com/.
        Returns: Optional[str]
        """
        return self._external_url
    
    @external_url.setter
    def external_url(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUrl property value. The published external URL for the application segment; for example, https://intranet.contoso.com/.
        Args:
            value: Value to set for the external_url property.
        """
        self._external_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_segment, cors_configuration_v2

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateUrl": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "corsConfigurations": lambda n : setattr(self, 'cors_configurations', n.get_collection_of_object_values(cors_configuration_v2.CorsConfiguration_v2)),
            "externalUrl": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internalUrl": lambda n : setattr(self, 'internal_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internal_url(self,) -> Optional[str]:
        """
        Gets the internalUrl property value. The internal URL of the application segment; for example, https://intranet/.
        Returns: Optional[str]
        """
        return self._internal_url
    
    @internal_url.setter
    def internal_url(self,value: Optional[str] = None) -> None:
        """
        Sets the internalUrl property value. The internal URL of the application segment; for example, https://intranet/.
        Args:
            value: Value to set for the internal_url property.
        """
        self._internal_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_collection_of_object_values("corsConfigurations", self.cors_configurations)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
    

