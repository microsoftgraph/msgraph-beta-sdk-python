from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_provider = lazy_import('msgraph.generated.models.identity_provider')
identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')
identity_user_flow = lazy_import('msgraph.generated.models.identity_user_flow')
identity_user_flow_attribute_assignment = lazy_import('msgraph.generated.models.identity_user_flow_attribute_assignment')
user_flow_api_connector_configuration = lazy_import('msgraph.generated.models.user_flow_api_connector_configuration')
user_flow_language_configuration = lazy_import('msgraph.generated.models.user_flow_language_configuration')

class B2cIdentityUserFlow(identity_user_flow.IdentityUserFlow):
    @property
    def api_connector_configuration(self,) -> Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration]:
        """
        Gets the apiConnectorConfiguration property value. Configuration for enabling an API connector for use as part of the user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        Returns: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration]
        """
        return self._api_connector_configuration
    
    @api_connector_configuration.setter
    def api_connector_configuration(self,value: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration] = None) -> None:
        """
        Sets the apiConnectorConfiguration property value. Configuration for enabling an API connector for use as part of the user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        Args:
            value: Value to set for the apiConnectorConfiguration property.
        """
        self._api_connector_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new B2cIdentityUserFlow and sets the default values.
        """
        super().__init__()
        # Configuration for enabling an API connector for use as part of the user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        self._api_connector_configuration: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration] = None
        # Indicates the default language of the b2cIdentityUserFlow that is used when no ui_locale tag is specified in the request. This field is RFC 5646 compliant.
        self._default_language_tag: Optional[str] = None
        # The identityProviders property
        self._identity_providers: Optional[List[identity_provider.IdentityProvider]] = None
        # The property that determines whether language customization is enabled within the B2C user flow. Language customization is not enabled by default for B2C user flows.
        self._is_language_customization_enabled: Optional[bool] = None
        # The languages supported for customization within the user flow. Language customization is not enabled by default in B2C user flows.
        self._languages: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user attribute assignments included in the user flow.
        self._user_attribute_assignments: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]] = None
        # The userFlowIdentityProviders property
        self._user_flow_identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> B2cIdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: B2cIdentityUserFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return B2cIdentityUserFlow()
    
    @property
    def default_language_tag(self,) -> Optional[str]:
        """
        Gets the defaultLanguageTag property value. Indicates the default language of the b2cIdentityUserFlow that is used when no ui_locale tag is specified in the request. This field is RFC 5646 compliant.
        Returns: Optional[str]
        """
        return self._default_language_tag
    
    @default_language_tag.setter
    def default_language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLanguageTag property value. Indicates the default language of the b2cIdentityUserFlow that is used when no ui_locale tag is specified in the request. This field is RFC 5646 compliant.
        Args:
            value: Value to set for the defaultLanguageTag property.
        """
        self._default_language_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "api_connector_configuration": lambda n : setattr(self, 'api_connector_configuration', n.get_object_value(user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration)),
            "default_language_tag": lambda n : setattr(self, 'default_language_tag', n.get_str_value()),
            "identity_providers": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider.IdentityProvider)),
            "is_language_customization_enabled": lambda n : setattr(self, 'is_language_customization_enabled', n.get_bool_value()),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(user_flow_language_configuration.UserFlowLanguageConfiguration)),
            "user_attribute_assignments": lambda n : setattr(self, 'user_attribute_assignments', n.get_collection_of_object_values(identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment)),
            "user_flow_identity_providers": lambda n : setattr(self, 'user_flow_identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_providers(self,) -> Optional[List[identity_provider.IdentityProvider]]:
        """
        Gets the identityProviders property value. The identityProviders property
        Returns: Optional[List[identity_provider.IdentityProvider]]
        """
        return self._identity_providers
    
    @identity_providers.setter
    def identity_providers(self,value: Optional[List[identity_provider.IdentityProvider]] = None) -> None:
        """
        Sets the identityProviders property value. The identityProviders property
        Args:
            value: Value to set for the identityProviders property.
        """
        self._identity_providers = value
    
    @property
    def is_language_customization_enabled(self,) -> Optional[bool]:
        """
        Gets the isLanguageCustomizationEnabled property value. The property that determines whether language customization is enabled within the B2C user flow. Language customization is not enabled by default for B2C user flows.
        Returns: Optional[bool]
        """
        return self._is_language_customization_enabled
    
    @is_language_customization_enabled.setter
    def is_language_customization_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLanguageCustomizationEnabled property value. The property that determines whether language customization is enabled within the B2C user flow. Language customization is not enabled by default for B2C user flows.
        Args:
            value: Value to set for the isLanguageCustomizationEnabled property.
        """
        self._is_language_customization_enabled = value
    
    @property
    def languages(self,) -> Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]]:
        """
        Gets the languages property value. The languages supported for customization within the user flow. Language customization is not enabled by default in B2C user flows.
        Returns: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]]
        """
        return self._languages
    
    @languages.setter
    def languages(self,value: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]] = None) -> None:
        """
        Sets the languages property value. The languages supported for customization within the user flow. Language customization is not enabled by default in B2C user flows.
        Args:
            value: Value to set for the languages property.
        """
        self._languages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("apiConnectorConfiguration", self.api_connector_configuration)
        writer.write_str_value("defaultLanguageTag", self.default_language_tag)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_bool_value("isLanguageCustomizationEnabled", self.is_language_customization_enabled)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("userAttributeAssignments", self.user_attribute_assignments)
        writer.write_collection_of_object_values("userFlowIdentityProviders", self.user_flow_identity_providers)
    
    @property
    def user_attribute_assignments(self,) -> Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]]:
        """
        Gets the userAttributeAssignments property value. The user attribute assignments included in the user flow.
        Returns: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]]
        """
        return self._user_attribute_assignments
    
    @user_attribute_assignments.setter
    def user_attribute_assignments(self,value: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]] = None) -> None:
        """
        Sets the userAttributeAssignments property value. The user attribute assignments included in the user flow.
        Args:
            value: Value to set for the userAttributeAssignments property.
        """
        self._user_attribute_assignments = value
    
    @property
    def user_flow_identity_providers(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the userFlowIdentityProviders property value. The userFlowIdentityProviders property
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._user_flow_identity_providers
    
    @user_flow_identity_providers.setter
    def user_flow_identity_providers(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the userFlowIdentityProviders property value. The userFlowIdentityProviders property
        Args:
            value: Value to set for the userFlowIdentityProviders property.
        """
        self._user_flow_identity_providers = value
    

