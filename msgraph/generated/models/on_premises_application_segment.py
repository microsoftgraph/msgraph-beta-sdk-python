from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cors_configuration = lazy_import('msgraph.generated.models.cors_configuration')

class OnPremisesApplicationSegment(AdditionalDataHolder, Parsable):
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
    def alternate_url(self,) -> Optional[str]:
        """
        Gets the alternateUrl property value. If you're configuring a traffic manager in front of multiple App Proxy application segments, contains the user-friendly URL that will point to the traffic manager.
        Returns: Optional[str]
        """
        return self._alternate_url
    
    @alternate_url.setter
    def alternate_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateUrl property value. If you're configuring a traffic manager in front of multiple App Proxy application segments, contains the user-friendly URL that will point to the traffic manager.
        Args:
            value: Value to set for the alternateUrl property.
        """
        self._alternate_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesApplicationSegment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If you're configuring a traffic manager in front of multiple App Proxy application segments, contains the user-friendly URL that will point to the traffic manager.
        self._alternate_url: Optional[str] = None
        # CORS Rule definition for a particular application segment.
        self._cors_configurations: Optional[List[cors_configuration.CorsConfiguration]] = None
        # The published external URL for the application segment; for example, https://intranet.contoso.com./
        self._external_url: Optional[str] = None
        # The internal URL of the application segment; for example, https://intranet/.
        self._internal_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def cors_configurations(self,) -> Optional[List[cors_configuration.CorsConfiguration]]:
        """
        Gets the corsConfigurations property value. CORS Rule definition for a particular application segment.
        Returns: Optional[List[cors_configuration.CorsConfiguration]]
        """
        return self._cors_configurations
    
    @cors_configurations.setter
    def cors_configurations(self,value: Optional[List[cors_configuration.CorsConfiguration]] = None) -> None:
        """
        Sets the corsConfigurations property value. CORS Rule definition for a particular application segment.
        Args:
            value: Value to set for the corsConfigurations property.
        """
        self._cors_configurations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesApplicationSegment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesApplicationSegment()
    
    @property
    def external_url(self,) -> Optional[str]:
        """
        Gets the externalUrl property value. The published external URL for the application segment; for example, https://intranet.contoso.com./
        Returns: Optional[str]
        """
        return self._external_url
    
    @external_url.setter
    def external_url(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUrl property value. The published external URL for the application segment; for example, https://intranet.contoso.com./
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
            "cors_configurations": lambda n : setattr(self, 'cors_configurations', n.get_collection_of_object_values(cors_configuration.CorsConfiguration)),
            "external_url": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internal_url": lambda n : setattr(self, 'internal_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
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
            value: Value to set for the internalUrl property.
        """
        self._internal_url = value
    
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
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_collection_of_object_values("corsConfigurations", self.cors_configurations)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

