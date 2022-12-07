from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

requirement_provider = lazy_import('msgraph.generated.models.requirement_provider')

class AuthenticationRequirementPolicy(AdditionalDataHolder, Parsable):
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
        Instantiates a new authenticationRequirementPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Provides additional detail on the feature identified in requirementProvider.
        self._detail: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Identifies what Azure AD feature requires MFA in this policy. Possible values are: user, request, servicePrincipal, v1ConditionalAccess, multiConditionalAccess, tenantSessionRiskPolicy, accountCompromisePolicies, v1ConditionalAccessDependency, v1ConditionalAccessPolicyIdRequested, mfaRegistrationRequiredByIdentityProtectionPolicy, baselineProtection, mfaRegistrationRequiredByBaselineProtection, mfaRegistrationRequiredByMultiConditionalAccess, enforcedForCspAdmins, securityDefaults, mfaRegistrationRequiredBySecurityDefaults, proofUpCodeRequest, crossTenantOutboundRule, gpsLocationCondition, riskBasedPolicy, unknownFutureValue.
        self._requirement_provider: Optional[requirement_provider.RequirementProvider] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationRequirementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationRequirementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationRequirementPolicy()
    
    @property
    def detail(self,) -> Optional[str]:
        """
        Gets the detail property value. Provides additional detail on the feature identified in requirementProvider.
        Returns: Optional[str]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[str] = None) -> None:
        """
        Sets the detail property value. Provides additional detail on the feature identified in requirementProvider.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requirement_provider": lambda n : setattr(self, 'requirement_provider', n.get_enum_value(requirement_provider.RequirementProvider)),
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
    def requirement_provider(self,) -> Optional[requirement_provider.RequirementProvider]:
        """
        Gets the requirementProvider property value. Identifies what Azure AD feature requires MFA in this policy. Possible values are: user, request, servicePrincipal, v1ConditionalAccess, multiConditionalAccess, tenantSessionRiskPolicy, accountCompromisePolicies, v1ConditionalAccessDependency, v1ConditionalAccessPolicyIdRequested, mfaRegistrationRequiredByIdentityProtectionPolicy, baselineProtection, mfaRegistrationRequiredByBaselineProtection, mfaRegistrationRequiredByMultiConditionalAccess, enforcedForCspAdmins, securityDefaults, mfaRegistrationRequiredBySecurityDefaults, proofUpCodeRequest, crossTenantOutboundRule, gpsLocationCondition, riskBasedPolicy, unknownFutureValue.
        Returns: Optional[requirement_provider.RequirementProvider]
        """
        return self._requirement_provider
    
    @requirement_provider.setter
    def requirement_provider(self,value: Optional[requirement_provider.RequirementProvider] = None) -> None:
        """
        Sets the requirementProvider property value. Identifies what Azure AD feature requires MFA in this policy. Possible values are: user, request, servicePrincipal, v1ConditionalAccess, multiConditionalAccess, tenantSessionRiskPolicy, accountCompromisePolicies, v1ConditionalAccessDependency, v1ConditionalAccessPolicyIdRequested, mfaRegistrationRequiredByIdentityProtectionPolicy, baselineProtection, mfaRegistrationRequiredByBaselineProtection, mfaRegistrationRequiredByMultiConditionalAccess, enforcedForCspAdmins, securityDefaults, mfaRegistrationRequiredBySecurityDefaults, proofUpCodeRequest, crossTenantOutboundRule, gpsLocationCondition, riskBasedPolicy, unknownFutureValue.
        Args:
            value: Value to set for the requirementProvider property.
        """
        self._requirement_provider = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("requirementProvider", self.requirement_provider)
        writer.write_additional_data_value(self.additional_data)
    

