from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_target_configuration, cross_tenant_access_policy_tenant_restrictions

class CrossTenantAccessPolicyB2BSetting(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyB2BSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of applications targeted with your cross-tenant access policy.
        self._applications: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of users and groups targeted with your cross-tenant access policy.
        self._users_and_groups: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None
    
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
    def applications(self,) -> Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration]:
        """
        Gets the applications property value. The list of applications targeted with your cross-tenant access policy.
        Returns: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration]
        """
        return self._applications
    
    @applications.setter
    def applications(self,value: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None) -> None:
        """
        Sets the applications property value. The list of applications targeted with your cross-tenant access policy.
        Args:
            value: Value to set for the applications property.
        """
        self._applications = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyB2BSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyB2BSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicyTenantRestrictions":
                from . import cross_tenant_access_policy_tenant_restrictions

                return cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions()
        return CrossTenantAccessPolicyB2BSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy_target_configuration, cross_tenant_access_policy_tenant_restrictions

        fields: Dict[str, Callable[[Any], None]] = {
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usersAndGroups": lambda n : setattr(self, 'users_and_groups', n.get_object_value(cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration)),
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
        writer.write_object_value("applications", self.applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("usersAndGroups", self.users_and_groups)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def users_and_groups(self,) -> Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration]:
        """
        Gets the usersAndGroups property value. The list of users and groups targeted with your cross-tenant access policy.
        Returns: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration]
        """
        return self._users_and_groups
    
    @users_and_groups.setter
    def users_and_groups(self,value: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None) -> None:
        """
        Sets the usersAndGroups property value. The list of users and groups targeted with your cross-tenant access policy.
        Args:
            value: Value to set for the users_and_groups property.
        """
        self._users_and_groups = value
    

