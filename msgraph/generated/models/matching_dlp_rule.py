from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dlp_action_info = lazy_import('msgraph.generated.models.dlp_action_info')
rule_mode = lazy_import('msgraph.generated.models.rule_mode')

class MatchingDlpRule(AdditionalDataHolder, Parsable):
    @property
    def actions(self,) -> Optional[List[dlp_action_info.DlpActionInfo]]:
        """
        Gets the actions property value. The actions property
        Returns: Optional[List[dlp_action_info.DlpActionInfo]]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[List[dlp_action_info.DlpActionInfo]] = None) -> None:
        """
        Sets the actions property value. The actions property
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
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
        Instantiates a new matchingDlpRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actions property
        self._actions: Optional[List[dlp_action_info.DlpActionInfo]] = None
        # The isMostRestrictive property
        self._is_most_restrictive: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policyId property
        self._policy_id: Optional[str] = None
        # The policyName property
        self._policy_name: Optional[str] = None
        # The priority property
        self._priority: Optional[int] = None
        # The ruleId property
        self._rule_id: Optional[str] = None
        # The ruleMode property
        self._rule_mode: Optional[rule_mode.RuleMode] = None
        # The ruleName property
        self._rule_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MatchingDlpRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MatchingDlpRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MatchingDlpRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(dlp_action_info.DlpActionInfo)),
            "is_most_restrictive": lambda n : setattr(self, 'is_most_restrictive', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policy_name": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "rule_id": lambda n : setattr(self, 'rule_id', n.get_str_value()),
            "rule_mode": lambda n : setattr(self, 'rule_mode', n.get_enum_value(rule_mode.RuleMode)),
            "rule_name": lambda n : setattr(self, 'rule_name', n.get_str_value()),
        }
        return fields
    
    @property
    def is_most_restrictive(self,) -> Optional[bool]:
        """
        Gets the isMostRestrictive property value. The isMostRestrictive property
        Returns: Optional[bool]
        """
        return self._is_most_restrictive
    
    @is_most_restrictive.setter
    def is_most_restrictive(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMostRestrictive property value. The isMostRestrictive property
        Args:
            value: Value to set for the isMostRestrictive property.
        """
        self._is_most_restrictive = value
    
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
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The policyId property
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The policyId property
        Args:
            value: Value to set for the policyId property.
        """
        self._policy_id = value
    
    @property
    def policy_name(self,) -> Optional[str]:
        """
        Gets the policyName property value. The policyName property
        Returns: Optional[str]
        """
        return self._policy_name
    
    @policy_name.setter
    def policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyName property value. The policyName property
        Args:
            value: Value to set for the policyName property.
        """
        self._policy_name = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def rule_id(self,) -> Optional[str]:
        """
        Gets the ruleId property value. The ruleId property
        Returns: Optional[str]
        """
        return self._rule_id
    
    @rule_id.setter
    def rule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleId property value. The ruleId property
        Args:
            value: Value to set for the ruleId property.
        """
        self._rule_id = value
    
    @property
    def rule_mode(self,) -> Optional[rule_mode.RuleMode]:
        """
        Gets the ruleMode property value. The ruleMode property
        Returns: Optional[rule_mode.RuleMode]
        """
        return self._rule_mode
    
    @rule_mode.setter
    def rule_mode(self,value: Optional[rule_mode.RuleMode] = None) -> None:
        """
        Sets the ruleMode property value. The ruleMode property
        Args:
            value: Value to set for the ruleMode property.
        """
        self._rule_mode = value
    
    @property
    def rule_name(self,) -> Optional[str]:
        """
        Gets the ruleName property value. The ruleName property
        Returns: Optional[str]
        """
        return self._rule_name
    
    @rule_name.setter
    def rule_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleName property value. The ruleName property
        Args:
            value: Value to set for the ruleName property.
        """
        self._rule_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_bool_value("isMostRestrictive", self.is_most_restrictive)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("ruleId", self.rule_id)
        writer.write_enum_value("ruleMode", self.rule_mode)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_additional_data_value(self.additional_data)
    

