from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, informational_urls, supported_claim_configuration

from . import entity

class ApplicationTemplate(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ApplicationTemplate and sets the default values.
        """
        super().__init__()
        # The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
        self._categories: Optional[List[str]] = None
        # A description of the application.
        self._description: Optional[str] = None
        # The name of the application.
        self._display_name: Optional[str] = None
        # The home page URL of the application.
        self._home_page_url: Optional[str] = None
        # The informationalUrls property
        self._informational_urls: Optional[informational_urls.InformationalUrls] = None
        # The URL to get the logo for this application.
        self._logo_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The name of the publisher for this application.
        self._publisher: Optional[str] = None
        # The supportedClaimConfiguration property
        self._supported_claim_configuration: Optional[supported_claim_configuration.SupportedClaimConfiguration] = None
        # The list of provisioning modes supported by this application. The only valid value is sync.
        self._supported_provisioning_types: Optional[List[str]] = None
        # The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.
        self._supported_single_sign_on_modes: Optional[List[str]] = None
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicationTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description of the application.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description of the application.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the application.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the application.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, informational_urls, supported_claim_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "homePageUrl": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "informationalUrls": lambda n : setattr(self, 'informational_urls', n.get_object_value(informational_urls.InformationalUrls)),
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "supportedClaimConfiguration": lambda n : setattr(self, 'supported_claim_configuration', n.get_object_value(supported_claim_configuration.SupportedClaimConfiguration)),
            "supportedProvisioningTypes": lambda n : setattr(self, 'supported_provisioning_types', n.get_collection_of_primitive_values(str)),
            "supportedSingleSignOnModes": lambda n : setattr(self, 'supported_single_sign_on_modes', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_page_url(self,) -> Optional[str]:
        """
        Gets the homePageUrl property value. The home page URL of the application.
        Returns: Optional[str]
        """
        return self._home_page_url
    
    @home_page_url.setter
    def home_page_url(self,value: Optional[str] = None) -> None:
        """
        Sets the homePageUrl property value. The home page URL of the application.
        Args:
            value: Value to set for the home_page_url property.
        """
        self._home_page_url = value
    
    @property
    def informational_urls(self,) -> Optional[informational_urls.InformationalUrls]:
        """
        Gets the informationalUrls property value. The informationalUrls property
        Returns: Optional[informational_urls.InformationalUrls]
        """
        return self._informational_urls
    
    @informational_urls.setter
    def informational_urls(self,value: Optional[informational_urls.InformationalUrls] = None) -> None:
        """
        Sets the informationalUrls property value. The informationalUrls property
        Args:
            value: Value to set for the informational_urls property.
        """
        self._informational_urls = value
    
    @property
    def logo_url(self,) -> Optional[str]:
        """
        Gets the logoUrl property value. The URL to get the logo for this application.
        Returns: Optional[str]
        """
        return self._logo_url
    
    @logo_url.setter
    def logo_url(self,value: Optional[str] = None) -> None:
        """
        Sets the logoUrl property value. The URL to get the logo for this application.
        Args:
            value: Value to set for the logo_url property.
        """
        self._logo_url = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The name of the publisher for this application.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The name of the publisher for this application.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_object_value("informationalUrls", self.informational_urls)
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_object_value("supportedClaimConfiguration", self.supported_claim_configuration)
        writer.write_collection_of_primitive_values("supportedProvisioningTypes", self.supported_provisioning_types)
        writer.write_collection_of_primitive_values("supportedSingleSignOnModes", self.supported_single_sign_on_modes)
    
    @property
    def supported_claim_configuration(self,) -> Optional[supported_claim_configuration.SupportedClaimConfiguration]:
        """
        Gets the supportedClaimConfiguration property value. The supportedClaimConfiguration property
        Returns: Optional[supported_claim_configuration.SupportedClaimConfiguration]
        """
        return self._supported_claim_configuration
    
    @supported_claim_configuration.setter
    def supported_claim_configuration(self,value: Optional[supported_claim_configuration.SupportedClaimConfiguration] = None) -> None:
        """
        Sets the supportedClaimConfiguration property value. The supportedClaimConfiguration property
        Args:
            value: Value to set for the supported_claim_configuration property.
        """
        self._supported_claim_configuration = value
    
    @property
    def supported_provisioning_types(self,) -> Optional[List[str]]:
        """
        Gets the supportedProvisioningTypes property value. The list of provisioning modes supported by this application. The only valid value is sync.
        Returns: Optional[List[str]]
        """
        return self._supported_provisioning_types
    
    @supported_provisioning_types.setter
    def supported_provisioning_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedProvisioningTypes property value. The list of provisioning modes supported by this application. The only valid value is sync.
        Args:
            value: Value to set for the supported_provisioning_types property.
        """
        self._supported_provisioning_types = value
    
    @property
    def supported_single_sign_on_modes(self,) -> Optional[List[str]]:
        """
        Gets the supportedSingleSignOnModes property value. The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.
        Returns: Optional[List[str]]
        """
        return self._supported_single_sign_on_modes
    
    @supported_single_sign_on_modes.setter
    def supported_single_sign_on_modes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedSingleSignOnModes property value. The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.
        Args:
            value: Value to set for the supported_single_sign_on_modes property.
        """
        self._supported_single_sign_on_modes = value
    

