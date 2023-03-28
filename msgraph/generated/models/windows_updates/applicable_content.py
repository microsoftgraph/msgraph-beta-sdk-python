from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import applicable_content_device_match, catalog_entry

class ApplicableContent(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new applicableContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The catalogEntry property
        self._catalog_entry: Optional[catalog_entry.CatalogEntry] = None
        # Collection of devices and recommendations for applicable catalog content.
        self._matched_devices: Optional[List[applicable_content_device_match.ApplicableContentDeviceMatch]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def catalog_entry(self,) -> Optional[catalog_entry.CatalogEntry]:
        """
        Gets the catalogEntry property value. The catalogEntry property
        Returns: Optional[catalog_entry.CatalogEntry]
        """
        return self._catalog_entry
    
    @catalog_entry.setter
    def catalog_entry(self,value: Optional[catalog_entry.CatalogEntry] = None) -> None:
        """
        Sets the catalogEntry property value. The catalogEntry property
        Args:
            value: Value to set for the catalog_entry property.
        """
        self._catalog_entry = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicableContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicableContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicableContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import applicable_content_device_match, catalog_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(catalog_entry.CatalogEntry)),
            "matchedDevices": lambda n : setattr(self, 'matched_devices', n.get_collection_of_object_values(applicable_content_device_match.ApplicableContentDeviceMatch)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def matched_devices(self,) -> Optional[List[applicable_content_device_match.ApplicableContentDeviceMatch]]:
        """
        Gets the matchedDevices property value. Collection of devices and recommendations for applicable catalog content.
        Returns: Optional[List[applicable_content_device_match.ApplicableContentDeviceMatch]]
        """
        return self._matched_devices
    
    @matched_devices.setter
    def matched_devices(self,value: Optional[List[applicable_content_device_match.ApplicableContentDeviceMatch]] = None) -> None:
        """
        Sets the matchedDevices property value. Collection of devices and recommendations for applicable catalog content.
        Args:
            value: Value to set for the matched_devices property.
        """
        self._matched_devices = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_collection_of_object_values("matchedDevices", self.matched_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

