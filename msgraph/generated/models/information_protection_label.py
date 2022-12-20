from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
parent_label_details = lazy_import('msgraph.generated.models.parent_label_details')

class InformationProtectionLabel(entity.Entity):
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
        Instantiates a new informationProtectionLabel and sets the default values.
        """
        super().__init__()
        # The color that the UI should display for the label, if configured.
        self._color: Optional[str] = None
        # The admin-defined description for the label.
        self._description: Optional[str] = None
        # Indicates whether the label is active or not. Active labels should be hidden or disabled in UI.
        self._is_active: Optional[bool] = None
        # The plaintext name of the label.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parent label associated with a child label. Null if label has no parent.
        self._parent: Optional[parent_label_details.ParentLabelDetails] = None
        # The sensitivity value of the label, where lower is less sensitive.
        self._sensitivity: Optional[int] = None
        # The tooltip that should be displayed for the label in a UI.
        self._tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtectionLabel()
    
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(parent_label_details.ParentLabelDetails)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in UI.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in UI.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
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
    def parent(self,) -> Optional[parent_label_details.ParentLabelDetails]:
        """
        Gets the parent property value. The parent label associated with a child label. Null if label has no parent.
        Returns: Optional[parent_label_details.ParentLabelDetails]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[parent_label_details.ParentLabelDetails] = None) -> None:
        """
        Sets the parent property value. The parent label associated with a child label. Null if label has no parent.
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
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isActive", self.is_active)
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
    

