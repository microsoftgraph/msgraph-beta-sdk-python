from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_uploaded_presentation = lazy_import('msgraph.generated.models.group_policy_uploaded_presentation')

class GroupPolicyPresentationListBox(group_policy_uploaded_presentation.GroupPolicyUploadedPresentation):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationListBox and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyPresentationListBox"
        # If this option is specified true the user must specify the registry subkey value and the registry subkey name. The list box shows two columns, one for the name and one for the data. The default value is false.
        self._explicit_value: Optional[bool] = None
        # Not yet documented
        self._value_prefix: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationListBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationListBox
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationListBox()
    
    @property
    def explicit_value(self,) -> Optional[bool]:
        """
        Gets the explicitValue property value. If this option is specified true the user must specify the registry subkey value and the registry subkey name. The list box shows two columns, one for the name and one for the data. The default value is false.
        Returns: Optional[bool]
        """
        return self._explicit_value
    
    @explicit_value.setter
    def explicit_value(self,value: Optional[bool] = None) -> None:
        """
        Sets the explicitValue property value. If this option is specified true the user must specify the registry subkey value and the registry subkey name. The list box shows two columns, one for the name and one for the data. The default value is false.
        Args:
            value: Value to set for the explicitValue property.
        """
        self._explicit_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "explicit_value": lambda n : setattr(self, 'explicit_value', n.get_bool_value()),
            "value_prefix": lambda n : setattr(self, 'value_prefix', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("explicitValue", self.explicit_value)
        writer.write_str_value("valuePrefix", self.value_prefix)
    
    @property
    def value_prefix(self,) -> Optional[str]:
        """
        Gets the valuePrefix property value. Not yet documented
        Returns: Optional[str]
        """
        return self._value_prefix
    
    @value_prefix.setter
    def value_prefix(self,value: Optional[str] = None) -> None:
        """
        Sets the valuePrefix property value. Not yet documented
        Args:
            value: Value to set for the valuePrefix property.
        """
        self._value_prefix = value
    

