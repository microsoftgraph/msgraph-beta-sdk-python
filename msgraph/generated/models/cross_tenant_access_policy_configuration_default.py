from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_b2_b_setting, cross_tenant_access_policy_inbound_trust, cross_tenant_access_policy_tenant_restrictions, entity, inbound_outbound_policy_configuration

from . import entity

class CrossTenantAccessPolicyConfigurationDefault(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyConfigurationDefault and sets the default values.
        """
        super().__init__()
        # Determines the default configuration for automatic user consent settings. inboundAllowed and outboundAllowed will always be false and cannot be updated in the default configuration. Read only.
        self._automatic_user_consent_settings: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration] = None
        # Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        self._b2b_collaboration_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        self._b2b_collaboration_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        self._b2b_direct_connect_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        self._b2b_direct_connect_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        self._inbound_trust: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None
        # If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        self._is_service_default: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The tenantRestrictions property
        self._tenant_restrictions: Optional[cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions] = None
    
    @property
    def automatic_user_consent_settings(self,) -> Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration]:
        """
        Gets the automaticUserConsentSettings property value. Determines the default configuration for automatic user consent settings. inboundAllowed and outboundAllowed will always be false and cannot be updated in the default configuration. Read only.
        Returns: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration]
        """
        return self._automatic_user_consent_settings
    
    @automatic_user_consent_settings.setter
    def automatic_user_consent_settings(self,value: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration] = None) -> None:
        """
        Sets the automaticUserConsentSettings property value. Determines the default configuration for automatic user consent settings. inboundAllowed and outboundAllowed will always be false and cannot be updated in the default configuration. Read only.
        Args:
            value: Value to set for the automatic_user_consent_settings property.
        """
        self._automatic_user_consent_settings = value
    
    @property
    def b2b_collaboration_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_inbound
    
    @b2b_collaboration_inbound.setter
    def b2b_collaboration_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2b_collaboration_inbound property.
        """
        self._b2b_collaboration_inbound = value
    
    @property
    def b2b_collaboration_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_outbound
    
    @b2b_collaboration_outbound.setter
    def b2b_collaboration_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2b_collaboration_outbound property.
        """
        self._b2b_collaboration_outbound = value
    
    @property
    def b2b_direct_connect_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_inbound
    
    @b2b_direct_connect_inbound.setter
    def b2b_direct_connect_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        Args:
            value: Value to set for the b2b_direct_connect_inbound property.
        """
        self._b2b_direct_connect_inbound = value
    
    @property
    def b2b_direct_connect_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_outbound
    
    @b2b_direct_connect_outbound.setter
    def b2b_direct_connect_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Args:
            value: Value to set for the b2b_direct_connect_outbound property.
        """
        self._b2b_direct_connect_outbound = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyConfigurationDefault:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationDefault
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyConfigurationDefault()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy_b2_b_setting, cross_tenant_access_policy_inbound_trust, cross_tenant_access_policy_tenant_restrictions, entity, inbound_outbound_policy_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticUserConsentSettings": lambda n : setattr(self, 'automatic_user_consent_settings', n.get_object_value(inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration)),
            "b2bCollaborationInbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bCollaborationOutbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectInbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectOutbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "inboundTrust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust)),
            "isServiceDefault": lambda n : setattr(self, 'is_service_default', n.get_bool_value()),
            "tenantRestrictions": lambda n : setattr(self, 'tenant_restrictions', n.get_object_value(cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inbound_trust(self,) -> Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]:
        """
        Gets the inboundTrust property value. Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Returns: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]
        """
        return self._inbound_trust
    
    @inbound_trust.setter
    def inbound_trust(self,value: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None) -> None:
        """
        Sets the inboundTrust property value. Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Args:
            value: Value to set for the inbound_trust property.
        """
        self._inbound_trust = value
    
    @property
    def is_service_default(self,) -> Optional[bool]:
        """
        Gets the isServiceDefault property value. If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        Returns: Optional[bool]
        """
        return self._is_service_default
    
    @is_service_default.setter
    def is_service_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isServiceDefault property value. If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        Args:
            value: Value to set for the is_service_default property.
        """
        self._is_service_default = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("automaticUserConsentSettings", self.automatic_user_consent_settings)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_bool_value("isServiceDefault", self.is_service_default)
        writer.write_object_value("tenantRestrictions", self.tenant_restrictions)
    
    @property
    def tenant_restrictions(self,) -> Optional[cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions]:
        """
        Gets the tenantRestrictions property value. The tenantRestrictions property
        Returns: Optional[cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions]
        """
        return self._tenant_restrictions
    
    @tenant_restrictions.setter
    def tenant_restrictions(self,value: Optional[cross_tenant_access_policy_tenant_restrictions.CrossTenantAccessPolicyTenantRestrictions] = None) -> None:
        """
        Sets the tenantRestrictions property value. The tenantRestrictions property
        Args:
            value: Value to set for the tenant_restrictions property.
        """
        self._tenant_restrictions = value
    

