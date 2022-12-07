from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class GovernanceRuleSetting(AdditionalDataHolder, Parsable):
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
        Instantiates a new governanceRuleSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The id of the rule. For example, ExpirationRule and MfaRule.
        self._rule_identifier: Optional[str] = None
        # The settings of the rule. The value is a JSON string with a list of pairs in the format of Parameter_Name:Parameter_Value. For example, {'permanentAssignment':false,'maximumGrantPeriodInMinutes':129600}
        self._setting: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRuleSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRuleSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceRuleSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rule_identifier": lambda n : setattr(self, 'rule_identifier', n.get_str_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
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
    def rule_identifier(self,) -> Optional[str]:
        """
        Gets the ruleIdentifier property value. The id of the rule. For example, ExpirationRule and MfaRule.
        Returns: Optional[str]
        """
        return self._rule_identifier
    
    @rule_identifier.setter
    def rule_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleIdentifier property value. The id of the rule. For example, ExpirationRule and MfaRule.
        Args:
            value: Value to set for the ruleIdentifier property.
        """
        self._rule_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("ruleIdentifier", self.rule_identifier)
        writer.write_str_value("setting", self.setting)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting(self,) -> Optional[str]:
        """
        Gets the setting property value. The settings of the rule. The value is a JSON string with a list of pairs in the format of Parameter_Name:Parameter_Value. For example, {'permanentAssignment':false,'maximumGrantPeriodInMinutes':129600}
        Returns: Optional[str]
        """
        return self._setting
    
    @setting.setter
    def setting(self,value: Optional[str] = None) -> None:
        """
        Sets the setting property value. The settings of the rule. The value is a JSON string with a list of pairs in the format of Parameter_Name:Parameter_Value. For example, {'permanentAssignment':false,'maximumGrantPeriodInMinutes':129600}
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value
    

