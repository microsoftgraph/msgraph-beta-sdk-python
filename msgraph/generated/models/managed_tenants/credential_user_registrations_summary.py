from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CredentialUserRegistrationsSummary(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new credentialUserRegistrationsSummary and sets the default values.
        """
        super().__init__()
        # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The number of users that are capable of performing multi-factor authentication or self service password reset. Optional. Read-only.
        self._mfa_and_sspr_capable_user_count: Optional[int] = None
        # The state of a conditional access policy that enforces multi-factor authentication. Optional. Read-only.
        self._mfa_conditional_access_policy_state: Optional[str] = None
        # The number of users in the multi-factor authentication exclusion security group (Microsoft 365 Lighthouse - MFA exclusions). Optional. Read-only.
        self._mfa_excluded_user_count: Optional[int] = None
        # The number of users registered for multi-factor authentication. Optional. Read-only.
        self._mfa_registered_user_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A flag indicating whether Identity Security Defaults is enabled. Optional. Read-only.
        self._security_defaults_enabled: Optional[bool] = None
        # The number of users enabled for self service password reset. Optional. Read-only.
        self._sspr_enabled_user_count: Optional[int] = None
        # The number of users registered for self service password reset. Optional. Read-only.
        self._sspr_registered_user_count: Optional[int] = None
        # The display name for the managed tenant. Required. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        self._tenant_id: Optional[str] = None
        # The total number of users in the given managed tenant. Optional. Read-only.
        self._total_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUserRegistrationsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationsSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialUserRegistrationsSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "mfa_and_sspr_capable_user_count": lambda n : setattr(self, 'mfa_and_sspr_capable_user_count', n.get_int_value()),
            "mfa_conditional_access_policy_state": lambda n : setattr(self, 'mfa_conditional_access_policy_state', n.get_str_value()),
            "mfa_excluded_user_count": lambda n : setattr(self, 'mfa_excluded_user_count', n.get_int_value()),
            "mfa_registered_user_count": lambda n : setattr(self, 'mfa_registered_user_count', n.get_int_value()),
            "security_defaults_enabled": lambda n : setattr(self, 'security_defaults_enabled', n.get_bool_value()),
            "sspr_enabled_user_count": lambda n : setattr(self, 'sspr_enabled_user_count', n.get_int_value()),
            "sspr_registered_user_count": lambda n : setattr(self, 'sspr_registered_user_count', n.get_int_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "total_user_count": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
    @property
    def mfa_and_sspr_capable_user_count(self,) -> Optional[int]:
        """
        Gets the mfaAndSsprCapableUserCount property value. The number of users that are capable of performing multi-factor authentication or self service password reset. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._mfa_and_sspr_capable_user_count
    
    @mfa_and_sspr_capable_user_count.setter
    def mfa_and_sspr_capable_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mfaAndSsprCapableUserCount property value. The number of users that are capable of performing multi-factor authentication or self service password reset. Optional. Read-only.
        Args:
            value: Value to set for the mfaAndSsprCapableUserCount property.
        """
        self._mfa_and_sspr_capable_user_count = value
    
    @property
    def mfa_conditional_access_policy_state(self,) -> Optional[str]:
        """
        Gets the mfaConditionalAccessPolicyState property value. The state of a conditional access policy that enforces multi-factor authentication. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._mfa_conditional_access_policy_state
    
    @mfa_conditional_access_policy_state.setter
    def mfa_conditional_access_policy_state(self,value: Optional[str] = None) -> None:
        """
        Sets the mfaConditionalAccessPolicyState property value. The state of a conditional access policy that enforces multi-factor authentication. Optional. Read-only.
        Args:
            value: Value to set for the mfaConditionalAccessPolicyState property.
        """
        self._mfa_conditional_access_policy_state = value
    
    @property
    def mfa_excluded_user_count(self,) -> Optional[int]:
        """
        Gets the mfaExcludedUserCount property value. The number of users in the multi-factor authentication exclusion security group (Microsoft 365 Lighthouse - MFA exclusions). Optional. Read-only.
        Returns: Optional[int]
        """
        return self._mfa_excluded_user_count
    
    @mfa_excluded_user_count.setter
    def mfa_excluded_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mfaExcludedUserCount property value. The number of users in the multi-factor authentication exclusion security group (Microsoft 365 Lighthouse - MFA exclusions). Optional. Read-only.
        Args:
            value: Value to set for the mfaExcludedUserCount property.
        """
        self._mfa_excluded_user_count = value
    
    @property
    def mfa_registered_user_count(self,) -> Optional[int]:
        """
        Gets the mfaRegisteredUserCount property value. The number of users registered for multi-factor authentication. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._mfa_registered_user_count
    
    @mfa_registered_user_count.setter
    def mfa_registered_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mfaRegisteredUserCount property value. The number of users registered for multi-factor authentication. Optional. Read-only.
        Args:
            value: Value to set for the mfaRegisteredUserCount property.
        """
        self._mfa_registered_user_count = value
    
    @property
    def security_defaults_enabled(self,) -> Optional[bool]:
        """
        Gets the securityDefaultsEnabled property value. A flag indicating whether Identity Security Defaults is enabled. Optional. Read-only.
        Returns: Optional[bool]
        """
        return self._security_defaults_enabled
    
    @security_defaults_enabled.setter
    def security_defaults_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityDefaultsEnabled property value. A flag indicating whether Identity Security Defaults is enabled. Optional. Read-only.
        Args:
            value: Value to set for the securityDefaultsEnabled property.
        """
        self._security_defaults_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("mfaAndSsprCapableUserCount", self.mfa_and_sspr_capable_user_count)
        writer.write_str_value("mfaConditionalAccessPolicyState", self.mfa_conditional_access_policy_state)
        writer.write_int_value("mfaExcludedUserCount", self.mfa_excluded_user_count)
        writer.write_int_value("mfaRegisteredUserCount", self.mfa_registered_user_count)
        writer.write_bool_value("securityDefaultsEnabled", self.security_defaults_enabled)
        writer.write_int_value("ssprEnabledUserCount", self.sspr_enabled_user_count)
        writer.write_int_value("ssprRegisteredUserCount", self.sspr_registered_user_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalUserCount", self.total_user_count)
    
    @property
    def sspr_enabled_user_count(self,) -> Optional[int]:
        """
        Gets the ssprEnabledUserCount property value. The number of users enabled for self service password reset. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._sspr_enabled_user_count
    
    @sspr_enabled_user_count.setter
    def sspr_enabled_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ssprEnabledUserCount property value. The number of users enabled for self service password reset. Optional. Read-only.
        Args:
            value: Value to set for the ssprEnabledUserCount property.
        """
        self._sspr_enabled_user_count = value
    
    @property
    def sspr_registered_user_count(self,) -> Optional[int]:
        """
        Gets the ssprRegisteredUserCount property value. The number of users registered for self service password reset. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._sspr_registered_user_count
    
    @sspr_registered_user_count.setter
    def sspr_registered_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ssprRegisteredUserCount property value. The number of users registered for self service password reset. Optional. Read-only.
        Args:
            value: Value to set for the ssprRegisteredUserCount property.
        """
        self._sspr_registered_user_count = value
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantDisplayName property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def total_user_count(self,) -> Optional[int]:
        """
        Gets the totalUserCount property value. The total number of users in the given managed tenant. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._total_user_count
    
    @total_user_count.setter
    def total_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUserCount property value. The total number of users in the given managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the totalUserCount property.
        """
        self._total_user_count = value
    

