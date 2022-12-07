from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

warranty_offer = lazy_import('msgraph.generated.models.warranty_offer')

class OemWarranty(AdditionalDataHolder, Parsable):
    """
    OEM Warranty information for a given device
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
    
    @property
    def additional_warranties(self,) -> Optional[List[warranty_offer.WarrantyOffer]]:
        """
        Gets the additionalWarranties property value. List of additional warranty offers. This collection can contain a maximum of 100 elements.
        Returns: Optional[List[warranty_offer.WarrantyOffer]]
        """
        return self._additional_warranties
    
    @additional_warranties.setter
    def additional_warranties(self,value: Optional[List[warranty_offer.WarrantyOffer]] = None) -> None:
        """
        Sets the additionalWarranties property value. List of additional warranty offers. This collection can contain a maximum of 100 elements.
        Args:
            value: Value to set for the additionalWarranties property.
        """
        self._additional_warranties = value
    
    @property
    def base_warranties(self,) -> Optional[List[warranty_offer.WarrantyOffer]]:
        """
        Gets the baseWarranties property value. List of base warranty offers. This collection can contain a maximum of 100 elements.
        Returns: Optional[List[warranty_offer.WarrantyOffer]]
        """
        return self._base_warranties
    
    @base_warranties.setter
    def base_warranties(self,value: Optional[List[warranty_offer.WarrantyOffer]] = None) -> None:
        """
        Sets the baseWarranties property value. List of base warranty offers. This collection can contain a maximum of 100 elements.
        Args:
            value: Value to set for the baseWarranties property.
        """
        self._base_warranties = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new oemWarranty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of additional warranty offers. This collection can contain a maximum of 100 elements.
        self._additional_warranties: Optional[List[warranty_offer.WarrantyOffer]] = None
        # List of base warranty offers. This collection can contain a maximum of 100 elements.
        self._base_warranties: Optional[List[warranty_offer.WarrantyOffer]] = None
        # Device configuration page URL
        self._device_configuration_url: Optional[str] = None
        # Device warranty page URL
        self._device_warranty_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OemWarranty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OemWarranty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OemWarranty()
    
    @property
    def device_configuration_url(self,) -> Optional[str]:
        """
        Gets the deviceConfigurationUrl property value. Device configuration page URL
        Returns: Optional[str]
        """
        return self._device_configuration_url
    
    @device_configuration_url.setter
    def device_configuration_url(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceConfigurationUrl property value. Device configuration page URL
        Args:
            value: Value to set for the deviceConfigurationUrl property.
        """
        self._device_configuration_url = value
    
    @property
    def device_warranty_url(self,) -> Optional[str]:
        """
        Gets the deviceWarrantyUrl property value. Device warranty page URL
        Returns: Optional[str]
        """
        return self._device_warranty_url
    
    @device_warranty_url.setter
    def device_warranty_url(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceWarrantyUrl property value. Device warranty page URL
        Args:
            value: Value to set for the deviceWarrantyUrl property.
        """
        self._device_warranty_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_warranties": lambda n : setattr(self, 'additional_warranties', n.get_collection_of_object_values(warranty_offer.WarrantyOffer)),
            "base_warranties": lambda n : setattr(self, 'base_warranties', n.get_collection_of_object_values(warranty_offer.WarrantyOffer)),
            "device_configuration_url": lambda n : setattr(self, 'device_configuration_url', n.get_str_value()),
            "device_warranty_url": lambda n : setattr(self, 'device_warranty_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("additionalWarranties", self.additional_warranties)
        writer.write_collection_of_object_values("baseWarranties", self.base_warranties)
        writer.write_str_value("deviceConfigurationUrl", self.device_configuration_url)
        writer.write_str_value("deviceWarrantyUrl", self.device_warranty_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

