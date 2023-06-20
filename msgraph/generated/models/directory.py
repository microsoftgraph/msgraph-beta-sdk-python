from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import administrative_unit, attribute_set, certificate_authority_path, company_subscription, custom_security_attribute_definition, directory_object, entity, feature_rollout_policy, identity_provider_base, impacted_resource, inbound_shared_user_profile, on_premises_directory_synchronization, outbound_shared_user_profile, recommendation, shared_email_domain

from . import entity

@dataclass
class Directory(entity.Entity):
    # Conceptual container for user and group directory objects.
    administrative_units: Optional[List[administrative_unit.AdministrativeUnit]] = None
    # Group of related custom security attribute definitions.
    attribute_sets: Optional[List[attribute_set.AttributeSet]] = None
    # The certificateAuthorities property
    certificate_authorities: Optional[certificate_authority_path.CertificateAuthorityPath] = None
    # Schema of a custom security attributes (key-value pairs).
    custom_security_attribute_definitions: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None
    # The deletedItems property
    deleted_items: Optional[List[directory_object.DirectoryObject]] = None
    # The featureRolloutPolicies property
    feature_rollout_policies: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None
    # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
    federation_configurations: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    # The impactedResources property
    impacted_resources: Optional[List[impacted_resource.ImpactedResource]] = None
    # A collection of external Azure AD users whose profile data has been shared with the Azure AD tenant. Nullable.
    inbound_shared_user_profiles: Optional[List[inbound_shared_user_profile.InboundSharedUserProfile]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A container for on-premises directory synchronization functionalities that are available for the organization.
    on_premises_synchronization: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None
    # The outboundSharedUserProfiles property
    outbound_shared_user_profiles: Optional[List[outbound_shared_user_profile.OutboundSharedUserProfile]] = None
    # List of recommended improvements to improve tenant posture.
    recommendations: Optional[List[recommendation.Recommendation]] = None
    # The sharedEmailDomains property
    shared_email_domains: Optional[List[shared_email_domain.SharedEmailDomain]] = None
    # The subscriptions property
    subscriptions: Optional[List[company_subscription.CompanySubscription]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Directory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import administrative_unit, attribute_set, certificate_authority_path, company_subscription, custom_security_attribute_definition, directory_object, entity, feature_rollout_policy, identity_provider_base, impacted_resource, inbound_shared_user_profile, on_premises_directory_synchronization, outbound_shared_user_profile, recommendation, shared_email_domain

        from . import administrative_unit, attribute_set, certificate_authority_path, company_subscription, custom_security_attribute_definition, directory_object, entity, feature_rollout_policy, identity_provider_base, impacted_resource, inbound_shared_user_profile, on_premises_directory_synchronization, outbound_shared_user_profile, recommendation, shared_email_domain

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(administrative_unit.AdministrativeUnit)),
            "attributeSets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(attribute_set.AttributeSet)),
            "certificateAuthorities": lambda n : setattr(self, 'certificate_authorities', n.get_object_value(certificate_authority_path.CertificateAuthorityPath)),
            "customSecurityAttributeDefinitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(custom_security_attribute_definition.CustomSecurityAttributeDefinition)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "featureRolloutPolicies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(feature_rollout_policy.FeatureRolloutPolicy)),
            "federationConfigurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "impactedResources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(impacted_resource.ImpactedResource)),
            "inboundSharedUserProfiles": lambda n : setattr(self, 'inbound_shared_user_profiles', n.get_collection_of_object_values(inbound_shared_user_profile.InboundSharedUserProfile)),
            "onPremisesSynchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(on_premises_directory_synchronization.OnPremisesDirectorySynchronization)),
            "outboundSharedUserProfiles": lambda n : setattr(self, 'outbound_shared_user_profiles', n.get_collection_of_object_values(outbound_shared_user_profile.OutboundSharedUserProfile)),
            "recommendations": lambda n : setattr(self, 'recommendations', n.get_collection_of_object_values(recommendation.Recommendation)),
            "sharedEmailDomains": lambda n : setattr(self, 'shared_email_domains', n.get_collection_of_object_values(shared_email_domain.SharedEmailDomain)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(company_subscription.CompanySubscription)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
        writer.write_object_value("certificateAuthorities", self.certificate_authorities)
        writer.write_collection_of_object_values("customSecurityAttributeDefinitions", self.custom_security_attribute_definitions)
        writer.write_collection_of_object_values("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("federationConfigurations", self.federation_configurations)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_collection_of_object_values("inboundSharedUserProfiles", self.inbound_shared_user_profiles)
        writer.write_collection_of_object_values("onPremisesSynchronization", self.on_premises_synchronization)
        writer.write_collection_of_object_values("outboundSharedUserProfiles", self.outbound_shared_user_profiles)
        writer.write_collection_of_object_values("recommendations", self.recommendations)
        writer.write_collection_of_object_values("sharedEmailDomains", self.shared_email_domains)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
    

