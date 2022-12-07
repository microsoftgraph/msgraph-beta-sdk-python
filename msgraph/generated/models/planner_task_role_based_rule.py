from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_task_configuration_role_base = lazy_import('msgraph.generated.models.planner_task_configuration_role_base')
planner_task_property_rule = lazy_import('msgraph.generated.models.planner_task_property_rule')

class PlannerTaskRoleBasedRule(AdditionalDataHolder, Parsable):
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
        Instantiates a new plannerTaskRoleBasedRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The defaultRule property
        self._default_rule: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The propertyRule property
        self._property_rule: Optional[planner_task_property_rule.PlannerTaskPropertyRule] = None
        # The role property
        self._role: Optional[planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskRoleBasedRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskRoleBasedRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskRoleBasedRule()
    
    @property
    def default_rule(self,) -> Optional[str]:
        """
        Gets the defaultRule property value. The defaultRule property
        Returns: Optional[str]
        """
        return self._default_rule
    
    @default_rule.setter
    def default_rule(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultRule property value. The defaultRule property
        Args:
            value: Value to set for the defaultRule property.
        """
        self._default_rule = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_rule": lambda n : setattr(self, 'default_rule', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "property_rule": lambda n : setattr(self, 'property_rule', n.get_object_value(planner_task_property_rule.PlannerTaskPropertyRule)),
            "role": lambda n : setattr(self, 'role', n.get_object_value(planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase)),
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
    
    @property
    def property_rule(self,) -> Optional[planner_task_property_rule.PlannerTaskPropertyRule]:
        """
        Gets the propertyRule property value. The propertyRule property
        Returns: Optional[planner_task_property_rule.PlannerTaskPropertyRule]
        """
        return self._property_rule
    
    @property_rule.setter
    def property_rule(self,value: Optional[planner_task_property_rule.PlannerTaskPropertyRule] = None) -> None:
        """
        Sets the propertyRule property value. The propertyRule property
        Args:
            value: Value to set for the propertyRule property.
        """
        self._property_rule = value
    
    @property
    def role(self,) -> Optional[planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase]:
        """
        Gets the role property value. The role property
        Returns: Optional[planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[planner_task_configuration_role_base.PlannerTaskConfigurationRoleBase] = None) -> None:
        """
        Sets the role property value. The role property
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultRule", self.default_rule)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("propertyRule", self.property_rule)
        writer.write_object_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

