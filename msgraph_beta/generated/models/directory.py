from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .administrative_unit import AdministrativeUnit
    from .attribute_set import AttributeSet
    from .certificate_authority_path import CertificateAuthorityPath
    from .company_subscription import CompanySubscription
    from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
    from .device_local_credential_info import DeviceLocalCredentialInfo
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .external_user_profile import ExternalUserProfile
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .identity_provider_base import IdentityProviderBase
    from .impacted_resource import ImpactedResource
    from .inbound_shared_user_profile import InboundSharedUserProfile
    from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
    from .outbound_shared_user_profile import OutboundSharedUserProfile
    from .pending_external_user_profile import PendingExternalUserProfile
    from .recommendation import Recommendation
    from .shared_email_domain import SharedEmailDomain

from .entity import Entity

@dataclass
class Directory(Entity):
    # Conceptual container for user and group directory objects.
    administrative_units: Optional[List[AdministrativeUnit]] = None
    # Group of related custom security attribute definitions.
    attribute_sets: Optional[List[AttributeSet]] = None
    # The certificateAuthorities property
    certificate_authorities: Optional[CertificateAuthorityPath] = None
    # Schema of a custom security attributes (key-value pairs).
    custom_security_attribute_definitions: Optional[List[CustomSecurityAttributeDefinition]] = None
    # Recently deleted items. Read-only. Nullable.
    deleted_items: Optional[List[DirectoryObject]] = None
    # The credentials of the device's local administrator account backed up to Microsoft Entra ID.
    device_local_credentials: Optional[List[DeviceLocalCredentialInfo]] = None
    # Collection of external user profiles that represent collaborators in the directory.
    external_user_profiles: Optional[List[ExternalUserProfile]] = None
    # The featureRolloutPolicies property
    feature_rollout_policies: Optional[List[FeatureRolloutPolicy]] = None
    # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
    federation_configurations: Optional[List[IdentityProviderBase]] = None
    # The impactedResources property
    impacted_resources: Optional[List[ImpactedResource]] = None
    # A collection of external users whose profile data is shared with the Microsoft Entra tenant. Nullable.
    inbound_shared_user_profiles: Optional[List[InboundSharedUserProfile]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A container for on-premises directory synchronization functionalities that are available for the organization.
    on_premises_synchronization: Optional[List[OnPremisesDirectorySynchronization]] = None
    # The outboundSharedUserProfiles property
    outbound_shared_user_profiles: Optional[List[OutboundSharedUserProfile]] = None
    # Collection of pending external user profiles representing collaborators in the directory that are unredeemed.
    pending_external_user_profiles: Optional[List[PendingExternalUserProfile]] = None
    # List of recommended improvements to improve tenant posture.
    recommendations: Optional[List[Recommendation]] = None
    # The sharedEmailDomains property
    shared_email_domains: Optional[List[SharedEmailDomain]] = None
    # List of commercial subscriptions that an organization has.
    subscriptions: Optional[List[CompanySubscription]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Directory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .administrative_unit import AdministrativeUnit
        from .attribute_set import AttributeSet
        from .certificate_authority_path import CertificateAuthorityPath
        from .company_subscription import CompanySubscription
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .external_user_profile import ExternalUserProfile
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .identity_provider_base import IdentityProviderBase
        from .impacted_resource import ImpactedResource
        from .inbound_shared_user_profile import InboundSharedUserProfile
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .outbound_shared_user_profile import OutboundSharedUserProfile
        from .pending_external_user_profile import PendingExternalUserProfile
        from .recommendation import Recommendation
        from .shared_email_domain import SharedEmailDomain

        from .administrative_unit import AdministrativeUnit
        from .attribute_set import AttributeSet
        from .certificate_authority_path import CertificateAuthorityPath
        from .company_subscription import CompanySubscription
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .external_user_profile import ExternalUserProfile
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .identity_provider_base import IdentityProviderBase
        from .impacted_resource import ImpactedResource
        from .inbound_shared_user_profile import InboundSharedUserProfile
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .outbound_shared_user_profile import OutboundSharedUserProfile
        from .pending_external_user_profile import PendingExternalUserProfile
        from .recommendation import Recommendation
        from .shared_email_domain import SharedEmailDomain

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(AdministrativeUnit)),
            "attributeSets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(AttributeSet)),
            "certificateAuthorities": lambda n : setattr(self, 'certificate_authorities', n.get_object_value(CertificateAuthorityPath)),
            "customSecurityAttributeDefinitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(CustomSecurityAttributeDefinition)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(DirectoryObject)),
            "deviceLocalCredentials": lambda n : setattr(self, 'device_local_credentials', n.get_collection_of_object_values(DeviceLocalCredentialInfo)),
            "externalUserProfiles": lambda n : setattr(self, 'external_user_profiles', n.get_collection_of_object_values(ExternalUserProfile)),
            "featureRolloutPolicies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(FeatureRolloutPolicy)),
            "federationConfigurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(IdentityProviderBase)),
            "impactedResources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(ImpactedResource)),
            "inboundSharedUserProfiles": lambda n : setattr(self, 'inbound_shared_user_profiles', n.get_collection_of_object_values(InboundSharedUserProfile)),
            "onPremisesSynchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(OnPremisesDirectorySynchronization)),
            "outboundSharedUserProfiles": lambda n : setattr(self, 'outbound_shared_user_profiles', n.get_collection_of_object_values(OutboundSharedUserProfile)),
            "pendingExternalUserProfiles": lambda n : setattr(self, 'pending_external_user_profiles', n.get_collection_of_object_values(PendingExternalUserProfile)),
            "recommendations": lambda n : setattr(self, 'recommendations', n.get_collection_of_object_values(Recommendation)),
            "sharedEmailDomains": lambda n : setattr(self, 'shared_email_domains', n.get_collection_of_object_values(SharedEmailDomain)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(CompanySubscription)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
        writer.write_object_value("certificateAuthorities", self.certificate_authorities)
        writer.write_collection_of_object_values("customSecurityAttributeDefinitions", self.custom_security_attribute_definitions)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("deviceLocalCredentials", self.device_local_credentials)
        writer.write_collection_of_object_values("externalUserProfiles", self.external_user_profiles)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_collection_of_object_values("inboundSharedUserProfiles", self.inbound_shared_user_profiles)
        writer.write_collection_of_object_values("onPremisesSynchronization", self.on_premises_synchronization)
        writer.write_collection_of_object_values("outboundSharedUserProfiles", self.outbound_shared_user_profiles)
        writer.write_collection_of_object_values("pendingExternalUserProfiles", self.pending_external_user_profiles)
        writer.write_collection_of_object_values("recommendations", self.recommendations)
        writer.write_collection_of_object_values("sharedEmailDomains", self.shared_email_domains)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
    

