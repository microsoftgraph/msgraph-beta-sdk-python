from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AdminReportSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new adminReportSettings and sets the default values.
        """
        super().__init__()
        # If set to true, all reports will conceal user information such as usernames, groups, and sites. If false, all reports will show identifiable information. This property represents a setting in the Microsoft 365 admin center. Required.
        self._display_concealed_names: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminReportSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminReportSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdminReportSettings()
    
    @property
    def display_concealed_names(self,) -> Optional[bool]:
        """
        Gets the displayConcealedNames property value. If set to true, all reports will conceal user information such as usernames, groups, and sites. If false, all reports will show identifiable information. This property represents a setting in the Microsoft 365 admin center. Required.
        Returns: Optional[bool]
        """
        return self._display_concealed_names
    
    @display_concealed_names.setter
    def display_concealed_names(self,value: Optional[bool] = None) -> None:
        """
        Sets the displayConcealedNames property value. If set to true, all reports will conceal user information such as usernames, groups, and sites. If false, all reports will show identifiable information. This property represents a setting in the Microsoft 365 admin center. Required.
        Args:
            value: Value to set for the displayConcealedNames property.
        """
        self._display_concealed_names = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_concealed_names": lambda n : setattr(self, 'display_concealed_names', n.get_bool_value()),
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
        writer.write_bool_value("displayConcealedNames", self.display_concealed_names)
    

