from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')

class DeviceManagementSettingDependency(AdditionalDataHolder, Parsable):
    """
    Dependency information for a setting
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
    def constraints(self,) -> Optional[List[device_management_constraint.DeviceManagementConstraint]]:
        """
        Gets the constraints property value. Collection of constraints for the dependency setting value
        Returns: Optional[List[device_management_constraint.DeviceManagementConstraint]]
        """
        return self._constraints
    
    @constraints.setter
    def constraints(self,value: Optional[List[device_management_constraint.DeviceManagementConstraint]] = None) -> None:
        """
        Sets the constraints property value. Collection of constraints for the dependency setting value
        Args:
            value: Value to set for the constraints property.
        """
        self._constraints = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingDependency and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Collection of constraints for the dependency setting value
        self._constraints: Optional[List[device_management_constraint.DeviceManagementConstraint]] = None
        # The setting definition ID of the setting depended on
        self._definition_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingDependency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingDependency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingDependency()
    
    @property
    def definition_id(self,) -> Optional[str]:
        """
        Gets the definitionId property value. The setting definition ID of the setting depended on
        Returns: Optional[str]
        """
        return self._definition_id
    
    @definition_id.setter
    def definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the definitionId property value. The setting definition ID of the setting depended on
        Args:
            value: Value to set for the definitionId property.
        """
        self._definition_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "constraints": lambda n : setattr(self, 'constraints', n.get_collection_of_object_values(device_management_constraint.DeviceManagementConstraint)),
            "definition_id": lambda n : setattr(self, 'definition_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("constraints", self.constraints)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

