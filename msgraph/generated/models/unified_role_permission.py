from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UnifiedRolePermission(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRolePermission and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Set of tasks that can be performed on a resource.
        self._allowed_resource_actions: Optional[List[str]] = None
        # Optional constraints that must be met for the permission to be effective. Not supported for custom roles.
        self._condition: Optional[str] = None
        # The excludedResourceActions property
        self._excluded_resource_actions: Optional[List[str]] = None
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
    def allowed_resource_actions(self,) -> Optional[List[str]]:
        """
        Gets the allowedResourceActions property value. Set of tasks that can be performed on a resource.
        Returns: Optional[List[str]]
        """
        return self._allowed_resource_actions
    
    @allowed_resource_actions.setter
    def allowed_resource_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedResourceActions property value. Set of tasks that can be performed on a resource.
        Args:
            value: Value to set for the allowed_resource_actions property.
        """
        self._allowed_resource_actions = value
    
    @property
    def condition(self,) -> Optional[str]:
        """
        Gets the condition property value. Optional constraints that must be met for the permission to be effective. Not supported for custom roles.
        Returns: Optional[str]
        """
        return self._condition
    
    @condition.setter
    def condition(self,value: Optional[str] = None) -> None:
        """
        Sets the condition property value. Optional constraints that must be met for the permission to be effective. Not supported for custom roles.
        Args:
            value: Value to set for the condition property.
        """
        self._condition = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRolePermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRolePermission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRolePermission()
    
    @property
    def excluded_resource_actions(self,) -> Optional[List[str]]:
        """
        Gets the excludedResourceActions property value. The excludedResourceActions property
        Returns: Optional[List[str]]
        """
        return self._excluded_resource_actions
    
    @excluded_resource_actions.setter
    def excluded_resource_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludedResourceActions property value. The excludedResourceActions property
        Args:
            value: Value to set for the excluded_resource_actions property.
        """
        self._excluded_resource_actions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedResourceActions": lambda n : setattr(self, 'allowed_resource_actions', n.get_collection_of_primitive_values(str)),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "excludedResourceActions": lambda n : setattr(self, 'excluded_resource_actions', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedResourceActions", self.allowed_resource_actions)
        writer.write_str_value("condition", self.condition)
        writer.write_collection_of_primitive_values("excludedResourceActions", self.excluded_resource_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

