from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceHealthScriptParameter(AdditionalDataHolder, Parsable):
    """
    Base properties of the script parameter.
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
    def apply_default_value_when_not_assigned(self,) -> Optional[bool]:
        """
        Gets the applyDefaultValueWhenNotAssigned property value. Whether Apply DefaultValue When Not Assigned
        Returns: Optional[bool]
        """
        return self._apply_default_value_when_not_assigned
    
    @apply_default_value_when_not_assigned.setter
    def apply_default_value_when_not_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyDefaultValueWhenNotAssigned property value. Whether Apply DefaultValue When Not Assigned
        Args:
            value: Value to set for the applyDefaultValueWhenNotAssigned property.
        """
        self._apply_default_value_when_not_assigned = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptParameter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether Apply DefaultValue When Not Assigned
        self._apply_default_value_when_not_assigned: Optional[bool] = None
        # The description of the param
        self._description: Optional[str] = None
        # Whether the param is required
        self._is_required: Optional[bool] = None
        # The name of the param
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptParameter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptParameter()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the param
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the param
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apply_default_value_when_not_assigned": lambda n : setattr(self, 'apply_default_value_when_not_assigned', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Whether the param is required
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Whether the param is required
        Args:
            value: Value to set for the isRequired property.
        """
        self._is_required = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the param
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the param
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_bool_value("applyDefaultValueWhenNotAssigned", self.apply_default_value_when_not_assigned)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

