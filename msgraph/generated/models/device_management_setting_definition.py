from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')
device_management_setting_dependency = lazy_import('msgraph.generated.models.device_management_setting_dependency')
device_manangement_intent_value_type = lazy_import('msgraph.generated.models.device_manangement_intent_value_type')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementSettingDefinition(entity.Entity):
    """
    Entity representing the defintion for a given setting
    """
    @property
    def constraints(self,) -> Optional[List[device_management_constraint.DeviceManagementConstraint]]:
        """
        Gets the constraints property value. Collection of constraints for the setting value
        Returns: Optional[List[device_management_constraint.DeviceManagementConstraint]]
        """
        return self._constraints
    
    @constraints.setter
    def constraints(self,value: Optional[List[device_management_constraint.DeviceManagementConstraint]] = None) -> None:
        """
        Sets the constraints property value. Collection of constraints for the setting value
        Args:
            value: Value to set for the constraints property.
        """
        self._constraints = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingDefinition and sets the default values.
        """
        super().__init__()
        # Collection of constraints for the setting value
        self._constraints: Optional[List[device_management_constraint.DeviceManagementConstraint]] = None
        # Collection of dependencies on other settings
        self._dependencies: Optional[List[device_management_setting_dependency.DeviceManagementSettingDependency]] = None
        # The setting's description
        self._description: Optional[str] = None
        # The setting's display name
        self._display_name: Optional[str] = None
        # Url to setting documentation
        self._documentation_url: Optional[str] = None
        # subtitle of the setting header for more details about the category/section
        self._header_subtitle: Optional[str] = None
        # title of the setting header represents a category/section of a setting/settings
        self._header_title: Optional[str] = None
        # If the setting is top level, it can be configured without the need to be wrapped in a collection or complex setting
        self._is_top_level: Optional[bool] = None
        # Keywords associated with the setting
        self._keywords: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Placeholder text as an example of valid input
        self._placeholder_text: Optional[str] = None
        # The valueType property
        self._value_type: Optional[device_manangement_intent_value_type.DeviceManangementIntentValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingDefinition()
    
    @property
    def dependencies(self,) -> Optional[List[device_management_setting_dependency.DeviceManagementSettingDependency]]:
        """
        Gets the dependencies property value. Collection of dependencies on other settings
        Returns: Optional[List[device_management_setting_dependency.DeviceManagementSettingDependency]]
        """
        return self._dependencies
    
    @dependencies.setter
    def dependencies(self,value: Optional[List[device_management_setting_dependency.DeviceManagementSettingDependency]] = None) -> None:
        """
        Sets the dependencies property value. Collection of dependencies on other settings
        Args:
            value: Value to set for the dependencies property.
        """
        self._dependencies = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The setting's description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The setting's description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The setting's display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The setting's display name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def documentation_url(self,) -> Optional[str]:
        """
        Gets the documentationUrl property value. Url to setting documentation
        Returns: Optional[str]
        """
        return self._documentation_url
    
    @documentation_url.setter
    def documentation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the documentationUrl property value. Url to setting documentation
        Args:
            value: Value to set for the documentationUrl property.
        """
        self._documentation_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "constraints": lambda n : setattr(self, 'constraints', n.get_collection_of_object_values(device_management_constraint.DeviceManagementConstraint)),
            "dependencies": lambda n : setattr(self, 'dependencies', n.get_collection_of_object_values(device_management_setting_dependency.DeviceManagementSettingDependency)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "documentation_url": lambda n : setattr(self, 'documentation_url', n.get_str_value()),
            "header_subtitle": lambda n : setattr(self, 'header_subtitle', n.get_str_value()),
            "header_title": lambda n : setattr(self, 'header_title', n.get_str_value()),
            "is_top_level": lambda n : setattr(self, 'is_top_level', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "placeholder_text": lambda n : setattr(self, 'placeholder_text', n.get_str_value()),
            "value_type": lambda n : setattr(self, 'value_type', n.get_enum_value(device_manangement_intent_value_type.DeviceManangementIntentValueType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def header_subtitle(self,) -> Optional[str]:
        """
        Gets the headerSubtitle property value. subtitle of the setting header for more details about the category/section
        Returns: Optional[str]
        """
        return self._header_subtitle
    
    @header_subtitle.setter
    def header_subtitle(self,value: Optional[str] = None) -> None:
        """
        Sets the headerSubtitle property value. subtitle of the setting header for more details about the category/section
        Args:
            value: Value to set for the headerSubtitle property.
        """
        self._header_subtitle = value
    
    @property
    def header_title(self,) -> Optional[str]:
        """
        Gets the headerTitle property value. title of the setting header represents a category/section of a setting/settings
        Returns: Optional[str]
        """
        return self._header_title
    
    @header_title.setter
    def header_title(self,value: Optional[str] = None) -> None:
        """
        Sets the headerTitle property value. title of the setting header represents a category/section of a setting/settings
        Args:
            value: Value to set for the headerTitle property.
        """
        self._header_title = value
    
    @property
    def is_top_level(self,) -> Optional[bool]:
        """
        Gets the isTopLevel property value. If the setting is top level, it can be configured without the need to be wrapped in a collection or complex setting
        Returns: Optional[bool]
        """
        return self._is_top_level
    
    @is_top_level.setter
    def is_top_level(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTopLevel property value. If the setting is top level, it can be configured without the need to be wrapped in a collection or complex setting
        Args:
            value: Value to set for the isTopLevel property.
        """
        self._is_top_level = value
    
    @property
    def keywords(self,) -> Optional[List[str]]:
        """
        Gets the keywords property value. Keywords associated with the setting
        Returns: Optional[List[str]]
        """
        return self._keywords
    
    @keywords.setter
    def keywords(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the keywords property value. Keywords associated with the setting
        Args:
            value: Value to set for the keywords property.
        """
        self._keywords = value
    
    @property
    def placeholder_text(self,) -> Optional[str]:
        """
        Gets the placeholderText property value. Placeholder text as an example of valid input
        Returns: Optional[str]
        """
        return self._placeholder_text
    
    @placeholder_text.setter
    def placeholder_text(self,value: Optional[str] = None) -> None:
        """
        Sets the placeholderText property value. Placeholder text as an example of valid input
        Args:
            value: Value to set for the placeholderText property.
        """
        self._placeholder_text = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("constraints", self.constraints)
        writer.write_collection_of_object_values("dependencies", self.dependencies)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("documentationUrl", self.documentation_url)
        writer.write_str_value("headerSubtitle", self.header_subtitle)
        writer.write_str_value("headerTitle", self.header_title)
        writer.write_bool_value("isTopLevel", self.is_top_level)
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_str_value("placeholderText", self.placeholder_text)
        writer.write_enum_value("valueType", self.value_type)
    
    @property
    def value_type(self,) -> Optional[device_manangement_intent_value_type.DeviceManangementIntentValueType]:
        """
        Gets the valueType property value. The valueType property
        Returns: Optional[device_manangement_intent_value_type.DeviceManangementIntentValueType]
        """
        return self._value_type
    
    @value_type.setter
    def value_type(self,value: Optional[device_manangement_intent_value_type.DeviceManangementIntentValueType] = None) -> None:
        """
        Sets the valueType property value. The valueType property
        Args:
            value: Value to set for the valueType property.
        """
        self._value_type = value
    

