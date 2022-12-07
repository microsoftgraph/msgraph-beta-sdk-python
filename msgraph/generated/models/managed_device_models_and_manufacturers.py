from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ManagedDeviceModelsAndManufacturers(AdditionalDataHolder, Parsable):
    """
    Models and Manufactures meatadata for managed devices in the account
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
        Instantiates a new managedDeviceModelsAndManufacturers and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of Manufactures for managed devices in the account
        self._device_manufacturers: Optional[List[str]] = None
        # List of Models for managed devices in the account
        self._device_models: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceModelsAndManufacturers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceModelsAndManufacturers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceModelsAndManufacturers()
    
    @property
    def device_manufacturers(self,) -> Optional[List[str]]:
        """
        Gets the deviceManufacturers property value. List of Manufactures for managed devices in the account
        Returns: Optional[List[str]]
        """
        return self._device_manufacturers
    
    @device_manufacturers.setter
    def device_manufacturers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deviceManufacturers property value. List of Manufactures for managed devices in the account
        Args:
            value: Value to set for the deviceManufacturers property.
        """
        self._device_manufacturers = value
    
    @property
    def device_models(self,) -> Optional[List[str]]:
        """
        Gets the deviceModels property value. List of Models for managed devices in the account
        Returns: Optional[List[str]]
        """
        return self._device_models
    
    @device_models.setter
    def device_models(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deviceModels property value. List of Models for managed devices in the account
        Args:
            value: Value to set for the deviceModels property.
        """
        self._device_models = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_manufacturers": lambda n : setattr(self, 'device_manufacturers', n.get_collection_of_primitive_values(str)),
            "device_models": lambda n : setattr(self, 'device_models', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("deviceManufacturers", self.device_manufacturers)
        writer.write_collection_of_primitive_values("deviceModels", self.device_models)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

