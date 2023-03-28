from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_rule_override

class PlannerFieldRules(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerFieldRules and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default rules that apply if no override matches to the current data.
        self._default_rules: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Overrides that specify different rules for specific data associated with the field.
        self._overrides: Optional[List[planner_rule_override.PlannerRuleOverride]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerFieldRules:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerFieldRules
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerFieldRules()
    
    @property
    def default_rules(self,) -> Optional[List[str]]:
        """
        Gets the defaultRules property value. The default rules that apply if no override matches to the current data.
        Returns: Optional[List[str]]
        """
        return self._default_rules
    
    @default_rules.setter
    def default_rules(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defaultRules property value. The default rules that apply if no override matches to the current data.
        Args:
            value: Value to set for the default_rules property.
        """
        self._default_rules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_rule_override

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultRules": lambda n : setattr(self, 'default_rules', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overrides": lambda n : setattr(self, 'overrides', n.get_collection_of_object_values(planner_rule_override.PlannerRuleOverride)),
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
    
    @property
    def overrides(self,) -> Optional[List[planner_rule_override.PlannerRuleOverride]]:
        """
        Gets the overrides property value. Overrides that specify different rules for specific data associated with the field.
        Returns: Optional[List[planner_rule_override.PlannerRuleOverride]]
        """
        return self._overrides
    
    @overrides.setter
    def overrides(self,value: Optional[List[planner_rule_override.PlannerRuleOverride]] = None) -> None:
        """
        Sets the overrides property value. Overrides that specify different rules for specific data associated with the field.
        Args:
            value: Value to set for the overrides property.
        """
        self._overrides = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("defaultRules", self.default_rules)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("overrides", self.overrides)
        writer.write_additional_data_value(self.additional_data)
    

