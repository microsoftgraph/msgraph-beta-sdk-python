from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')

class GroupPolicyPresentation(entity.Entity):
    """
    The base entity for the display presentation of any of the additional options in a group policy definition.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyPresentation and sets the default values.
        """
        super().__init__()
        # The group policy definition associated with the presentation.
        self._definition: Optional[group_policy_definition.GroupPolicyDefinition] = None
        # Localized text label for any presentation entity. The default value is empty.
        self._label: Optional[str] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentation()
    
    @property
    def definition(self,) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        Gets the definition property value. The group policy definition associated with the presentation.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[group_policy_definition.GroupPolicyDefinition] = None) -> None:
        """
        Sets the definition property value. The group policy definition associated with the presentation.
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(group_policy_definition.GroupPolicyDefinition)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. Localized text label for any presentation entity. The default value is empty.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. Localized text label for any presentation entity. The default value is empty.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("label", self.label)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

