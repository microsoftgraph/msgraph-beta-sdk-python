from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_uri import ConfigurationUri
    from .entity import Entity
    from .informational_urls import InformationalUrls
    from .supported_claim_configuration import SupportedClaimConfiguration

from .entity import Entity

@dataclass
class ApplicationTemplate(Entity):
    # The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
    categories: Optional[List[str]] = None
    # The URIs required for the single sign-on configuration of a preintegrated application.
    configuration_uris: Optional[List[ConfigurationUri]] = None
    # A description of the application.
    description: Optional[str] = None
    # The name of the application.
    display_name: Optional[str] = None
    # The home page URL of the application.
    home_page_url: Optional[str] = None
    # The informationalUrls property
    informational_urls: Optional[InformationalUrls] = None
    # The URL to get the logo for this application.
    logo_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the publisher for this application.
    publisher: Optional[str] = None
    # The supportedClaimConfiguration property
    supported_claim_configuration: Optional[SupportedClaimConfiguration] = None
    # The list of provisioning modes supported by this application. The only valid value is sync.
    supported_provisioning_types: Optional[List[str]] = None
    # The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.
    supported_single_sign_on_modes: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_uri import ConfigurationUri
        from .entity import Entity
        from .informational_urls import InformationalUrls
        from .supported_claim_configuration import SupportedClaimConfiguration

        from .configuration_uri import ConfigurationUri
        from .entity import Entity
        from .informational_urls import InformationalUrls
        from .supported_claim_configuration import SupportedClaimConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "configurationUris": lambda n : setattr(self, 'configuration_uris', n.get_collection_of_object_values(ConfigurationUri)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "homePageUrl": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "informationalUrls": lambda n : setattr(self, 'informational_urls', n.get_object_value(InformationalUrls)),
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "supportedClaimConfiguration": lambda n : setattr(self, 'supported_claim_configuration', n.get_object_value(SupportedClaimConfiguration)),
            "supportedProvisioningTypes": lambda n : setattr(self, 'supported_provisioning_types', n.get_collection_of_primitive_values(str)),
            "supportedSingleSignOnModes": lambda n : setattr(self, 'supported_single_sign_on_modes', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("configurationUris", self.configuration_uris)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_object_value("informationalUrls", self.informational_urls)
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_object_value("supportedClaimConfiguration", self.supported_claim_configuration)
        writer.write_collection_of_primitive_values("supportedProvisioningTypes", self.supported_provisioning_types)
        writer.write_collection_of_primitive_values("supportedSingleSignOnModes", self.supported_single_sign_on_modes)
    

