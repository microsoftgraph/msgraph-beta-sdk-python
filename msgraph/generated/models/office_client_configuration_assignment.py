from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, office_configuration_assignment_target

from . import entity

class OfficeClientConfigurationAssignment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new officeClientConfigurationAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The target property
        self._target: Optional[office_configuration_assignment_target.OfficeConfigurationAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeClientConfigurationAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeClientConfigurationAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeClientConfigurationAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, office_configuration_assignment_target

        fields: Dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(office_configuration_assignment_target.OfficeConfigurationAssignmentTarget)),
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
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[office_configuration_assignment_target.OfficeConfigurationAssignmentTarget]:
        """
        Gets the target property value. The target property
        Returns: Optional[office_configuration_assignment_target.OfficeConfigurationAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[office_configuration_assignment_target.OfficeConfigurationAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The target property
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

