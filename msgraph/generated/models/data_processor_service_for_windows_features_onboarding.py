from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DataProcessorServiceForWindowsFeaturesOnboarding(AdditionalDataHolder, Parsable):
    """
    A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
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
    def are_data_processor_service_for_windows_features_enabled(self,) -> Optional[bool]:
        """
        Gets the areDataProcessorServiceForWindowsFeaturesEnabled property value. Indicates whether the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When TRUE, the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When FALSE, the tenant has not enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._are_data_processor_service_for_windows_features_enabled
    
    @are_data_processor_service_for_windows_features_enabled.setter
    def are_data_processor_service_for_windows_features_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the areDataProcessorServiceForWindowsFeaturesEnabled property value. Indicates whether the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When TRUE, the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When FALSE, the tenant has not enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. Default value is FALSE.
        Args:
            value: Value to set for the areDataProcessorServiceForWindowsFeaturesEnabled property.
        """
        self._are_data_processor_service_for_windows_features_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new dataProcessorServiceForWindowsFeaturesOnboarding and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When TRUE, the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When FALSE, the tenant has not enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. Default value is FALSE.
        self._are_data_processor_service_for_windows_features_enabled: Optional[bool] = None
        # Indicates whether the tenant has required Windows license. When TRUE, the tenant has the required Windows license. When FALSE, the tenant does not have the required Windows license. Default value is FALSE.
        self._has_valid_windows_license: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataProcessorServiceForWindowsFeaturesOnboarding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataProcessorServiceForWindowsFeaturesOnboarding
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataProcessorServiceForWindowsFeaturesOnboarding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "are_data_processor_service_for_windows_features_enabled": lambda n : setattr(self, 'are_data_processor_service_for_windows_features_enabled', n.get_bool_value()),
            "has_valid_windows_license": lambda n : setattr(self, 'has_valid_windows_license', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def has_valid_windows_license(self,) -> Optional[bool]:
        """
        Gets the hasValidWindowsLicense property value. Indicates whether the tenant has required Windows license. When TRUE, the tenant has the required Windows license. When FALSE, the tenant does not have the required Windows license. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._has_valid_windows_license
    
    @has_valid_windows_license.setter
    def has_valid_windows_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasValidWindowsLicense property value. Indicates whether the tenant has required Windows license. When TRUE, the tenant has the required Windows license. When FALSE, the tenant does not have the required Windows license. Default value is FALSE.
        Args:
            value: Value to set for the hasValidWindowsLicense property.
        """
        self._has_valid_windows_license = value
    
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
        writer.write_bool_value("areDataProcessorServiceForWindowsFeaturesEnabled", self.are_data_processor_service_for_windows_features_enabled)
        writer.write_bool_value("hasValidWindowsLicense", self.has_valid_windows_license)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

