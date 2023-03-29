from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import current_label, discovered_sensitive_type, dlp_evaluation_windows_devices_input

class DlpEvaluationInput(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new dlpEvaluationInput and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The currentLabel property
        self._current_label: Optional[current_label.CurrentLabel] = None
        # The discoveredSensitiveTypes property
        self._discovered_sensitive_types: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpEvaluationInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpEvaluationInput
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.dlpEvaluationWindowsDevicesInput":
                from . import dlp_evaluation_windows_devices_input

                return dlp_evaluation_windows_devices_input.DlpEvaluationWindowsDevicesInput()
        return DlpEvaluationInput()
    
    @property
    def current_label(self,) -> Optional[current_label.CurrentLabel]:
        """
        Gets the currentLabel property value. The currentLabel property
        Returns: Optional[current_label.CurrentLabel]
        """
        return self._current_label
    
    @current_label.setter
    def current_label(self,value: Optional[current_label.CurrentLabel] = None) -> None:
        """
        Sets the currentLabel property value. The currentLabel property
        Args:
            value: Value to set for the current_label property.
        """
        self._current_label = value
    
    @property
    def discovered_sensitive_types(self,) -> Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]]:
        """
        Gets the discoveredSensitiveTypes property value. The discoveredSensitiveTypes property
        Returns: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]]
        """
        return self._discovered_sensitive_types
    
    @discovered_sensitive_types.setter
    def discovered_sensitive_types(self,value: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]] = None) -> None:
        """
        Sets the discoveredSensitiveTypes property value. The discoveredSensitiveTypes property
        Args:
            value: Value to set for the discovered_sensitive_types property.
        """
        self._discovered_sensitive_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import current_label, discovered_sensitive_type, dlp_evaluation_windows_devices_input

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(current_label.CurrentLabel)),
            "discoveredSensitiveTypes": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(discovered_sensitive_type.DiscoveredSensitiveType)),
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
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

