from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_control_type = lazy_import('msgraph.generated.models.device_management_configuration_control_type')
device_management_configuration_referred_setting_information = lazy_import('msgraph.generated.models.device_management_configuration_referred_setting_information')
device_management_configuration_setting_access_types = lazy_import('msgraph.generated.models.device_management_configuration_setting_access_types')
device_management_configuration_setting_applicability = lazy_import('msgraph.generated.models.device_management_configuration_setting_applicability')
device_management_configuration_setting_occurrence = lazy_import('msgraph.generated.models.device_management_configuration_setting_occurrence')
device_management_configuration_setting_usage = lazy_import('msgraph.generated.models.device_management_configuration_setting_usage')
device_management_configuration_setting_visibility = lazy_import('msgraph.generated.models.device_management_configuration_setting_visibility')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationSettingDefinition(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def access_types(self,) -> Optional[device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes]:
        """
        Gets the accessTypes property value. The accessTypes property
        Returns: Optional[device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes]
        """
        return self._access_types
    
    @access_types.setter
    def access_types(self,value: Optional[device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes] = None) -> None:
        """
        Sets the accessTypes property value. The accessTypes property
        Args:
            value: Value to set for the accessTypes property.
        """
        self._access_types = value
    
    @property
    def applicability(self,) -> Optional[device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability]:
        """
        Gets the applicability property value. Details which device setting is applicable on
        Returns: Optional[device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability]
        """
        return self._applicability
    
    @applicability.setter
    def applicability(self,value: Optional[device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability] = None) -> None:
        """
        Sets the applicability property value. Details which device setting is applicable on
        Args:
            value: Value to set for the applicability property.
        """
        self._applicability = value
    
    @property
    def base_uri(self,) -> Optional[str]:
        """
        Gets the baseUri property value. Base CSP Path
        Returns: Optional[str]
        """
        return self._base_uri
    
    @base_uri.setter
    def base_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the baseUri property value. Base CSP Path
        Args:
            value: Value to set for the baseUri property.
        """
        self._base_uri = value
    
    @property
    def category_id(self,) -> Optional[str]:
        """
        Gets the categoryId property value. Specifies the area group under which the setting is configured in a specified configuration service provider (CSP)
        Returns: Optional[str]
        """
        return self._category_id
    
    @category_id.setter
    def category_id(self,value: Optional[str] = None) -> None:
        """
        Sets the categoryId property value. Specifies the area group under which the setting is configured in a specified configuration service provider (CSP)
        Args:
            value: Value to set for the categoryId property.
        """
        self._category_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingDefinition and sets the default values.
        """
        super().__init__()
        # The accessTypes property
        self._access_types: Optional[device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes] = None
        # Details which device setting is applicable on
        self._applicability: Optional[device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability] = None
        # Base CSP Path
        self._base_uri: Optional[str] = None
        # Specifies the area group under which the setting is configured in a specified configuration service provider (CSP)
        self._category_id: Optional[str] = None
        # Description of the item
        self._description: Optional[str] = None
        # Display name of the item
        self._display_name: Optional[str] = None
        # Help text of the item
        self._help_text: Optional[str] = None
        # List of links more info for the setting can be found at
        self._info_urls: Optional[List[str]] = None
        # Tokens which to search settings on
        self._keywords: Optional[List[str]] = None
        # Name of the item
        self._name: Optional[str] = None
        # Indicates whether the setting is required or not
        self._occurrence: Optional[device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Offset CSP Path from Base
        self._offset_uri: Optional[str] = None
        # List of referred setting information.
        self._referred_setting_information_list: Optional[List[device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation]] = None
        # Root setting definition if the setting is a child setting.
        self._root_definition_id: Optional[str] = None
        # Supported setting types
        self._setting_usage: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage] = None
        # Setting control type representation in the UX
        self._ux_behavior: Optional[device_management_configuration_control_type.DeviceManagementConfigurationControlType] = None
        # Item Version
        self._version: Optional[str] = None
        # Supported setting types
        self._visibility: Optional[device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the item
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the item
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the item
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the item
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_types": lambda n : setattr(self, 'access_types', n.get_enum_value(device_management_configuration_setting_access_types.DeviceManagementConfigurationSettingAccessTypes)),
            "applicability": lambda n : setattr(self, 'applicability', n.get_object_value(device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability)),
            "base_uri": lambda n : setattr(self, 'base_uri', n.get_str_value()),
            "category_id": lambda n : setattr(self, 'category_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "help_text": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "info_urls": lambda n : setattr(self, 'info_urls', n.get_collection_of_primitive_values(str)),
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "occurrence": lambda n : setattr(self, 'occurrence', n.get_object_value(device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence)),
            "offset_uri": lambda n : setattr(self, 'offset_uri', n.get_str_value()),
            "referred_setting_information_list": lambda n : setattr(self, 'referred_setting_information_list', n.get_collection_of_object_values(device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation)),
            "root_definition_id": lambda n : setattr(self, 'root_definition_id', n.get_str_value()),
            "setting_usage": lambda n : setattr(self, 'setting_usage', n.get_enum_value(device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage)),
            "ux_behavior": lambda n : setattr(self, 'ux_behavior', n.get_enum_value(device_management_configuration_control_type.DeviceManagementConfigurationControlType)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def help_text(self,) -> Optional[str]:
        """
        Gets the helpText property value. Help text of the item
        Returns: Optional[str]
        """
        return self._help_text
    
    @help_text.setter
    def help_text(self,value: Optional[str] = None) -> None:
        """
        Sets the helpText property value. Help text of the item
        Args:
            value: Value to set for the helpText property.
        """
        self._help_text = value
    
    @property
    def info_urls(self,) -> Optional[List[str]]:
        """
        Gets the infoUrls property value. List of links more info for the setting can be found at
        Returns: Optional[List[str]]
        """
        return self._info_urls
    
    @info_urls.setter
    def info_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the infoUrls property value. List of links more info for the setting can be found at
        Args:
            value: Value to set for the infoUrls property.
        """
        self._info_urls = value
    
    @property
    def keywords(self,) -> Optional[List[str]]:
        """
        Gets the keywords property value. Tokens which to search settings on
        Returns: Optional[List[str]]
        """
        return self._keywords
    
    @keywords.setter
    def keywords(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the keywords property value. Tokens which to search settings on
        Args:
            value: Value to set for the keywords property.
        """
        self._keywords = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the item
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the item
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def occurrence(self,) -> Optional[device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence]:
        """
        Gets the occurrence property value. Indicates whether the setting is required or not
        Returns: Optional[device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence]
        """
        return self._occurrence
    
    @occurrence.setter
    def occurrence(self,value: Optional[device_management_configuration_setting_occurrence.DeviceManagementConfigurationSettingOccurrence] = None) -> None:
        """
        Sets the occurrence property value. Indicates whether the setting is required or not
        Args:
            value: Value to set for the occurrence property.
        """
        self._occurrence = value
    
    @property
    def offset_uri(self,) -> Optional[str]:
        """
        Gets the offsetUri property value. Offset CSP Path from Base
        Returns: Optional[str]
        """
        return self._offset_uri
    
    @offset_uri.setter
    def offset_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the offsetUri property value. Offset CSP Path from Base
        Args:
            value: Value to set for the offsetUri property.
        """
        self._offset_uri = value
    
    @property
    def referred_setting_information_list(self,) -> Optional[List[device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation]]:
        """
        Gets the referredSettingInformationList property value. List of referred setting information.
        Returns: Optional[List[device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation]]
        """
        return self._referred_setting_information_list
    
    @referred_setting_information_list.setter
    def referred_setting_information_list(self,value: Optional[List[device_management_configuration_referred_setting_information.DeviceManagementConfigurationReferredSettingInformation]] = None) -> None:
        """
        Sets the referredSettingInformationList property value. List of referred setting information.
        Args:
            value: Value to set for the referredSettingInformationList property.
        """
        self._referred_setting_information_list = value
    
    @property
    def root_definition_id(self,) -> Optional[str]:
        """
        Gets the rootDefinitionId property value. Root setting definition if the setting is a child setting.
        Returns: Optional[str]
        """
        return self._root_definition_id
    
    @root_definition_id.setter
    def root_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the rootDefinitionId property value. Root setting definition if the setting is a child setting.
        Args:
            value: Value to set for the rootDefinitionId property.
        """
        self._root_definition_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("accessTypes", self.access_types)
        writer.write_object_value("applicability", self.applicability)
        writer.write_str_value("baseUri", self.base_uri)
        writer.write_str_value("categoryId", self.category_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_collection_of_primitive_values("infoUrls", self.info_urls)
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_str_value("name", self.name)
        writer.write_object_value("occurrence", self.occurrence)
        writer.write_str_value("offsetUri", self.offset_uri)
        writer.write_collection_of_object_values("referredSettingInformationList", self.referred_setting_information_list)
        writer.write_str_value("rootDefinitionId", self.root_definition_id)
        writer.write_enum_value("settingUsage", self.setting_usage)
        writer.write_enum_value("uxBehavior", self.ux_behavior)
        writer.write_str_value("version", self.version)
        writer.write_enum_value("visibility", self.visibility)
    
    @property
    def setting_usage(self,) -> Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage]:
        """
        Gets the settingUsage property value. Supported setting types
        Returns: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage]
        """
        return self._setting_usage
    
    @setting_usage.setter
    def setting_usage(self,value: Optional[device_management_configuration_setting_usage.DeviceManagementConfigurationSettingUsage] = None) -> None:
        """
        Sets the settingUsage property value. Supported setting types
        Args:
            value: Value to set for the settingUsage property.
        """
        self._setting_usage = value
    
    @property
    def ux_behavior(self,) -> Optional[device_management_configuration_control_type.DeviceManagementConfigurationControlType]:
        """
        Gets the uxBehavior property value. Setting control type representation in the UX
        Returns: Optional[device_management_configuration_control_type.DeviceManagementConfigurationControlType]
        """
        return self._ux_behavior
    
    @ux_behavior.setter
    def ux_behavior(self,value: Optional[device_management_configuration_control_type.DeviceManagementConfigurationControlType] = None) -> None:
        """
        Sets the uxBehavior property value. Setting control type representation in the UX
        Args:
            value: Value to set for the uxBehavior property.
        """
        self._ux_behavior = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Item Version
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Item Version
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def visibility(self,) -> Optional[device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility]:
        """
        Gets the visibility property value. Supported setting types
        Returns: Optional[device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[device_management_configuration_setting_visibility.DeviceManagementConfigurationSettingVisibility] = None) -> None:
        """
        Sets the visibility property value. Supported setting types
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    

