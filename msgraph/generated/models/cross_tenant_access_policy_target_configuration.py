from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_target, cross_tenant_access_policy_target_configuration_access_type

class CrossTenantAccessPolicyTargetConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyTargetConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines whether access is allowed or blocked. The possible values are: allowed, blocked, unknownFutureValue.
        self._access_type: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies whether to target users, groups, or applications with this rule.
        self._targets: Optional[List[cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget]] = None
    
    @property
    def access_type(self,) -> Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType]:
        """
        Gets the accessType property value. Defines whether access is allowed or blocked. The possible values are: allowed, blocked, unknownFutureValue.
        Returns: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType]
        """
        return self._access_type
    
    @access_type.setter
    def access_type(self,value: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType] = None) -> None:
        """
        Sets the accessType property value. Defines whether access is allowed or blocked. The possible values are: allowed, blocked, unknownFutureValue.
        Args:
            value: Value to set for the access_type property.
        """
        self._access_type = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyTargetConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTargetConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyTargetConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy_target, cross_tenant_access_policy_target_configuration_access_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def targets(self,) -> Optional[List[cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget]]:
        """
        Gets the targets property value. Specifies whether to target users, groups, or applications with this rule.
        Returns: Optional[List[cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget]] = None) -> None:
        """
        Sets the targets property value. Specifies whether to target users, groups, or applications with this rule.
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    

