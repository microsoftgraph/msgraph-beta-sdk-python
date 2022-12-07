from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ParentLabelDetails(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. The color that the user interface should display for the label, if configured.
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. The color that the user interface should display for the label, if configured.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new parentLabelDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The color that the user interface should display for the label, if configured.
        self._color: Optional[str] = None
        # The admin-defined description for the label.
        self._description: Optional[str] = None
        # The label ID is a globally unique identifier (GUID).
        self._id: Optional[str] = None
        # Indicates whether the label is active or not. Active labels should be hidden or disabled in user interfaces.
        self._is_active: Optional[bool] = None
        # The plaintext name of the label.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The parent property
        self._parent: Optional[ParentLabelDetails] = None
        # The sensitivity value of the label, where lower is less sensitive.
        self._sensitivity: Optional[int] = None
        # The tooltip that should be displayed for the label in a user interface.
        self._tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParentLabelDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParentLabelDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParentLabelDetails()
    
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
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(ParentLabelDetails)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The label ID is a globally unique identifier (GUID).
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The label ID is a globally unique identifier (GUID).
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in user interfaces.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the label is active or not. Active labels should be hidden or disabled in user interfaces.
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
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def parent(self,) -> Optional[ParentLabelDetails]:
        """
        Gets the parent property value. The parent property
        Returns: Optional[ParentLabelDetails]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[ParentLabelDetails] = None) -> None:
        """
        Sets the parent property value. The parent property
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parent", self.parent)
        writer.write_int_value("sensitivity", self.sensitivity)
        writer.write_str_value("tooltip", self.tooltip)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tooltip(self,) -> Optional[str]:
        """
        Gets the tooltip property value. The tooltip that should be displayed for the label in a user interface.
        Returns: Optional[str]
        """
        return self._tooltip
    
    @tooltip.setter
    def tooltip(self,value: Optional[str] = None) -> None:
        """
        Sets the tooltip property value. The tooltip that should be displayed for the label in a user interface.
        Args:
            value: Value to set for the tooltip property.
        """
        self._tooltip = value
    

