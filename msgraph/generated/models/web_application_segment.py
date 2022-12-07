from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_segment = lazy_import('msgraph.generated.models.application_segment')
cors_configuration_v2 = lazy_import('msgraph.generated.models.cors_configuration_v2')

class WebApplicationSegment(application_segment.ApplicationSegment):
    @property
    def alternate_url(self,) -> Optional[str]:
        """
        Gets the alternateUrl property value. The alternateUrl property
        Returns: Optional[str]
        """
        return self._alternate_url
    
    @alternate_url.setter
    def alternate_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateUrl property value. The alternateUrl property
        Args:
            value: Value to set for the alternateUrl property.
        """
        self._alternate_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WebApplicationSegment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.webApplicationSegment"
        # The alternateUrl property
        self._alternate_url: Optional[str] = None
        # The corsConfigurations property
        self._cors_configurations: Optional[List[cors_configuration_v2.CorsConfiguration_v2]] = None
        # The externalUrl property
        self._external_url: Optional[str] = None
        # The internalUrl property
        self._internal_url: Optional[str] = None
    
    @property
    def cors_configurations(self,) -> Optional[List[cors_configuration_v2.CorsConfiguration_v2]]:
        """
        Gets the corsConfigurations property value. The corsConfigurations property
        Returns: Optional[List[cors_configuration_v2.CorsConfiguration_v2]]
        """
        return self._cors_configurations
    
    @cors_configurations.setter
    def cors_configurations(self,value: Optional[List[cors_configuration_v2.CorsConfiguration_v2]] = None) -> None:
        """
        Sets the corsConfigurations property value. The corsConfigurations property
        Args:
            value: Value to set for the corsConfigurations property.
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
        Gets the externalUrl property value. The externalUrl property
        Returns: Optional[str]
        """
        return self._external_url
    
    @external_url.setter
    def external_url(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUrl property value. The externalUrl property
        Args:
            value: Value to set for the externalUrl property.
        """
        self._external_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alternate_url": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "cors_configurations": lambda n : setattr(self, 'cors_configurations', n.get_collection_of_object_values(cors_configuration_v2.CorsConfiguration_v2)),
            "external_url": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internal_url": lambda n : setattr(self, 'internal_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internal_url(self,) -> Optional[str]:
        """
        Gets the internalUrl property value. The internalUrl property
        Returns: Optional[str]
        """
        return self._internal_url
    
    @internal_url.setter
    def internal_url(self,value: Optional[str] = None) -> None:
        """
        Sets the internalUrl property value. The internalUrl property
        Args:
            value: Value to set for the internalUrl property.
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
    

