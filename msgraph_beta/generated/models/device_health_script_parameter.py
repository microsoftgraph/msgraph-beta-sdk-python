from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
    from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
    from .device_health_script_string_parameter import DeviceHealthScriptStringParameter

@dataclass
class DeviceHealthScriptParameter(AdditionalDataHolder, BackedModel, Parsable):
    """
    Base properties of the script parameter.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Whether Apply DefaultValue When Not Assigned
    apply_default_value_when_not_assigned: Optional[bool] = None
    # The description of the param
    description: Optional[str] = None
    # Whether the param is required
    is_required: Optional[bool] = None
    # The name of the param
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptParameter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptBooleanParameter".casefold():
            from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter

            return DeviceHealthScriptBooleanParameter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptIntegerParameter".casefold():
            from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter

            return DeviceHealthScriptIntegerParameter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptStringParameter".casefold():
            from .device_health_script_string_parameter import DeviceHealthScriptStringParameter

            return DeviceHealthScriptStringParameter()
        return DeviceHealthScriptParameter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
        from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
        from .device_health_script_string_parameter import DeviceHealthScriptStringParameter

        from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
        from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
        from .device_health_script_string_parameter import DeviceHealthScriptStringParameter

        fields: Dict[str, Callable[[Any], None]] = {
            "applyDefaultValueWhenNotAssigned": lambda n : setattr(self, 'apply_default_value_when_not_assigned', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("applyDefaultValueWhenNotAssigned", self.apply_default_value_when_not_assigned)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

