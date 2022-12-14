from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

administrative_unit = lazy_import('msgraph.generated.models.administrative_unit')
attribute_set = lazy_import('msgraph.generated.models.attribute_set')
custom_security_attribute_definition = lazy_import('msgraph.generated.models.custom_security_attribute_definition')
directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
feature_rollout_policy = lazy_import('msgraph.generated.models.feature_rollout_policy')
identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')
inbound_shared_user_profile = lazy_import('msgraph.generated.models.inbound_shared_user_profile')
on_premises_directory_synchronization = lazy_import('msgraph.generated.models.on_premises_directory_synchronization')
outbound_shared_user_profile = lazy_import('msgraph.generated.models.outbound_shared_user_profile')
recommendation = lazy_import('msgraph.generated.models.recommendation')
recommendation_resource = lazy_import('msgraph.generated.models.recommendation_resource')
shared_email_domain = lazy_import('msgraph.generated.models.shared_email_domain')

class Directory(entity.Entity):
    @property
    def administrative_units(self,) -> Optional[List[administrative_unit.AdministrativeUnit]]:
        """
        Gets the administrativeUnits property value. Conceptual container for user and group directory objects.
        Returns: Optional[List[administrative_unit.AdministrativeUnit]]
        """
        return self._administrative_units
    
    @administrative_units.setter
    def administrative_units(self,value: Optional[List[administrative_unit.AdministrativeUnit]] = None) -> None:
        """
        Sets the administrativeUnits property value. Conceptual container for user and group directory objects.
        Args:
            value: Value to set for the administrativeUnits property.
        """
        self._administrative_units = value
    
    @property
    def attribute_sets(self,) -> Optional[List[attribute_set.AttributeSet]]:
        """
        Gets the attributeSets property value. Group of related custom security attribute definitions.
        Returns: Optional[List[attribute_set.AttributeSet]]
        """
        return self._attribute_sets
    
    @attribute_sets.setter
    def attribute_sets(self,value: Optional[List[attribute_set.AttributeSet]] = None) -> None:
        """
        Sets the attributeSets property value. Group of related custom security attribute definitions.
        Args:
            value: Value to set for the attributeSets property.
        """
        self._attribute_sets = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Directory and sets the default values.
        """
        super().__init__()
        # Conceptual container for user and group directory objects.
        self._administrative_units: Optional[List[administrative_unit.AdministrativeUnit]] = None
        # Group of related custom security attribute definitions.
        self._attribute_sets: Optional[List[attribute_set.AttributeSet]] = None
        # Schema of a custom security attributes (key-value pairs).
        self._custom_security_attribute_definitions: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None
        # The deletedItems property
        self._deleted_items: Optional[List[directory_object.DirectoryObject]] = None
        # The featureRolloutPolicies property
        self._feature_rollout_policies: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None
        # Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        self._federation_configurations: Optional[List[identity_provider_base.IdentityProviderBase]] = None
        # The impactedResources property
        self._impacted_resources: Optional[List[recommendation_resource.RecommendationResource]] = None
        # The inboundSharedUserProfiles property
        self._inbound_shared_user_profiles: Optional[List[inbound_shared_user_profile.InboundSharedUserProfile]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A container for on-premises directory synchronization functionalities that are available for the organization.
        self._on_premises_synchronization: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None
        # The outboundSharedUserProfiles property
        self._outbound_shared_user_profiles: Optional[List[outbound_shared_user_profile.OutboundSharedUserProfile]] = None
        # The recommendations property
        self._recommendations: Optional[List[recommendation.Recommendation]] = None
        # The sharedEmailDomains property
        self._shared_email_domains: Optional[List[shared_email_domain.SharedEmailDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Directory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Directory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Directory()
    
    @property
    def custom_security_attribute_definitions(self,) -> Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]]:
        """
        Gets the customSecurityAttributeDefinitions property value. Schema of a custom security attributes (key-value pairs).
        Returns: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]]
        """
        return self._custom_security_attribute_definitions
    
    @custom_security_attribute_definitions.setter
    def custom_security_attribute_definitions(self,value: Optional[List[custom_security_attribute_definition.CustomSecurityAttributeDefinition]] = None) -> None:
        """
        Sets the customSecurityAttributeDefinitions property value. Schema of a custom security attributes (key-value pairs).
        Args:
            value: Value to set for the customSecurityAttributeDefinitions property.
        """
        self._custom_security_attribute_definitions = value
    
    @property
    def deleted_items(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the deletedItems property value. The deletedItems property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._deleted_items
    
    @deleted_items.setter
    def deleted_items(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the deletedItems property value. The deletedItems property
        Args:
            value: Value to set for the deletedItems property.
        """
        self._deleted_items = value
    
    @property
    def feature_rollout_policies(self,) -> Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]:
        """
        Gets the featureRolloutPolicies property value. The featureRolloutPolicies property
        Returns: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]
        """
        return self._feature_rollout_policies
    
    @feature_rollout_policies.setter
    def feature_rollout_policies(self,value: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None) -> None:
        """
        Sets the featureRolloutPolicies property value. The featureRolloutPolicies property
        Args:
            value: Value to set for the featureRolloutPolicies property.
        """
        self._feature_rollout_policies = value
    
    @property
    def federation_configurations(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the federationConfigurations property value. Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._federation_configurations
    
    @federation_configurations.setter
    def federation_configurations(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the federationConfigurations property value. Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.
        Args:
            value: Value to set for the federationConfigurations property.
        """
        self._federation_configurations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "administrative_units": lambda n : setattr(self, 'administrative_units', n.get_collection_of_object_values(administrative_unit.AdministrativeUnit)),
            "attribute_sets": lambda n : setattr(self, 'attribute_sets', n.get_collection_of_object_values(attribute_set.AttributeSet)),
            "custom_security_attribute_definitions": lambda n : setattr(self, 'custom_security_attribute_definitions', n.get_collection_of_object_values(custom_security_attribute_definition.CustomSecurityAttributeDefinition)),
            "deleted_items": lambda n : setattr(self, 'deleted_items', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "feature_rollout_policies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(feature_rollout_policy.FeatureRolloutPolicy)),
            "federation_configurations": lambda n : setattr(self, 'federation_configurations', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "impacted_resources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(recommendation_resource.RecommendationResource)),
            "inbound_shared_user_profiles": lambda n : setattr(self, 'inbound_shared_user_profiles', n.get_collection_of_object_values(inbound_shared_user_profile.InboundSharedUserProfile)),
            "on_premises_synchronization": lambda n : setattr(self, 'on_premises_synchronization', n.get_collection_of_object_values(on_premises_directory_synchronization.OnPremisesDirectorySynchronization)),
            "outbound_shared_user_profiles": lambda n : setattr(self, 'outbound_shared_user_profiles', n.get_collection_of_object_values(outbound_shared_user_profile.OutboundSharedUserProfile)),
            "recommendations": lambda n : setattr(self, 'recommendations', n.get_collection_of_object_values(recommendation.Recommendation)),
            "shared_email_domains": lambda n : setattr(self, 'shared_email_domains', n.get_collection_of_object_values(shared_email_domain.SharedEmailDomain)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def impacted_resources(self,) -> Optional[List[recommendation_resource.RecommendationResource]]:
        """
        Gets the impactedResources property value. The impactedResources property
        Returns: Optional[List[recommendation_resource.RecommendationResource]]
        """
        return self._impacted_resources
    
    @impacted_resources.setter
    def impacted_resources(self,value: Optional[List[recommendation_resource.RecommendationResource]] = None) -> None:
        """
        Sets the impactedResources property value. The impactedResources property
        Args:
            value: Value to set for the impactedResources property.
        """
        self._impacted_resources = value
    
    @property
    def inbound_shared_user_profiles(self,) -> Optional[List[inbound_shared_user_profile.InboundSharedUserProfile]]:
        """
        Gets the inboundSharedUserProfiles property value. The inboundSharedUserProfiles property
        Returns: Optional[List[inbound_shared_user_profile.InboundSharedUserProfile]]
        """
        return self._inbound_shared_user_profiles
    
    @inbound_shared_user_profiles.setter
    def inbound_shared_user_profiles(self,value: Optional[List[inbound_shared_user_profile.InboundSharedUserProfile]] = None) -> None:
        """
        Sets the inboundSharedUserProfiles property value. The inboundSharedUserProfiles property
        Args:
            value: Value to set for the inboundSharedUserProfiles property.
        """
        self._inbound_shared_user_profiles = value
    
    @property
    def on_premises_synchronization(self,) -> Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]]:
        """
        Gets the onPremisesSynchronization property value. A container for on-premises directory synchronization functionalities that are available for the organization.
        Returns: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]]
        """
        return self._on_premises_synchronization
    
    @on_premises_synchronization.setter
    def on_premises_synchronization(self,value: Optional[List[on_premises_directory_synchronization.OnPremisesDirectorySynchronization]] = None) -> None:
        """
        Sets the onPremisesSynchronization property value. A container for on-premises directory synchronization functionalities that are available for the organization.
        Args:
            value: Value to set for the onPremisesSynchronization property.
        """
        self._on_premises_synchronization = value
    
    @property
    def outbound_shared_user_profiles(self,) -> Optional[List[outbound_shared_user_profile.OutboundSharedUserProfile]]:
        """
        Gets the outboundSharedUserProfiles property value. The outboundSharedUserProfiles property
        Returns: Optional[List[outbound_shared_user_profile.OutboundSharedUserProfile]]
        """
        return self._outbound_shared_user_profiles
    
    @outbound_shared_user_profiles.setter
    def outbound_shared_user_profiles(self,value: Optional[List[outbound_shared_user_profile.OutboundSharedUserProfile]] = None) -> None:
        """
        Sets the outboundSharedUserProfiles property value. The outboundSharedUserProfiles property
        Args:
            value: Value to set for the outboundSharedUserProfiles property.
        """
        self._outbound_shared_user_profiles = value
    
    @property
    def recommendations(self,) -> Optional[List[recommendation.Recommendation]]:
        """
        Gets the recommendations property value. The recommendations property
        Returns: Optional[List[recommendation.Recommendation]]
        """
        return self._recommendations
    
    @recommendations.setter
    def recommendations(self,value: Optional[List[recommendation.Recommendation]] = None) -> None:
        """
        Sets the recommendations property value. The recommendations property
        Args:
            value: Value to set for the recommendations property.
        """
        self._recommendations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("administrativeUnits", self.administrative_units)
        writer.write_collection_of_object_values("attributeSets", self.attribute_sets)
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
    
    @property
    def shared_email_domains(self,) -> Optional[List[shared_email_domain.SharedEmailDomain]]:
        """
        Gets the sharedEmailDomains property value. The sharedEmailDomains property
        Returns: Optional[List[shared_email_domain.SharedEmailDomain]]
        """
        return self._shared_email_domains
    
    @shared_email_domains.setter
    def shared_email_domains(self,value: Optional[List[shared_email_domain.SharedEmailDomain]] = None) -> None:
        """
        Sets the sharedEmailDomains property value. The sharedEmailDomains property
        Args:
            value: Value to set for the sharedEmailDomains property.
        """
        self._shared_email_domains = value
    

