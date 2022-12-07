from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_uploaded_presentation = lazy_import('msgraph.generated.models.group_policy_uploaded_presentation')

class GroupPolicyPresentationComboBox(group_policy_uploaded_presentation.GroupPolicyUploadedPresentation):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationComboBox and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyPresentationComboBox"
        # Localized default string displayed in the combo box. The default value is empty.
        self._default_value: Optional[str] = None
        # An unsigned integer that specifies the maximum number of text characters for the parameter. The default value is 1023.
        self._max_length: Optional[int] = None
        # Specifies whether a value must be specified for the parameter. The default value is false.
        self._required: Optional[bool] = None
        # Localized strings listed in the drop-down list of the combo box. The default value is empty.
        self._suggestions: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationComboBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationComboBox
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationComboBox()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. Localized default string displayed in the combo box. The default value is empty.
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. Localized default string displayed in the combo box. The default value is empty.
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
            "default_value": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "max_length": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "suggestions": lambda n : setattr(self, 'suggestions', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_length(self,) -> Optional[int]:
        """
        Gets the maxLength property value. An unsigned integer that specifies the maximum number of text characters for the parameter. The default value is 1023.
        Returns: Optional[int]
        """
        return self._max_length
    
    @max_length.setter
    def max_length(self,value: Optional[int] = None) -> None:
        """
        Sets the maxLength property value. An unsigned integer that specifies the maximum number of text characters for the parameter. The default value is 1023.
        Args:
            value: Value to set for the maxLength property.
        """
        self._max_length = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Specifies whether a value must be specified for the parameter. The default value is false.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Specifies whether a value must be specified for the parameter. The default value is false.
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
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_int_value("maxLength", self.max_length)
        writer.write_bool_value("required", self.required)
        writer.write_collection_of_primitive_values("suggestions", self.suggestions)
    
    @property
    def suggestions(self,) -> Optional[List[str]]:
        """
        Gets the suggestions property value. Localized strings listed in the drop-down list of the combo box. The default value is empty.
        Returns: Optional[List[str]]
        """
        return self._suggestions
    
    @suggestions.setter
    def suggestions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the suggestions property value. Localized strings listed in the drop-down list of the combo box. The default value is empty.
        Args:
            value: Value to set for the suggestions property.
        """
        self._suggestions = value
    

