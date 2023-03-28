from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import security_baseline_state_summary

from . import security_baseline_state_summary

class SecurityBaselineCategoryStateSummary(security_baseline_state_summary.SecurityBaselineStateSummary):
    def __init__(self,) -> None:
        """
        Instantiates a new SecurityBaselineCategoryStateSummary and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.securityBaselineCategoryStateSummary"
        # The category name
        self._display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineCategoryStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineCategoryStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineCategoryStateSummary()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The category name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The category name
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import security_baseline_state_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

