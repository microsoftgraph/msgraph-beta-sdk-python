from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DataProcessorServiceForWindowsFeaturesOnboarding(AdditionalDataHolder, BackedModel, Parsable):
    """
    A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When TRUE, the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When FALSE, the tenant has not enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. Default value is FALSE.
    are_data_processor_service_for_windows_features_enabled: Optional[bool] = None
    # Indicates whether the tenant has required Windows license. When TRUE, the tenant has the required Windows license. When FALSE, the tenant does not have the required Windows license. Default value is FALSE.
    has_valid_windows_license: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataProcessorServiceForWindowsFeaturesOnboarding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataProcessorServiceForWindowsFeaturesOnboarding
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataProcessorServiceForWindowsFeaturesOnboarding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "areDataProcessorServiceForWindowsFeaturesEnabled": lambda n : setattr(self, 'are_data_processor_service_for_windows_features_enabled', n.get_bool_value()),
            "hasValidWindowsLicense": lambda n : setattr(self, 'has_valid_windows_license', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("areDataProcessorServiceForWindowsFeaturesEnabled", self.are_data_processor_service_for_windows_features_enabled)
        writer.write_bool_value("hasValidWindowsLicense", self.has_valid_windows_license)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

