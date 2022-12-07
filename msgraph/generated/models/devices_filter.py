from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_target_configuration_access_type = lazy_import('msgraph.generated.models.cross_tenant_access_policy_target_configuration_access_type')

class DevicesFilter(AdditionalDataHolder, Parsable):
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
        Instantiates a new devicesFilter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The mode property
        self._mode: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The rule property
        self._rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DevicesFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DevicesFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DevicesFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
        }
        return fields
    
    @property
    def mode(self,) -> Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType]:
        """
        Gets the mode property value. The mode property
        Returns: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType]
        """
        return self._mode
    
    @mode.setter
    def mode(self,value: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType] = None) -> None:
        """
        Sets the mode property value. The mode property
        Args:
            value: Value to set for the mode property.
        """
        self._mode = value
    
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
    def rule(self,) -> Optional[str]:
        """
        Gets the rule property value. The rule property
        Returns: Optional[str]
        """
        return self._rule
    
    @rule.setter
    def rule(self,value: Optional[str] = None) -> None:
        """
        Sets the rule property value. The rule property
        Args:
            value: Value to set for the rule property.
        """
        self._rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("mode", self.mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("rule", self.rule)
        writer.write_additional_data_value(self.additional_data)
    

