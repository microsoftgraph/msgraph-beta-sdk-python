from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_uploaded_presentation = lazy_import('msgraph.generated.models.group_policy_uploaded_presentation')

class GroupPolicyPresentationDecimalTextBox(group_policy_uploaded_presentation.GroupPolicyUploadedPresentation):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationDecimalTextBox and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyPresentationDecimalTextBox"
        # An unsigned integer that specifies the initial value for the decimal text box. The default value is 1.
        self._default_value: Optional[int] = None
        # An unsigned integer that specifies the maximum allowed value. The default value is 9999.
        self._max_value: Optional[int] = None
        # An unsigned integer that specifies the minimum allowed value. The default value is 0.
        self._min_value: Optional[int] = None
        # Requirement to enter a value in the parameter box. The default value is false.
        self._required: Optional[bool] = None
        # If true, create a spin control; otherwise, create a text box for numeric entry. The default value is true.
        self._spin: Optional[bool] = None
        # An unsigned integer that specifies the increment of change for the spin control. The default value is 1.
        self._spin_step: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationDecimalTextBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationDecimalTextBox
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationDecimalTextBox()
    
    @property
    def default_value(self,) -> Optional[int]:
        """
        Gets the defaultValue property value. An unsigned integer that specifies the initial value for the decimal text box. The default value is 1.
        Returns: Optional[int]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultValue property value. An unsigned integer that specifies the initial value for the decimal text box. The default value is 1.
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_int_value()),
            "max_value": lambda n : setattr(self, 'max_value', n.get_int_value()),
            "min_value": lambda n : setattr(self, 'min_value', n.get_int_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "spin": lambda n : setattr(self, 'spin', n.get_bool_value()),
            "spin_step": lambda n : setattr(self, 'spin_step', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_value(self,) -> Optional[int]:
        """
        Gets the maxValue property value. An unsigned integer that specifies the maximum allowed value. The default value is 9999.
        Returns: Optional[int]
        """
        return self._max_value
    
    @max_value.setter
    def max_value(self,value: Optional[int] = None) -> None:
        """
        Sets the maxValue property value. An unsigned integer that specifies the maximum allowed value. The default value is 9999.
        Args:
            value: Value to set for the maxValue property.
        """
        self._max_value = value
    
    @property
    def min_value(self,) -> Optional[int]:
        """
        Gets the minValue property value. An unsigned integer that specifies the minimum allowed value. The default value is 0.
        Returns: Optional[int]
        """
        return self._min_value
    
    @min_value.setter
    def min_value(self,value: Optional[int] = None) -> None:
        """
        Sets the minValue property value. An unsigned integer that specifies the minimum allowed value. The default value is 0.
        Args:
            value: Value to set for the minValue property.
        """
        self._min_value = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Requirement to enter a value in the parameter box. The default value is false.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Requirement to enter a value in the parameter box. The default value is false.
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("defaultValue", self.default_value)
        writer.write_int_value("maxValue", self.max_value)
        writer.write_int_value("minValue", self.min_value)
        writer.write_bool_value("required", self.required)
        writer.write_bool_value("spin", self.spin)
        writer.write_int_value("spinStep", self.spin_step)
    
    @property
    def spin(self,) -> Optional[bool]:
        """
        Gets the spin property value. If true, create a spin control; otherwise, create a text box for numeric entry. The default value is true.
        Returns: Optional[bool]
        """
        return self._spin
    
    @spin.setter
    def spin(self,value: Optional[bool] = None) -> None:
        """
        Sets the spin property value. If true, create a spin control; otherwise, create a text box for numeric entry. The default value is true.
        Args:
            value: Value to set for the spin property.
        """
        self._spin = value
    
    @property
    def spin_step(self,) -> Optional[int]:
        """
        Gets the spinStep property value. An unsigned integer that specifies the increment of change for the spin control. The default value is 1.
        Returns: Optional[int]
        """
        return self._spin_step
    
    @spin_step.setter
    def spin_step(self,value: Optional[int] = None) -> None:
        """
        Sets the spinStep property value. An unsigned integer that specifies the increment of change for the spin control. The default value is 1.
        Args:
            value: Value to set for the spinStep property.
        """
        self._spin_step = value
    

