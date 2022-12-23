from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class SensitivityLabel(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. The color that the UI should display for the label, if configured.
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. The color that the UI should display for the label, if configured.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sensitivityLabel and sets the default values.
        """
        super().__init__()
        # The color that the UI should display for the label, if configured.
        self._color: Optional[str] = None
        # Returns the supported content formats for the label.
        self._content_formats: Optional[List[str]] = None
        # The admin-defined description for the label.
        self._description: Optional[str] = None
        # Indicates whether the label has protection actions configured.
        self._has_protection: Optional[bool] = None
        # Indicates whether the label is active or not. Active labels should be hidden or disabled in the UI.
        self._is_active: Optional[bool] = None
        # Indicates whether the label can be applied to content. False if the label is a parent with child labels.
        self._is_appliable: Optional[bool] = None
        # The plaintext name of the label.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parent label associated with a child label. Null if the label has no parent.
        self._parent: Optional[SensitivityLabel] = None
        # The sensitivity value of the label, where lower is less sensitive.
        self._sensitivity: Optional[int] = None
        # The tooltip that should be displayed for the label in a UI.
        self._tooltip: Optional[str] = None
    
    @property
    def content_formats(self,) -> Optional[List[str]]:
        """
        Gets the contentFormats property value. Returns the supported content formats for the label.
        Returns: Optional[List[str]]
        """
        return self._content_formats
    
    @content_formats.setter
    def content_formats(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contentFormats property value. Returns the supported content formats for the label.
        Args:
            value: Value to set for the contentFormats property.
        """
        self._content_formats = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitivityLabel()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The admin-defined description for the label.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The admin-defined description for the label.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "content_formats": lambda n : setattr(self, 'content_formats', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "has_protection": lambda n : setattr(self, 'has_protection', n.get_bool_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "is_appliable": lambda n : setattr(self, 'is_appliable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(SensitivityLabel)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_protection(self,) -> Optional[bool]:
        """
        Gets the hasProtection property value. Indicates whether the label has protection actions configured.
        Returns: Optional[bool]
        """
        return self._has_protection
    
    @has_protection.setter
    def has_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasProtection property value. Indicates whether the label has protection actions configured.
        Args:
            value: Value to set for the hasProtection property.
        """
        self._has_protection = value
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in the UI.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in the UI.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    @property
    def is_appliable(self,) -> Optional[bool]:
        """
        Gets the isAppliable property value. Indicates whether the label can be applied to content. False if the label is a parent with child labels.
        Returns: Optional[bool]
        """
        return self._is_appliable
    
    @is_appliable.setter
    def is_appliable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAppliable property value. Indicates whether the label can be applied to content. False if the label is a parent with child labels.
        Args:
            value: Value to set for the isAppliable property.
        """
        self._is_appliable = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The plaintext name of the label.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The plaintext name of the label.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def parent(self,) -> Optional[SensitivityLabel]:
        """
        Gets the parent property value. The parent label associated with a child label. Null if the label has no parent.
        Returns: Optional[SensitivityLabel]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[SensitivityLabel] = None) -> None:
        """
        Sets the parent property value. The parent label associated with a child label. Null if the label has no parent.
        Args:
            value: Value to set for the parent property.
        """
        self._parent = value
    
    @property
    def sensitivity(self,) -> Optional[int]:
        """
        Gets the sensitivity property value. The sensitivity value of the label, where lower is less sensitive.
        Returns: Optional[int]
        """
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self,value: Optional[int] = None) -> None:
        """
        Sets the sensitivity property value. The sensitivity value of the label, where lower is less sensitive.
        Args:
            value: Value to set for the sensitivity property.
        """
        self._sensitivity = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("color", self.color)
        writer.write_collection_of_primitive_values("contentFormats", self.content_formats)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("hasProtection", self.has_protection)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isAppliable", self.is_appliable)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parent", self.parent)
        writer.write_int_value("sensitivity", self.sensitivity)
        writer.write_str_value("tooltip", self.tooltip)
    
    @property
    def tooltip(self,) -> Optional[str]:
        """
        Gets the tooltip property value. The tooltip that should be displayed for the label in a UI.
        Returns: Optional[str]
        """
        return self._tooltip
    
    @tooltip.setter
    def tooltip(self,value: Optional[str] = None) -> None:
        """
        Sets the tooltip property value. The tooltip that should be displayed for the label in a UI.
        Args:
            value: Value to set for the tooltip property.
        """
        self._tooltip = value
    

